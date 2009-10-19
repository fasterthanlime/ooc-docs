Version blocks
==============

Version blocks are a cleaner alternative to #ifdef in C.

They allow you to write platform-specific code. It's almost
always a bad thing to have to maintain several separate codebases,
each for one platform. Version blocks allows you to have the code
for all platforms in one case.

Syntax
------

version-block ::= "version" "(" <version-expr> ")" "{" <block> "}"
version-expr ::= <version-name>
version-expr ::= "(" <version-expr> ")"
version-expr ::= "!" <version-expr>
version-expr ::= <version-expr> && <version-expr>
version-expr ::= <version-expr> || <version-expr>

Examples
--------

Here are some examples of combinations of version-expr::

    version(linux) {
        println("Got Linux\n")
    }
    version(!linux && unix) {
        println("Got another unix")
    }
    version(!linux && (unix || windows)) {
        println()
    }

Builtin version-names
---------------------

windows -> __WIN32
linux   -> __linux__
unix    -> __unix__    
beos    -> __BEOS__
haiku   -> __HAIKU__
apple   -> __APPLE_
gnuc    -> __GNUC__
i386    -> __i386__
x86     -> __X86__
x86_64  -> __X86_64_
64      -> __X86_64_

If you use another name, it will write is as-is in the #ifdef,
which means you can add your own typedefs if you want.
(E.g. pass them with +-DYOURTYPEDEF=1 if you're using gcc)

Imports
-------

There will be support for imports in version blocks soon.
Meanwhile, your best bet is to have an abstract class that contains
the interface you want to expose, and to subclass it for each platform.

Then use the Factory pattern and return the right subclass depending
on the platform.




