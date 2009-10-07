Writing bindings
================

You can use any C library from ooc very easily. All what you need is to write
some code to let the compiler know the functions and types you are using.

Let's say you have this C code in a file called :file:`test.h`:

.. code-block:: c

    typedef struct _Entry {
	char* m_name;
	int m_age;
    } Entry;

    Entry* create_entry();
    void entry_set_name(Entry* entry, char* name);
    void entry_set_age(Entry* entry, int age);
    int print_entry(Entry* entry);

You have to create a cover for the struct::

    Entry: extern cover {
	m_name: extern String
	m_age: extern Int
    }

It would be nice to get rid of these ``m_`` prefixes. That's easy; you can
specify aliases by passing the original name to the ``extern`` keyword::

    Entry: extern cover {
	name: extern(m_name) String
	age: extern(m_age) Int
    }

Now, let us start wrapping the functions::

    create_entry: extern func -> Entry*
    entry_set_name: extern func (entry: Entry*, name: String)
    entry_set_age: extern func (entry: Entry*, age: Int)
    print_entry: extern func (entry: Entry*) -> Int

You see, we are just repeating the definitions in ooc syntax, with one
difference: We are using the :class:`String` type insted of Char* because the
ooc standard library defines a tasty cover for ``String`` that has some really
convenient methods.

If you are lazy, you can also leave out the argument names; the following would
work, too::

    create_entry: extern func -> Entry*
    entry_set_name: extern func (Entry*, String)
    entry_set_age: extern func (Entry*, Int)
    print_entry: extern func (Entry*) -> Int

Now, you are done.

But since the API of your C library is designed in a object-oriented way, it
would be nice to be able to use it in a object-oriented way in ooc.

Therefore, we define a cover from the ``Entry*`` type, because the ``Entry*``
works like a ``this`` pointer in the library: The pseudo-methods
(``entry_set_name``, ``entry_set_age``, ``print_entry``) take a ``Entry*`` as
first argument, and the pseudo-constructor (``create_entry``) returns a
``Entry*``::

    
