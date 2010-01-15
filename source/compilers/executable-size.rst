Reducing the executable size
============================

A basic hello world can easily compile to a 120KB file, with the default
sdk and options.

While it's no problem for desktop use, if you have more drastic requirements,
you'll probably want to cut that down. Here's how.

Stripping
---------

The first thing to try when you want to reduce the size of an executable is::

    strip yourprogram

It got it down to 89KB for me. Not exactly a miracle, but nice to know.

.. note::

    What does strip do? It "discards symbols (ie. function names) from object files"
    Of course, you don't want to that on your debug builds ;)

Linking dynamically with the GC
-------------------------------

Most of the remaining fat is a constant cost when you link statically to the GC. By default, it's 
linked statically to ease distribution of ooc executables.

The `-v` compiler option prints the commands ooc executes. By default, it links with libgc.a

.. note::

    A ".a" file is a static version of a library.
    Dynamic libraries usually have the ".so" extension on most *nix,
    .dll on Win32, and .dylib on Apple

If you have installed the Boehm GC properly you can try the "-dyngc" switch. Down to 31KB for me =) Better.

Stripping brings it down to 19KB which begins to become acceptable.

Disabling the GC
----------------

But wait, there's more! The default sdk is adapted to a desktop use, and
thus includes many convenient but costly (depending on your requirements) things

.. note::

    Did you know? Every .ooc file in sdk/lang/ is imported by default.
    
You can completely disable the GC, that's a tricky subject, thus it's
discussed on :doc:`another page <no-gc>`.

Using a custom SDK
------------------
    
You can use a custom SDK by defining the OOC_SDK environment variable before compilation.
e.g::

    OOC_SDK="my-custom-sdk/" ooc hello-embedded-world.ooc
    
For an example of custom sdk, see `ooc-ti project on GitHub <http://github.com/nddrylliog/ooc-ti>`_

The first thing you probably want to do at this point is alias gc_[malloc, realloc, free]
to the regular malloc, realloc, free. Be warned though, if you use the rest of the SDK as
is, it will just leak like MediaDefender's internal e-mails.

.. note::

    It's planned to make the SDK modular, e.g. either depending on the GC or not (with version blocks)
    If you're interested come on IRC, so we can discuss it all together =)

How much can you cut from the SDK
---------------------------------

ooclib.ooc is pretty much essential, e.g. it provides all the type aliases such as int->Int, etc.
Object.ooc is difficult to do without too, as it's used in Type_class() functions which are generated
for each cover, etc.

Iterable/Iterator are necessary when you want to use for (element in list) where list is an object.
for (i in 0..10) is alright though - it doesn't even instanciate a Range

All the rest you can cut down pretty easily =)

End result
----------

With all the tricks defined above and a minimal SDK (with just what you need to make both compilers happy),
we can reach a size of 8,2KB unstripped, 5,8KB stripped. It's only slightly worse than
a C executable (6,8KB unstripped, 5,6KB stripped)

I hope all that shows you that the language is, in fact, pretty modular, and that you can tailor it
easily to your particular use, e.g. add/remove bloat at will =)





