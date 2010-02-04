import re

from docutils import nodes
from docutils.parsers.rst import directives, roles

from sphinx import addnodes
from sphinx.roles import xfileref_role
from sphinx.directives.desc import DescDirective
from sphinx.util.compat import Directive, directive_dwim

ooc_sig_re = re.compile(
    r'''^ ([\w<>/]*[ /])?            # class name(s)
          ([\w<>~]+)  \s*             # thing name
          (?: \((.*)\))?           # optional: arguments
          (?:\s* -> \s* (.*))?  #           return annotation
          $                   # and nothing more
          ''', re.VERBOSE)
ooc_paramlist_re = re.compile(r'([\[\],])')  # split at '[', ']' and ','

class OOCDesc(DescDirective):
    """
        Description of a ooc object.
    """
    def get_signature_prefix(self, sig):
        return ''

    def needs_arglist(self):
        return False

    def parse_signature(self, sig, signode):
        """
            Returns (fully qualified name, classname if any).
        """
        m = ooc_sig_re.match(sig)
        if m is None:
            raise ValueError
        classname, name, arglist, retann = m.groups()
        if self.env.currclass:
            add_module = False
            if classname and classname.startswith(self.env.currclass):
                # classname is repeated in the signature
                classname = classname[len(self.env.currclass):].lstrip('/')
            elif classname:
                # class name given in the signature, but different,
                # should not happen
                fullname = self.env.currclass + '/' + classname + name
            else:
                # not given
                if isinstance(self, ClassmemberDesc):
                    fullname = self.env.currclass + ' ' + name
                else:
                    fullname = self.env.currclass + '/' + name
        else:
            add_module = True
            fullname = classname and classname + name or name

        prefix = self.get_signature_prefix(sig)
        if prefix:
            signode += addnodes.desc_annotation(prefix, prefix)
        #if classname:
        #   signode += addnodes.desc_addname(classname, classname)

        # exceptions are a special case, since they are documented in the
        # 'exceptions' module.
        elif add_module and self.env.config.add_module_names:
            modname = self.options.get('module', self.env.currmodule)
            if modname and modname != 'exceptions':
                nodetext = modname + '/'
                # signode += addnodes.desc_addname(nodetext, nodetext)

        signode += addnodes.desc_name(name, name)
        if not arglist:
            if self.needs_arglist():
                # for callables, add an empty parameter list
                signode += addnodes.desc_parameterlist()
            if retann:
                signode += addnodes.desc_returns(retann, retann)
            return fullname, classname
        signode += addnodes.desc_parameterlist()

        stack = [signode[-1]]
        for token in ooc_paramlist_re.split(arglist):
            if not token or token == ',' or token.isspace():
                pass
            else:
                token = token.strip()
                stack[-1] += addnodes.desc_parameter(token, token)
        if len(stack) != 1:
            raise ValueError
        if retann:
            signode += addnodes.desc_returns(retann, retann)
        return fullname, classname

    def get_index_text(self, modname, name):
        """
        Return the text for the index entry of the object.
        """
        raise NotImplementedError('must be implemented in subclasses')

    def add_target_and_index(self, name_cls, sig, signode):
        modname = self.options.get('module', self.env.currmodule)
        fullname = (modname and modname + '/' or '') + name_cls[0]
        # note target
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            self.env.note_descref(fullname, self.desctype, self.lineno)
        indextext = self.get_index_text(modname, name_cls)
        if indextext:
            self.indexnode['entries'].append(('single', indextext,
                                              fullname, fullname))

    def before_content(self):
        # needed for automatic qualification of members (reset in subclasses)
        self.clsname_set = False

    def after_content(self):
        if self.clsname_set:
            self.env.currclass = None

class ModulelevelDesc(OOCDesc):
    """
    Description of an object on module level (functions, data).
    """

    def needs_arglist(self):
        return self.desctype == 'function'

    def get_index_text(self, modname, name_cls):
        if self.desctype == 'function':
            if not modname:
                return _('%s() (built-in function)') % name_cls[0]
            return _('%s() (in module %s)') % (name_cls[0], modname)
        elif self.desctype == 'data':
            if not modname:
                return _('%s (built-in variable)') % name_cls[0]
            return _('%s (in module %s)') % (name_cls[0], modname)
        else:
            return ''

class ClasslikeDesc(OOCDesc):
    """
    Description of a class-like object (classes, covers).
    """

    def get_signature_prefix(self, sig):
        return self.desctype + ' '

    def get_index_text(self, modname, name_cls):
        if self.desctype == 'class':
            return _('%s (class in %s)') % (name_cls[0], modname)
        elif self.desctype == 'cover':
            return _('%s (cover in %s)') % (name_cls[0], modname)
        elif self.desctype == 'exception':
            return name_cls[0]
        else:
            return ''

    def before_content(self):
        OOCDesc.before_content(self)
        if self.names:
            self.env.currclass = self.names[0][0]
            self.clsname_set = True

class ClassmemberDesc(OOCDesc):
    """
    Description of a class member (methods, attributes).
    """

    def needs_arglist(self):
        return self.desctype.endswith('function')

    def get_signature_prefix(self, sig):
        if self.desctype == 'staticmemberfunction':
            return 'static member function '
        elif self.desctype == 'memberfunction':
            return 'member function '
        return ''

    def get_index_text(self, modname, name_cls):
        name, cls = name_cls
        add_modules = self.env.config.add_module_names
        if self.desctype == 'memberfunction':
            try:
                clsname, methname = name.rsplit(' ', 1)
            except ValueError:
                if modname:
                    return _('%s() (in module %s)') % (name, modname)
                else:
                    return '%s()' % name
            if modname and add_modules:
                return _('%s() (%s/%s member function)') % (methname, modname, clsname)
            else:
                return _('%s() (%s member function)') % (methname, clsname)
        elif self.desctype == 'staticmemberfunction':
            try:
                clsname, methname = name.rsplit(' ', 1)
            except ValueError:
                if modname:
                    return _('%s() (in module %s)') % (name, modname)
                else:
                    return '%s()' % name
            if modname and add_modules:
                return _('%s() (%s/%s static member function)') % (methname, modname,
                                                          clsname)
            else:
                return _('%s() (%s static member function)') % (methname, clsname)
        elif self.desctype == 'field':
            try:
                clsname, attrname = name.rsplit(' ', 1)
            except ValueError:
                if modname:
                    return _('%s (in module %s)') % (name, modname)
                else:
                    return name
            if modname and add_modules:
                return _('%s (%s/%s field)') % (attrname, modname, clsname)
            else:
                return _('%s (%s field)') % (attrname, clsname)
        else:
            return ''

    def before_content(self):
        OOCDesc.before_content(self)
        if self.names and self.names[-1][1] and not self.env.currclass:
            self.env.currclass = self.names[-1][1].strip('/ ')
            self.clsname_set = True


directives.register_directive('describe', directive_dwim(DescDirective))

directives.register_directive('function', directive_dwim(ModulelevelDesc))
directives.register_directive('data', directive_dwim(ModulelevelDesc))
directives.register_directive('class', directive_dwim(ClasslikeDesc))
directives.register_directive('cover', directive_dwim(ClasslikeDesc))

directives.register_directive('memberfunction', directive_dwim(ClassmemberDesc))
directives.register_directive('staticmemberfunction', directive_dwim(ClassmemberDesc))
directives.register_directive('field', directive_dwim(ClassmemberDesc))


