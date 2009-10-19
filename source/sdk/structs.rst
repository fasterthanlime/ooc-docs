structs/
========

Array
-----

The :mod:`sdk/structs/Array` module contains a simple, non-resizeable, generic list
class which takes care of you::

    import sdk/structs/Array
    // get an Array object with 10 elements
    array := Array new<String>(10)
    // set the first element
    array set(0, "First")
    // set the last element
    array set(array lastIndex(), "Last")
    // try to set an element outside the array range
    array set(11, "eeeevil!")
    // -> Exception.
    // you can even pass the contents to a C function!
    doSomethingWithMyArray: func (array: Char**, size: SizeT)
    doSomethingWithMYArray(array data, array size())
    // it's iterable!
    for(element: String in array) {
	element println()
    }

ArrayList
---------

In the :mod:`sdk/structs/ArrayList` module, we have a resizeable generic list class which
implements the :class:`List<T>` interface::

    import sdk/structs/ArrayList
    // we can pass an initial capacity here. No worries, it's a growing buffer, but if you
    // already know that you'll add maaaany elements (100?), you can speed up your application
    // by passing the capacity to the constructor. But it's no problem to leave it out.
    list := ArrayList<Int> new(100)
    // ffffill it!
    for(i: Int in 0..100) {
	list add(i)
    }
    // oh! Let's get element #42!
    fortytwo := list get(42)
    // yay! Let's get element #1337!
    leet := list get(1337)
    // oh. We only have 100 elements. -> Exception!
    // i don't like the number 63. Let's remove it.
    // `remove` tries to remove the first occurence of `63` and returns
    // `true` if it was successful.
    list remove(63)
    // I want to remove the element at index 4.
    list removeAt(4)
    // we've also got tasty operator overloading!
    fortytwo := list[42]
    list[42] = 36461
    // adds a new element (shortcut for `add`)
    list += 100
    // removes a single instance of a value (shortcut for `remove`)
    list -= 32
    
