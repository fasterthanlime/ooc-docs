from docutils import nodes, utils
from docutils.parsers.rst import roles

from sphinx import addnodes
from sphinx.environment import BuildEnvironment
from sphinx.util import ws_re, caption_ref_re
from sphinx.roles import innernodetypes

def _fix_parens(typ, text, env):
    if typ in ('func', 'meth', 'cfunc'):
        if text.endswith('()'):
            # remove parentheses
            text = text[:-2]
        if env.config.add_function_parentheses:
            # add them back to all occurrences if configured
            text += '()'
    return text

def ooc_xfileref_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    env = inliner.document.settings.env
    if not typ:
        typ = env.config.default_role
    else:
        typ = typ.lower()
    text = utils.unescape(text)
    # if the first character is a bang, don't cross-reference at all
    if text[0:1] == '!':
        text = _fix_parens(typ, text[1:], env)
        return [innernodetypes.get(typ, nodes.literal)(
            rawtext, text, classes=['xref'])], []
    # we want a cross-reference, create the reference node
    nodeclass = (typ == 'download') and addnodes.download_reference or \
                addnodes.pending_xref
    pnode = nodeclass(rawtext, reftype=typ, refcaption=False,
                      modname=env.currmodule, classname=env.currclass)
    # we may need the line number for warnings
    pnode.line = lineno
    # the link title may differ from the target, but by default
    # they are the same
    title = target = text
    titleistarget = True
    # look if explicit title and target are given with `foo <bar>` syntax
    brace = text.find('<')
    if brace != -1:
        titleistarget = False
        pnode['refcaption'] = True
        m = caption_ref_re.match(text)
        if m:
            target = m.group(2)
            title = m.group(1)
        else:
            # fallback: everything after '<' is the target
            target = text[brace+1:]
            title = text[:brace]
    # special target for Python object cross-references
    if typ in ('data', 'exc', 'func', 'class', 'const', 'attr',
               'meth', 'mod', 'obj'):
        # fix-up parentheses in link title
        if titleistarget:
            title = title.lstrip('.')   # only has a meaning for the target
            target = target.lstrip('~') # only has a meaning for the title
            title = _fix_parens(typ, title, env)
            # if the first character is a tilde, don't display the module/class
            # parts of the contents
            if title[0:1] == '~':
                title = title[1:]
                dot = title.rfind('/')
                if dot != -1:
                    title = title[dot+1:]
        # remove parentheses from the target too
        if target.endswith('()'):
            target = target[:-2]
        # if the first character is a dot, search more specific namespaces first
        # else search builtins first
        if target[0:1] == '.':
            target = target[1:]
            pnode['refspecific'] = True
    # some other special cases for the target
    elif typ == 'option':
        program = env.currprogram
        if titleistarget:
            if ' ' in title and not (title.startswith('/') or
                                     title.startswith('-')):
                program, target = re.split(' (?=-|--|/)', title, 1)
                program = ws_re.sub('-', program)
                target = target.strip()
        elif ' ' in target:
            program, target = re.split(' (?=-|--|/)', target, 1)
            program = ws_re.sub('-', program)
        pnode['refprogram'] = program
    elif typ == 'term':
        # normalize whitespace in definition terms (if the term reference is
        # broken over a line, a newline will be in target)
        target = ws_re.sub(' ', target).lower()
    elif typ == 'ref':
        # reST label names are always lowercased
        target = ws_re.sub('', target).lower()
    elif typ == 'cfunc':
        # fix-up parens for C functions too
        if titleistarget:
            title = _fix_parens(typ, title, env)
        # remove parentheses from the target too
        if target.endswith('()'):
            target = target[:-2]
    else:
        # remove all whitespace to avoid referencing problems
        target = ws_re.sub('', target)
    pnode['reftarget'] = target
    pnode += innernodetypes.get(typ, nodes.literal)(rawtext, title,
                                                    classes=['xref'])
    return [pnode], []

roles.register_local_role('cover', ooc_xfileref_role)
BuildEnvironment.descroles = frozenset(set(BuildEnvironment.descroles) | set(('cover',)))
