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
       : identifier
    parameters: tag { "," tag }
    identifier: [a-zA-Z0-9_ ]+
    modifier: [a-zA-Z0-9_]+

Some examples for valid tags::

    test
    pointer(test)
    array(Int, 10)
    method(MyClass, yeaahh)

Tags for ordinary functions (i.e. not methods), classes, covers and global variables are just the name of the symbol.

Tags for members are consisting of a describing modifier and the class tag and the member name as parameters:

.. function:: method(class, name)
.. function:: field(class, name)

Tags for pointer and reference types just consist of the ``pointer``/``reference`` modifier and the type tag as parameter:

.. function:: pointer(type)
.. function:: reference(type)

.. _entities:

Entities
--------

Entities are described by a list of 2-element lists that contain symbol names (first element) and objects (second element).
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
``tag``
    defines an unique name for the entity.

The following keys exist for all entity types **except** ``field``:

``unmangled``
    If the user has marked the entity as ``unmangled``, but didn't specify
    a name, this is ``true``. If the user has marked this entity and
    provided a name, this is the name. Otherwise, this is ``false``.
    
.. note:: In the current implementation, ``unmangled`` is only given for functions, methods, global variables and fields, because classes and covers can't have an ``unmangled`` name yet.

``fullName``
    The full, mangled name of the entity, like it appears in the C sourcecode.

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
``doc``
    The oocdoc comment if available, or ``null``.
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
~~~~~~~~~~~~~~~~~~

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
``property_data``
    An object that is only present if the variable is a property. Otherwise, it's ``null``.

    See `property_data`_.

.. _property_data:

``property_data``
^^^^^^^^^^^^^^^^^

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
    A list of 2-element lists ``[name, entity]``.
``abstract``
    A boolean that describes if the class is abstract or not.
``doc``
    A string containing the oocdoc comment if available, or ``null``.

``cover``
~~~~~~~~~

Same attributes as :ref:`class <json-class-entity>`, but additionally:

``from``
    The tag of the type we're covering.

