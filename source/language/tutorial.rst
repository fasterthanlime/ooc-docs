Tutorial
========

Preface
-------

Welcome to the ooc tutorial. It's still under construction, so if you have any suggestions or additions, please let us know.

In order to work with this tutorial, you need to have a working ooc installation. Installation of ooc will not be discussed here.

We want to keep this tutorial as simple as possible to make it as simple as possible for you to learn the ooc basics. However, basic programming skills in other imperative languages are a good thing. If you don't understand something, let us know.

KALAMAZOO
---------

Let's start with the obligatory "Hello World" program, but for additional awesomeness, we won't just print a boring greet, we will print KALAMAZOO.

In Python, this would be::

    print 'KALAMAZOO'

In ooc, we have::

    "KALAMAZOO" println()

Huh! This looks strange. What does this ``println`` do right **after** the string? This doesn't make any sense.

Well, in fact it does.

ooc is a little bit different. 

First: ooc doesn't have a print statement like Python. In ooc, the ``String`` class (which is the type of the ``"KALAMAZOO"`` literal) has a method (other languages might call this "method") called ``println`` that takes no arguments and will just print the string.

Second: There Is No Dot In ooc. To call a method of an object, just add a space and write the method name, followed by arguments. Yeah, this feels strange at first. But you'll get used to it. Just look at this::

    "%s --- %s" format("ABC", "DEF") toUpper() println()

It might look strange for your dot-affine eyes at first. But take another look. This line almost reads like natural language and there is no useless dot-noise.
It's just beautiful.

Enough chit-chat, let's run the program. As expected, this prints a beatiful, awesome and stylish KALAMAZOO.

More methods!
----------------------

Let's improve this. My code looks so aggressive if it contains KALAMAZOO in upper case. I get headache every time I look at it. I really want to change this.

No problem. We'll just write ``"kalamazoo"`` and make this uppercase at runtime. Isn't this a nice idea?

For peace's sake::

    "kalamazoo" toUpper() println()

I suppose you already got the concept here. ``"kalamazoo"``'s method ``toUpper`` gets called, and ``println`` gets called on the resulting string (our uppercased "kalamazoo").

Yay.

Variables
---------

Hoh. I have an idea how to write an ever more awesome program. I'll print KALAMAZOO not once, not twice - but three times! For additional coolness, we'll store it in a variable.

But how will be do it?

As in C, we have to declare a variable before we can use it. But that's easy. Normal variable declarations have this format::

    name: Type

Of course, this can get more sophisticated. You can easily declare multiple variables of the same type::

    name1, name2, name3: Type

Or specify an initial value (this won't work with multiple variables, though)::

    name: Type = Value

It gets much cooler with the ``decl-on-assign`` operator::

    name := Value

If you write this, the ooc compiler will guess the type of the variable based on the information about ``Value``. This will work just as expected in many, many cases. In some tricky cases, you might have to specify the type of the variable manually using a cast. Later you'll get to know more about this.

So, let's use this operator in our great KALAMAZOO application::

    message := "kalamazoo" toUpper()
    message println()
    message println()
    message println()

``message`` stores ``"KALAMAZOO"``, then, which gets printed three fucking times as proposed above. ``message``'s type (``String``) is guessed by the compiler.

Ouch, but these three println lines look not so awesome. Can't we do this shorter?

Yes, we can.

For-Loops
---------

We'll use a loop. There are various kinds of loops, but we'll use the for-loop for now. It iterates over an iterable object (later.) and assigns each value to a specified variable, then executes an inner block.

Luckily, there is a short form for simple numeric ranges. We want to print it three times, and for EVEN MORE AWESOMENESS, we'll print the iteration counter each time. That's easy with a for loop::

    message := "kalamazoo" toUpper()
    for(i in 1..4) {
	i toString() println()
	message println()
    }

Ouh, that's much. Let's get this line-by-line. The first line should be clear.
The second line indicates the start of a for loop. All for loops have this syntax::

    for(variable in iterable) {
	...
    }

Our ``iterable`` is created via the range syntax::

    start..end

``start`` is the first value that will get returned. ``end`` is the exclusive end marker: The last value isn't ``end``, but actually ``end-1``. It's important to know that.

The third line introduces a new method:: ``toString`` called on numeric values will return the value of the number, but converted to a string.

The fourth line is easy again.

Let's run this. It will print::

    1
    KALAMAZOO
    2
    KALAMAZOO
    3
    KALAMAZOO

