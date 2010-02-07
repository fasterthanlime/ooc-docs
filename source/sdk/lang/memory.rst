lang/memory
===========

.. module:: lang/memory

.. function:: gc_malloc (size: :cover:`~lang/types SizeT`) -> :cover:`~lang/types Pointer`
    
.. function:: gc_malloc_atomic (size: :cover:`~lang/types SizeT`) -> :cover:`~lang/types Pointer`
    
.. function:: gc_realloc (ptr: :cover:`~lang/types Pointer`, size: :cover:`~lang/types SizeT`) -> :cover:`~lang/types Pointer`
    
.. function:: gc_calloc (nmemb, size: :cover:`~lang/types SizeT`) -> :cover:`~lang/types Pointer`
    
.. function:: gc_register_finalizer (obj: :cover:`~lang/types Pointer`, callback: :cover:`~lang/memory GC_finalization_proc`, userdata, oldObj, oldCallback: :cover:`~lang/types Pointer`)
    
.. function:: gc_invoke_finalizers
    
.. function:: sizeof (...) -> :cover:`~lang/types SizeT`
    
.. function:: memset (:cover:`~lang/types Pointer`, :cover:`~lang/types Int`, :cover:`~lang/types SizeT`) -> :cover:`~lang/types Pointer`
    
.. function:: memcmp (:cover:`~lang/types Pointer`, :cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`) -> :cover:`~lang/types Int`
    
.. function:: memmove (:cover:`~lang/types Pointer`, :cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`)
    
.. function:: memcpy (:cover:`~lang/types Pointer`, :cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`)
    
.. function:: free (:cover:`~lang/types Pointer`)
    
.. cover:: GC_finalization_proc
    
