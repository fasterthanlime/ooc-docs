Meta-classes
============

A little vocabulary
-------------------

In the following piece of code::

    dog := Dog new()
    
`dog` is an object, ie. an instance of the `Dog` class

A class is also an object! It's an instance of a meta-class.

Thus, `Dog` is a singleton instance of the meta-class `DogClass`.

.. note::

    `Singleton` means that there's only one instance in the
    whole program. For classes, in C-based ooc compilers,
    they're usually accessed with package_ClassName_class(), e.g.
    Dog_class() for that example.
    
Introspection
-------------

Every object has a `class` field::

    "Our object is a %s of size %d" format(dog class name, dog class instanceSize) println()

Since dog is an instance of Dog, we have::

    dog class == Dog
    
What if our Dog class inherited of Animal? Let's see::

    Animal: class {}
    Dog: class extends Animal {}
    
Comparing classes directly only works if it's the exact class::
    
    dog class == Dog // true
    dog class == Animal // false
    
Class inheritsFrom() checks inheritance, though::
    
    dog class inheritsFrom(Dog) // true
    dog class inheritsFrom(Animal) // true
    
Object instanceOf() is even shorter::
   
    dog instanceOf(Dog) // true
    dog instanceOf(Animal) // true
    dog instanceOf(Object) // always true ;)
    
Under the hood
--------------

Variables
~~~~~~~~~

Static fields belong in the meta-class, and instance fields belong
in the class, for example::

    Dog: class {
    
        totalDogs: static Int
        name: String
    
    }

`name` will be stored in the Dog class, and `totalDogs` in the meta-class

That makes a lot of sense, because we can access these fields like this::

    dog name // a field of the class
    Dog totalDogs // a field of the meta-class

Methods
~~~~~~~

All methods belong in the meta-class

Let's say we have::

    Cat: class {
    
        growl: func { "Rrrrr, my address is %d" format(this) println() }
        createCat: func -> This { new() }
    
    }

.. note::
    
    Don't confuse those two: `this` is a reference to the object instance
    we're calling the method on, whereas `This` is the type we're
    currently defining.
     
    Here, we could have just as well wrote `Cat` instead of `This`,
    but it's a good way to `avoid repetition <http://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

Then both `growl` and `createCat` belong to CatClass

The difference is that growl has a `this`, and createCat doesn't.

What really happens, when we do::

    cat := Cat createCat()
    cat growl()

is::

    cat := Cat createCat() // alright
    Cat growl(cat) // the first argument is 'this'

So yeah, doing 'Cat growl' essentially gives you the adress of the growl
function in the Cat class.




