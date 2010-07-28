The JSON output of the ooc compiler (proposal)
==============================================

JSON output of the ooc compiler is useful for automated bindings generation for foreign programming languages and
for API documentation generation.

Example ooc code
----------------

.. code-block:: ooc

    Something: class {
	value: String
	init: func (a: Int, b: String)
	fiddle: static func (value: Bool) -> Bool
	doNothing: func ~withSomething <T> (something: T) -> Int
	doNothing: func -> Int
    }
    SomethingSpecial: class extends Something {
	doSomethingSpecial: func (yay: String)
    }
    CoolFloat: cover from Float {
	sqrt: func -> Float
    }
    five := 5
    ohYeah: func (no: Something)
    killCoolFloat: func (fl: CoolFloat@)
    killInteger: func (integer: Integer*)
    

The JSON format
---------------

The root structure is an object containing some meta-information about the sourcefile. The rule: One sourcefile = one
module = one .json file.

All required keys:

``path``
    An absolute module path (e.g. ``"io/File"``)
``entities``
    See `entities`_.
``globalImports``
    A list of module paths that got imported globally explicitly (e.g. ``["io/File", "os/Process"]``)
``namespacedImports``
    An object mapping namespace names to imported module paths.

    Example::

	import io/File into IO
	import io/FileReader into IO
	import os/Process into OS

    gets translated to::

	{
	    "IO": ["io/File", "io/FileReader"],
	    "OS": ["os/Process"]
	}
``uses``
    A list of "used" usefiles (e.g. ``["mycoollib"]``)

Tags
~~~~

A tag defines an unique name for an entity. It is a mini description language:

.. productionlist:: 
    tag: modifier "(" parameters ")" 
       | identifier
    parameters: tag { "," tag }
    identifier: [a-zA-Z0-9_ ]+
    modifier: [a-zA-Z0-9_]+

Some examples for valid tags::

    test
    pointer(test)
    array(Int, 10)
    method(MyClass, yeaahh)

Tags for ordinary functions (i.e. not methods), classes, covers, global variables and interfaces are just the name of the symbol.

Tags for interface implementations are like this:

.. function:: interfaceImpl(interface, for)

    See `interfaceImpl`_.

Tags for members are consisting of a describing modifier and the class tag and the member name as parameters:

.. function:: method(class, name)
.. function:: field(class, name)
.. function:: enumElement(enum, name)

Tags for pointer and reference types just consist of the ``pointer``/``reference`` modifier and the type tag as parameter:

.. function:: pointer(type)
.. function:: reference(type)

Tags for multi types (only occur in return types) consist of the ``multi`` modifier and the type tags as parameters:

.. function:: multi(type1, type2, ...)

Tags for operators are a bit more complicated. They carry information about all types:

.. function:: operator(name, generics(...), arguments(...), return(...))

