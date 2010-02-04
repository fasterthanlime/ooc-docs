lang/memory
===========

.. module:: lang/memory

.. function:: gc_malloc (size: SizeT) -> Pointer
    

.. function:: gc_malloc_atomic (size: SizeT) -> Pointer
    

.. function:: gc_realloc (ptr: Pointer, size: SizeT) -> Pointer
    

.. function:: gc_calloc (nmemb, size: SizeT) -> Pointer
    

.. function:: gc_register_finalizer (obj: Pointer, callback: GC_finalization_proc, userdata, oldObj, oldCallback: Pointer)
    

.. function:: gc_invoke_finalizers
    

.. function:: sizeof (...) -> SizeT
    

.. function:: memset (Pointer, Int, SizeT) -> Pointer
    

.. function:: memcmp (Pointer, Pointer, SizeT) -> Int
    

.. function:: memmove (Pointer, Pointer, SizeT)
    

.. function:: memcpy (Pointer, Pointer, SizeT)
    

.. function:: free (Pointer)
    

.. cover:: GC_finalization_proc
    

