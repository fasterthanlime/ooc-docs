Disabling the Garbage Collector
===============================

In embedded environments, often you just can't afford a garbage collector.

.. note::

        Of course, if you use the current SDK without the GC, it will just leak through every hole
        That said, since there are many people interested in an SDK that doesn't rely on the
        GC, we'll do something about it. I'm thinking maybe version(!gc) {} blocks would be useful here.

Command line options
--------------------

*Step 1: use -gc=off to avoid linking with libgc*

If you want to compile without the gc, use the -nogc compiler flag, e.g.

.. ooc -nogc myfile.ooc

That way, it won't try to link with libgc.

.. note::

    Remember, to see what commands ooc launches, use the `-v` compiler option

Aliasing gc_malloc
------------------

*Step 2: change the definitions of gc_[malloc, realloc, free] in sdk/ooclib.ooc*

A good example of that is the `ooc-ti project <http://github.com/nddrylliog/ooc-ti>`_ (for running
 ooc applications on a TI89/92/v200 calculator), which uses a custom SDK with no GC.

Here's the part of the sdk/ooclib.ooc file with memory allocation related
definitions::

    gc_malloc: extern(malloc) func (size: SizeT) -> Pointer
    gc_malloc_atomic: extern(malloc) func (size: SizeT) -> Pointer
    gc_realloc: extern(realloc) func (ptr: Pointer, size: SizeT) -> Pointer
    gc_calloc: extern(calloc) func (nmemb: SizeT, size: SizeT) -> Pointer

As you can see, aliasing gc_malloc to malloc etc. is very easy and has
no runtime cost (e.g. occurences of gc_malloc are just replaced with malloc)

.. note::
    
    To use a custom sdk, specify its path by setting the OOC_SDK environment
    variable before launching ooc.

*Step 3: PROFIT!*

If you're disabling the GC just to manual memory management, you may want to
check out alternative malloc implementations, 
such as `TCMalloc <http://goog-perftools.sourceforge.net/doc/tcmalloc.html>`_
