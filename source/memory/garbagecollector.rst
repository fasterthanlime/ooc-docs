The Garbage Collector
=====================

The Garbage Collector (GC) currently used in ooc is 
the `Boehm GC <http://www.hpl.hp.com/personal/Hans_Boehm/gc/>`_

It's a conservative GC, which basically means it plays well 
with languages like C and C++, where you don't have precise type information.

The Boehm GC has been developed for years and is very stable and
well-tested, thus we're not afraid to use it.

It is somewhat an easy solution for now though. It's not entirely
impossible that the Boehm GC would be replaced by another one,
and it would be quite awesome if it was written in ooc itself.

*How should I allocate memory?*

Just use gc_malloc, gc_realloc, gc_calloc instead of the regular ones,
and don't worry about free.

Example::

    // allocate a raw array of 100 Int32, because I can.
    arr = gc_malloc(Int32 size * 100) : Int32*
    
    // or
    arr2 = gc_calloc(Int 32 size, 100) : Int32*
    
You can still use good old malloc/free and do things by hand.

You might also want to `completely disable the GC <no-gc>`_ in certain cases.

*Are there cases where memory is not freed?*

Not that we're aware of

*Are there cases where memory is freed even though it's still used?*

Some rare cases, yeah. If the address of an allocated object is not
reachable for the GC, it may be collected even though still used
elsewhere.

Be particularly careful for example if you pass a GC-allocated object
to a C library and keep no reference to it. The object will become
unreachable, and will be collected.

An example of that is if you pass an ooc gc-allocated object as a
gpointer *data to a Gtk+ callback. As a workaround, either keep a
reference to it somewhere reachable (e.g. in your ooc code) or allocate
it manually.