Nonexistent chunks can be omitted (e.g. ``operator(IDX, arguments(...), return(...)``).

.. function:: generics(T, U, V, ...)
    
    holds the generic types names

.. function:: arguments(Int, pointer(String), T, ...)

    holds the arguments types tags

.. function:: return(Int)

    holds the return type tag

.. _entities:

Entities
--------

Entities are described by a `members`_ list-of-lists.
It only contains the "root" entities which are part of the global namespaces (no class members).

Now, each entity has some essential keys:

``type``
    describes the type of the entity. Possible values are:
     * ``"function"``
     * ``"method"``
     * ``"globalVariable"``
     * ``"field"``
     * ``"class"``
     * ``"cover"``
     * ``"enum"``
     * ``"enumElement"``
     * ``"operator"``
     * ``"interface"``
     * ``"interfaceImpl"``
``tag``
    defines an unique name for the entity.
``doc``
    The oocdoc documentation if given (defaults to an empty string)

The following keys are somewhat special:

``unmangled``
    If the user has marked the entity as ``unmangled``, but didn't specify
    a name, this is ``true``. If the user has marked this entity and
    provided a name, this is the name. Otherwise, this is ``false``.
    
.. note:: In the current implementation, ``unmangled`` is only given for functions, methods, global variables and fields, because classes, covers, enums and enum elements can't have an ``unmangled`` name.

``fullName``
    The full, mangled name of the entity, like it appears in the C sourcecode.

.. note:: ``fullName`` is given for all types except ``enumElement`` and ``field``.

``version``
    A version spec or null. See `version specs`_.

.. note:: ``version`` is given for all entities, but will always be null for globalVariable, field and operator entities.

.. _version specs:

version specs
~~~~~~~~~~~~~

Version specs are represented in the tag mini language with these modifiers:

.. function:: and(spec1, spec2)

    Equivalent of ``version(spec1 && spec2)``

.. function:: or(spec1, spec2)

    Equivalent of ``version(spec1 || spec2)``

.. function:: not(spec)

    Equivalent of ``version(!(spec))``

``spec`` can either be another sub-spec or a version name.

Example::

    version(!(gc && (win32 || win64)))
    
    =>

    "not(and(gc,or(win32,win64)))"

.. _members:

members
~~~~~~~

Since there can exist multiple versions for every member always, members are organized in a
way that allows multiple entities with equal tags to coexist in peace and harmony.

Members are organized as a list-of-lists. One sublist describes one member with all its versions.
So a sublist has this format::

    [name, member_versionA, member_versionB, ...]

Where the elements 2 to infinity are just real subentities with the same tag, but different
``version`` fields.

.. _json-function-entity:

``function``
~~~~~~~~~~~~

A function entity has the following attributes:

``name``
    Although the name is identical to the tag, it contains the name of the function. It also contains the suffix (if given), separated by a "~" char. So, a ``doSomething: func ~string`` would have the name "doSomething~string".
``modifiers``
    A list of function modifiers. Possible modifiers are:

     * ``const``
     * ``static``
     * ``final``
     * ``inline``
     * ``proto``
``genericTypes``
    The names of generic parameter types as a list.
``extern``
    Either ``true`` (if it's an extern function, but not aliased) or a string containing the original name of
    the function (if it's an aliased extern function).
``returnType``
    Either ``null`` if the function has no return value or the tag of the return type.
``arguments``
    A list of 2-element lists ``[name, argument tag, modifiers or null]``.
    Example::
	
	test: func (name: const String, age, foobar: Int*)

    generates

    .. code-block:: javascript

	[
	    ["name", "String", ["const"]],
	    ["age", "pointer(Int)", null],
	    ["foobar", "pointer(Int)", null]
	]

.. note:: If a function has varargs, the last element in the "arguments" list will be an argument named "..." with the type "": ``["...", "", null]``.

``method``
~~~~~~~~~~

A method entity has the same attributes as the :ref:`function entity <json-function-entity>`,
but a ``method`` tag.

.. note:: The convenient ``This`` type has to be resolved by the compiler.
	
.. _json-globalVariable-entity:

``globalVariable``
~~~~~~~~~~~~~~~~~~

``name``
    Guess what!
``modifiers``
    A list of modifiers. Possible modifiers:

    * ``const``
    * ``static``
``value``
    The value of the variable as string, if it's known (i.e. for const variables), otherwise ``null``.
``varType``
    The tag of the type of the variable.

    .. note:: The compiler has to resolve the type of the variable for implicit assignments (``:=``).
``extern``
    Either ``true`` (if it's an extern field, but not aliased) or a string containing the original name of
    the field (if it's an aliased extern field).
``propertyData``
    An object that is only present if the variable is a property. Otherwise, it's ``null``.

    See `propertyData`_.

.. _propertyData:

``propertyData``
^^^^^^^^^^^^^^^^

An object holding information on the property. Can be present in ``field`` and ``globalVariable`` entities.

``hasGetter``
    ``true`` if the property has a getter (custom or default)
``hasSetter``
    ``true`` if the property has a setter (custom or default)
``fullGetterName``
    The full, mangled name of the getter function, like it appears in the C sourcecode or ``null`` if there
    is no getter.
``fullSetterName``
    The full, mangled name of the setter function, like it appears in the C sourcecode or ``null`` if there
    is no setter.
    
``field``
~~~~~~~~~

A field entity has the same attributes as the :ref:`globalVariable entity <json-globalVariable-entity>`, but a
``field`` tag.

.. _json-class-entity:

``class``
~~~~~~~~~

``name``
    Ha-Ha.
``genericTypes``
    A list of all generic type names or an empty list.
``extends``
    The tag of the class this class extends, or ``null``.
``members``
    `members`_
``abstract``
    A boolean that describes if the class is abstract or not.
``final``
    A boolean that describes if the class is final or not.

``cover``
~~~~~~~~~

``name``
    ...
``from``
    The tag of the type we're covering.
``extends``
    The tag of the class this class extends, or ``null``.
``members``
    `members`_
``enum``
~~~~~~~~

``name``
    !
``extern``
    Either ``true`` (if it's an extern field, but not aliased) or a string containing the original name of
    the field (if it's an aliased extern field).
``incrementOper``
    Increment operator as string. Either ``"+"`` (default) or ``"*"``.
``incrementStep``
    Increment step as int (defaults to ``1``)
``elements``
    A list of 2-element lists ``[name, element]`` where ``element`` is of the type ``enumElement``.

``enumElement``
~~~~~~~~~~~~~~~

``name``
    hihi
``extern``
    A string containing the element's extern name or null.
``value``
    The value as integer.

``operator``
~~~~~~~~~~~~

``symbol``
    The operator symbol as string. ``"+"`` or something.
``name``
    Name of the symbol as string like ``"PLUS"``. Used in operator tags.
``function``
    Subentity describing the generated function. Really like an ordinary function entity.

.. note:: The ``doc`` field is always an empty string here because rock has no support for
          oocdoc'ed operator declarations yet.

``interface``
~~~~~~~~~~~~~

``name``
    yaay
``members``
    `members`_

.. _interfaceImpl:

``interfaceImpl``
~~~~~~~~~~~~~~~~~

``for``
    Tag of the target class/cover.
``interface``
    Tag of the interface.

.. note:: The ``doc`` field is always empty for ``interfaceImpl``. A possible TODO.
