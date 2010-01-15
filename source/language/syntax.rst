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

things to keep in mind: \* ooc translates directly to C. This
explains some corners of the syntax

keywords
~~~~~~~~

class, cover, interface, implement, func, abstract, extends, from,
this, super, new, const, final, static, include, import, use,
extern, inline, proto, break, continue, fallthrough, operator, if,
else, for, while, do, switch, case, as, in, version, return, true,
false, null, default

(note: things like 'new', and 'this' aren't really keywords, they
are proper functions and variables, but it's still useful they
stand out in syntax highlighting, for readability. Also a few other
keywords aren't implemented yet, but reserved.)

operators
~~~~~~~~~

+, -, \*, /, +=, -=,\*=, /=, =, :=, ==, !=, !, %, ?, >, <, >=, <=,
&&, \|\|, &, \|, ^, ., ~, .., >>, <<, >>>, <<<, >>=, <<=, >>>=,
<<<=

(note, '.' is the chaining operator in ooc, not the 'member access'
one. To access a member of an object, just whitespace is needed as
in Io, e.g. "dog name", or "dog barf()")

literals
~~~~~~~~

-  string: "hi world"
-  char: 'c', '\\0' (same escape sequences as C)
-  decimal: 234
-  hexa: 0xdeadbeef
-  octal: 0c777
-  binary: 0b1011
-  float: 3.14, 0.
-  array literal: [1, 2, 3]
-  range literal: 0..10


builtin-types
~~~~~~~~~~~~~

-  Int, Int8, Int16, Int32, Int64, Int80, Int128
-  UInt, UInt8, UInt16, UInt32, UInt64, UInt80, UInt128
-  Octet, Short, UShort, Long, ULong, LLong, ULLong
-  Float, Double, LDouble, Float32, Float64, Float128
-  Char, UChar, WChar, String
-  Void, Pointer, Bool, SizeT, This

(Note about 'This': it refers to the current type being defined,
e.g. a clone method would be defined like clone: func -> This { /\*
return a copy \*/ })

(Note 2: some types above are redundant, some will be deprecated
soon, but coloring all of them can't harm.)


statements
~~~~~~~~~~

include, import, use
^^^^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    include header1, path/header2
    include ./mylocalheader
    import my/package/MyModule
    import my/package/[MyModule1, MyModule2]
    use mylib, mylib2

No backslashes, even on windows.

comments
^^^^^^^^

.. code-block:: ooc

    // single-line comment
    /* multi-line comment */
    /** oocdoc comment (a-la javadoc/doxygen), with @tags */

function call
^^^^^^^^^^^^^

.. code-block:: ooc

    myFunction()
    myFunction(arg1, arg2)
    myObject doThing()
    MyClass callStaticMethod()

declarations
^^^^^^^^^^^^

.. code-block:: ooc

    i: Int // variable declaration
    i = 3 : Int // variable declaration + assignment
    i := 3 // variable declassignment. (the type is guessed)
    a, b, c: Int // declare three variables
    // useful for bitfields:
    OPTION1 = 1, OPTION2 = 2, OPTION3 = 4, OPTION4 = 8 : const Int

casting
^^^^^^^

.. code-block:: ooc

    3.14 as Int // casting

function declaration
^^^^^^^^^^^^^^^^^^^^

Function definitions can have an argument list, a return value, a
suffix (used for overloading), and a number of special keywords. Any
combination of these can be included or left out.

.. code-block:: ooc

    // two Int arguments, return is Int
    add: func (a: Int, b: Int) -> Int {
        return a + b
    }
    
    // both a and b are Int, and the return keyword is optional.
    add: func (a, b: Int) -> Int { a + b }

    // function with no return
    println: func (s: String) { print(s + "\n") }

    // no argument list = takes no argument
    // no '->' = void func (no return)
    doStuff: func {
        doFirstThing()
        doSecondThing()
    }

For function overloading [#overload]_, you must specify a suffix. This will be used
for the C function name and can also be used to call a specific
version of an overloaded function. It is specified like so:

.. [#overload] Do not confuse overloading with overriding. Overloading simply
      allows you to create several functions with the same name that recieve
      or return different types of arguments.

.. code-block:: ooc

     print: func ~withString (s: String) { puts(s) }
     print: func ~withChar (c: Char) { putc(c) }

     print("Hello, ooc!") // calls print~withString()
     print('\n') // calls print~withChar()

     // calling a specific version
     print~withChar('a')

Note: You can leave the suffix off of one of the functions, but only
one of them.

You can also use these other keywords, before the 'func' keyword:

proto
  Adds function prototypes in the generated C file (e.g. when you're
  missing a header)
inline
  Just like C inline (Hint to the compiler to make calling this
  function faster, usually by substituting calls to this function
  with the actual code of the function. It's generally used for
  functions that will be called very often)
extern
  Means it is defined elsewhere, e.g. in some C code. By default it
  uses the name of the ooc function being defined but you can also
  use it with an argument to wrap a C function with a different
  name.

.. code-block:: ooc

    // wraps C 'exit'
    exit: extern func (status: Int)
    
    // wraps C 'puts', but will be called in ooc as putString(s)
    putString: extern(puts) func (str: String) -> Int

    // exactly the same as above. naming extern arguments is optional
    putString: extern(puts) func (String) -> Int

classes
^^^^^^^

.. code-block:: ooc

    Animal: class {
      name: String
      age := 0
    
      /** Simple constructor with a member-assign-argument */
      init: func (=name) {}
      // equivalent to
      // init: func (name: String) { this name = name }
    
      /** Another constructor, we need to choose a suffix, here 'withAge' */
      init: func ~withAge (.name, =age) {
        this(name) // call another constructor
      }
      // equivalent to
      // init: func (name: String, age: Int) { this(name); this age = age }
    
      /** An abstract function, should be implemented by child classes */
      shout: abstract func
      // note: if we have no arguments, we don't need parenthesis
      // (heh, that's what the 'func' keyword is for!)
    }
    
    Dog: class extends Animal {
    
      shout: func {
        "Woof, woof!" println()
      }
    
    }

static fields in classes
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    Ant: class {
      total = 0 : static Int
      init: func { total += 1 }
      getTotal: static func -> Int { total }
    }
    
    main: func {
      list := ArrayList<Ant>
      for(i in 0..20) {
        list add(Ant new())
      }
      printf("Created %d ants in total!\n", Ant getTotal())
    }

covers
^^^^^^

.. code-block:: ooc

    // this translates to a simple typedef
    Int: cover from int
    
    // typedef here..
    String: cover from Char* {
    
      // and define the String_println(String this) function here. (in C)
      println: func {
        printf("%s\n", this)
      }
    
    }
    
    Button: cover from GtkButton extends Window {
    
      // inheritance works almost the same as with classes, e.g.
      // you can call methods from its super-cover
    
    }
    
    // Compound cover =)
    Color4f : cover {
      r, g, b, a: Float
    }

interfaces (note: not implemented yet)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    Message: class {
      content: String
    }
    
    Printable: interface {
      print: func
    }
    
    implement Printable for Message {
      print: func {
        content println()
      }
    }

operator overloading
^^^^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    operator + (left, right: String) -> String {
      // note: this is a horrible implementation, but it's just for the example
      return strcat(strdup(left), right)
    }

pointer syntax
^^^^^^^^^^^^^^

.. code-block:: ooc

    main: func {
      ptr := gc_malloc(Int size) as Int*
      ptr@ = 42
      printf("ptr's value is %d\n", ptr@)
      add(ptr, 3)
      printf("ptr's value is now %d\n", ptr@)
    }
    
    add: func(ptr: Int*, value: Int) {
      ptr@ += value
    }

reference syntax
^^^^^^^^^^^^^^^^

.. code-block:: ooc

    main: func {
      ptr := gc_malloc(Int size) as Int* // alloc an int on the heap
      ptr@ = 42
      printf("ptr's value is %d\n", ptr@)
      add(ptr, 3)
      printf("ptr's value is now %d\n", ptr@)
    }
    
    add: func(ptr: Int@, value: Int) {
      ptr += value
    }

more fun with pointers & references
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    main: func {
      number := 42 // alloc an int on the stack
      printf("number is %d\n", number)
      add(number&, 3)
      printf("number is now %d\n", number)
    }
    
    add: func(ptr: Int@, value: Int) {
      ptr += value
    }

foreach
^^^^^^^

.. code-block:: ooc

    for(i in 0..10) {
      printf("%d, ", i)
    }

also, for collections

.. code-block:: ooc

    list := ArrayList<Int> new() .add(1) .add(2) .add(3)
    for(i in list) {
      printf("%d, ", i)
    }

Can also be a decl before the 'in', e.g.

.. code-block:: ooc

    for(i: UInt in 0..10) {
      printf("%d, ", i)
    }

function pointers
^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    action: Func // a dumb function pointer
    
    doThing: func {
      "Oh, really?" println()
    }
    
    action = doThing
    
    action() // call action, thus call doThing

typed function pointers
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    applyOperator: func(operator: Func (Int, Int) -> Int, left, right: Int) {
      return operator(left, right)
    }
    
    add: func (left, right: Int) { left + right }
    sub: func (left, right: Int) { left - right }
    mul: func (left, right: Int) { left * right }
    div: func (left, right: Int) { left / right }
    
    printf("1 + 2 = %d\n", applyOperator(add, 1, 2))
    printf("10 - 5 = %d\n", applyOperator(sub, 10, 5))
    printf("6 * 7 = %d\n", applyOperator(mul, 6, 7))
    printf("10 / 2 = %d\n", applyOperator(div, 10, 2))

chain calls
^^^^^^^^^^^

.. code-block:: ooc

    list := ArrayList<Int> new()
    list add(1) .add(2) .add(3)

closures
^^^^^^^^

.. code-block:: ooc

    butt := Button new()
    butt connect("clicked", func { "Button clicked!" println() })

generic functions
^^^^^^^^^^^^^^^^^

The following code:

.. code-block:: ooc

    printType: func <T> (param: T) {
      printf("Got param of type %s and size %d\n", T name, T size)
      if(T == Int) printf("It's an Int! and its value is %d\n", param as Int)
      else if(T == Char) printf("It's a char! and its value is '%c'\n", param as Char)
    }
    
    printType('c')
    printType(42)

prints:

.. code-block:: ooc

    Got param of type Char and size 1
    It's a char! and its value is 'c'
    Got param of type Int and size 4
    It's an Int! and its value is 42
   
The following code:

.. code-block:: ooc    
    
    Container: class <T> {
      content: T
      init: func(=content)
      get: func -> T { content }
      set: func(=content)
    }
    
    main: func {
    
      cont1 := Container<Int> new(42)
      number := cont1 get()
      printf("number is an %s, and its value is %d\n", number class name, number)
    
      cont2 := Container<String> new("Hi, world!")
      message := cont2 get()
      printf("message is a %s, and its value is %s\n", message class name, message)
    
    }

prints:

.. code-block:: ooc

    number is an Int, and its value is 42
    message is a String, and its value is Hi, world!

the match statement
^^^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    mark := stdin readLine() toInt()
    match mark {
      case 0 => println("Oh, that's bad.")
      case 1 =>
        // there can be several statements
        mark = 3
        println("There, I helped you a little")
      case 2 => 
        println("So you like middles?")
      case => // default case
        println("Now what is that value?")
    }

Note: there is a 'fallthrough' reserved keyword, which isn't
implemented yet.

match can be used as an expression:

.. code-block:: ooc

    hello := match 42 { case 42 => "Hello!" }

match without an expression is the equivalent of match true {}

.. code-block:: ooc

    isPositive: func (i: Int) -> Int {
      return match {
        case (i > 0) => 1
        case (i < 0) => -1
        case => 0
      }
    }

(parenthesis added for readability, but not actually needed)

a few other things in no particular order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

qualifiers for decl-assigns
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    Math: class {
      PI := const static 3.14159
    }

unusual qualifiers
^^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    Container: class {
      content: Pointer
      /** inline keyword: same meaning as C */
      getContent: inline func -> Pointer { content }
    }
    
    /** proto keyword adds function prototypes int the generated C file, e.g. when you're missing a header. */
    usleep: extern proto func -> Int

extern symbols aliasing
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: ooc

    c_exit extern(exit) func
    
    main: func {
      c_exit(); // translates to exit() in C
    }

for member functions (ie. methods)

.. code-block:: ooc

    include stdlib
    
    String: cover from char* {
      length: extern(strlen) func -> Int
    }
    
    "blah" length() toString() println()

prints '4'

raw arrays
^^^^^^^^^^

.. code-block:: ooc

    arr := [1, 2, 3] // array of ints, typed Int*
    
    // the type is determined by the first element
    arr2 := [1 as UInt, 2, 3] // typed UInt*
    
    // this is invalid:
    Dog: class {}
    arr3 := [1, 2, 3, Dog new()] // error, incompatible type



