Operator overloading
====================

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

