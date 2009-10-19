Reducing the executable size produced by ooc
============================================

It comes as a surprise for beginners, that a naive hello world, compiled with all the defaults,
takes usually ~120KB. This is obviously a lot too much to be used in most embedded environments.

Stripping
---------

The first thing to try when you want to reduce the size of an executable is strip.
Try "strip yourprogram". It got it down to 89KB for me. Not exactly a miracle, but nice to know.

Linking dynamically with the GC
-------------------------------

90% of the remaining fat is a constant cost when you link statically to the GC. By default, it's 
linked statically to help distributing ooc executables everywhere. If you need proof, compile
with -v and see that it's the libgc.a

If you have installed the Boehm GC properly and have a libgc.so somewhere (e.g. in /usr/lib or
 /usr/local/lib for *nix), you can try the "-dyngc" switch. Down to 31KB for me =) Better.

Stripping brings it down to 19KB which begins to become acceptable.

Disabling the GC
----------------

Fortunately it doesn't end here! The currently distributed SDK is adapted to a desktop use, and
thus includes many things by default.

.. note::

    Every .ooc file in sdk/lang/ is imported by default.

Using a custom SDK
------------------
    
You can use a custom SDK by defining the OOC_SDK environment variable before compilation.
e.g::

    OOC_SDK="my-custom-sdk/" ooc hello-embedded-world.ooc
    
For an example of custom sdk, see the ooc-ti project on GitHub.

The first thing you probably want to do at this point is alias gc_[malloc, realloc, free]
to the regular malloc, realloc, free. Be warned though, if you use the rest of the SDK as
is, it will just leak like MediaDefender's internal e-mails.

..note ::

    It's planned to make the SDK modular, e.g. either depending on the GC or not (with version blocks)
    If you're interested come on IRC, so we can discuss it all together =)

How much can you cut from the SDK?

ooclib.ooc is pretty much essential, e.g. it provides all the type aliases such as int->Int, etc.
Object.ooc is difficult to do without too, as it's used in Type_class() functions which are generated
for each cover, etc.

Iterable/Iterator are necessary when you want to use for (element in list) where list is an object.
for (i in 0..10) is alright though - it doesn't even instanciate a Range

All the rest you can cut down pretty easily =)

Extremely slim ooc config
-------------------------

With all the tricks defined above and a minimal SDK (with just what you need to make both compilers happy),
we can reach a size of 8,2KB unstripped, 5,8KB stripped. It's only slightly worse than
a C executable (6,8KB unstripped, 5,6KB stripped)

I hope all that shows you that the language is, in fact, pretty modular, and that you can tailor it
easily to your particular use, e.g. add/remove bloat at will =)





