The Garbage Collector
=====================

The Garbage Collector (GC) currently used in ooc is 
the `Boehm GC <http://www.hpl.hp.com/personal/Hans_Boehm/gc/>`_

It's a `conservative GC <http://en.wikipedia.org/wiki/Garbage_collection_%28computer_science%29#Precise_vs._conservative_and_internal_pointers>`_,
which basically means it plays well with languages like C and C++, where you don't have precise type information.

The Boehm GC has been developed for years and is very stable and
well-tested, thus we're not afraid to use it.

It is somewhat an easy solution for now though. It's not entirely
impossible that the Boehm GC would be replaced by another one,
and it would be quite awesome if it was written in ooc itself.

Memory allocation
-----------------

Just use gc_malloc, gc_realloc, gc_calloc instead of the regular ones,
and don't worry about free.

Example::

    // allocate a raw array of 100 Int32, because I can.
    arr = gc_malloc(Int32 size * 100) : Int32*
    
    // or
    arr2 = gc_calloc(Int 32 size, 100) : Int32*
    
You can still use good old malloc/free and do things by hand.

You might also want to `completely disable the GC <no-gc.html>`_ in certain cases.

Finalizers (and destructors)
----------------------------

For an excellent explanation on the difference between destructors and finalizers,
read the `presentation from Hans-J. Boehm <http://www.hpl.hp.com/personal/Hans_Boehm/popl03/web/>`_

To define a finalizer for an object, just overload its __destroy__ method,

Example::

    PCRE: class {
        __destroy__: func {
            pcre_free(pcre) // avoid memory leaks
        }
    }

For performance reasons, if the __destroy__ method is empty, it won't be registered
as a finalizer to the Boehm GC, thus saving a lot of CPU cycles. According to the Boehm
GC documentation, a finalized object may be up to 5x slower to track, so this optimisation
is worthwile.

Short-term memory leaks
-----------------------

*Does the GC sometimes leak memory?*

According to the Boehm GC documentation, it *may* happen, although
it's quite unlikely, and they "avoid growing leaks", as they say.

For more information, please refer to the `Boehm GC FAQ <http://www.hpl.hp.com/personal/Hans_Boehm/gc/faq.html>`_

Memory freed too soon
---------------------

*Are there cases where memory is freed even though it's still used?*

Some rare cases, yeah. If the address of an allocated object is not
reachable for the GC, it may be collected even though still used
elsewhere.

Be particularly careful for example if you pass a GC-allocated object
to a C library and keep no reference to it. The object will become
unreachable, and will be collected.

An example of that is if you pass an ooc gc-allocated object as a
gpointer \*data to a Gtk+ callback. As a workaround, either keep a
reference to it somewhere reachable (e.g. in your ooc code) or allocate
it manually.


