The ooc language
================

Hello world
-----------

Here's a small hello world in ooc::

    main: func {
        "Oh, hi world =)" println()
    }

But this is not the shortest hello world possible.
In fact, you don't even need a main function::

    "Hello world!" println()

Operator overloading
--------------------

Operator overloading works almost like a function declaration.

Let's see the difference::

    Bignum: class {
        // ...
    }
    
    add: func (left, right: Bignum) -> Bignum {
        // ...
    }
    
    operator + (left, right: Bignum) -> Bignum {
        // ...
    }
    
    b1 := Bignum new()
    b2 := Bignum new()
    
    b3 := add(b1, b2) // 'add' is called
    b4 := b1 + b2 // 'operator +' is called.

Valid operators are listed below::

    + - / *
    == != < <= > >=
    = += -= /= *=
    []
    []= // three arguments: the third is the rvalue of the assignment

It is not yet possible to define operator overloads as methods.

An interesting side-effect of defining overloads as functions, is that
you can add overloads to already-existing classes.

Syntax
------

ooc has a proper module system, it's easy to declare functions, does some type inference for you, and feature generics::

    import structs/ArrayList

    main: func {
        a := ArrayList<String> new()
    }

(note: this article is obviously a stub. The page at http://ooc-lang.org/syntax
needs to be migrated here.)
