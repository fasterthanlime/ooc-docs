Writing bindings manually
=========================

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

First, we'll include this header::

    include test

Then, you have to create a cover for the struct; let's call it ``EntryStruct``

.. note:: This naming scheme is only a convention.

::

    EntryStruct: cover from struct _Entry {
	m_name: extern String
	m_age: extern Int
    }

It would be nice to get rid of these ``m_`` prefixes. That's easy; you can
specify aliases by passing the original name to the ``extern`` keyword::

    EntryStruct: cover from struct _Entry {
	name: extern(m_name) String
	age: extern(m_age) Int
    }

Now, let us start wrapping the functions::

    create_entry: extern func -> EntryStruct*
    entry_set_name: extern func (entry: EntryStruct*, name: String)
    entry_set_age: extern func (entry: EntryStruct*, age: Int)
    print_entry: extern func (entry: EntryStruct*) -> Int

You see, we are just repeating the definitions in ooc syntax, with one
difference: We are using the :class:`String` type instead of Char* because the
ooc standard library defines a tasty cover for ``String`` that has some really
convenient methods.

If you are lazy, you can also leave out the argument names; the following would
work, too::

    create_entry: extern func -> EntryStruct*
    entry_set_name: extern func (EntryStruct*, String)
    entry_set_age: extern func (EntryStruct*, Int)
    print_entry: extern func (EntryStruct*) -> Int

Now, you are done.

But since the API of your C library is designed in a object-oriented way, it
would be nice to be able to use it in a object-oriented way in ooc.

Therefore, we define a cover from the ``EntryStruct*`` type, because the ``EntryStruct*``
works like a ``this`` pointer in the library: The pseudo-methods
(``entry_set_name``, ``entry_set_age``, ``print_entry``) take a ``EntryStruct*`` as
first argument, and the pseudo-constructor (``create_entry``) returns a
``EntryStruct*``::

    Entry: cover from EntryStruct* {
	setName: extern(entry_set_name) func (String)
	setAge: extern(entry_set_age) func (Int)
	print: extern(print_entry) func -> Int
    }

Now, we've added some "extern methods" very easily. Like we did for
the struct members, we just pass the real name of the C function to the
``extern`` keyword. In the argument list, we let out the first argument (the
*this pointer*).

But what for a constructor function like *create_entry*? We'll just define it
as a static method called ``new``::

    Entry: cover from EntryStruct* {
	new: extern(create_entry) func -> Entry
    }

Since we have defined all our C functions as extern methods now, we
can skip the definitions as extern functions; so our glue code looks like
that::

    include test

    EntryStruct: cover from struct _Entry {
	name: extern(m_name) String
	age: extern(m_age) Int
    }

    Entry: cover from EntryStruct* {
	new: extern(create_entry) func -> Entry
	setName: extern(entry_set_name) func (String)
	setAge: extern(entry_set_age) func (Int)
	print: extern(print_entry) func -> Int
    }

