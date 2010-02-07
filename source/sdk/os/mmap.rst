os/mmap
=======

.. module:: os/mmap

.. function:: mmap (:cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`, :cover:`~lang/types Int`, :cover:`~lang/types Int`, :cover:`~lang/types Int`, :cover:`~lang/types Int`) -> :cover:`~lang/types Pointer`
    
.. function:: munmap (:cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`) -> :cover:`~lang/types Int`
    
.. function:: mprotect (:cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`, :cover:`~lang/types Int`) -> :cover:`~lang/types Int`
    
.. function:: madvise (:cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`, :cover:`~lang/types Int`) -> :cover:`~lang/types Int`
    
.. function:: mincore (:cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`, :cover:`~lang/types Char`*) -> :cover:`~lang/types Int`
    
.. function:: minherit (:cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`, :cover:`~lang/types Int`) -> :cover:`~lang/types Int`
    
.. function:: msync (:cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`, :cover:`~lang/types Int`) -> :cover:`~lang/types Int`
    
.. function:: mlock (:cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`) -> :cover:`~lang/types Int`
    
.. function:: munlock (:cover:`~lang/types Pointer`, :cover:`~lang/types SizeT`) -> :cover:`~lang/types Int`
    
.. var:: PROT_EXEC -> :cover:`~lang/types Int`

.. var:: PROT_WRITE -> :cover:`~lang/types Int`

.. var:: PROT_READ -> :cover:`~lang/types Int`

.. var:: PROT_NONE -> :cover:`~lang/types Int`

.. var:: MAP_FIXED -> :cover:`~lang/types Int`

.. var:: MAP_SHARED -> :cover:`~lang/types Int`

.. var:: MAP_PRIVATE -> :cover:`~lang/types Int`

.. var:: MAP_DENYWRITE -> :cover:`~lang/types Int`

.. var:: MAP_EXECUTABLE -> :cover:`~lang/types Int`

.. var:: MAP_NORESERVE -> :cover:`~lang/types Int`

.. var:: MAP_LOCKED -> :cover:`~lang/types Int`

.. var:: MAP_GROWSDOWN -> :cover:`~lang/types Int`

.. var:: MAP_ANONYMOUS -> :cover:`~lang/types Int`

.. var:: MAP_ANON -> :cover:`~lang/types Int`

.. var:: MAP_FILE -> :cover:`~lang/types Int`

.. var:: MAP_32BIT -> :cover:`~lang/types Int`

.. var:: MAP_POPULATE -> :cover:`~lang/types Int`

.. var:: MAP_NONBLOCK -> :cover:`~lang/types Int`

.. var:: MAP_FAILED -> :cover:`~lang/types Pointer`

.. var:: MADV_NORMAL -> :cover:`~lang/types Int`

.. var:: MADV_SEQUENTIAL -> :cover:`~lang/types Int`

.. var:: MADV_RANDOM -> :cover:`~lang/types Int`

.. var:: MADV_WILLNEED -> :cover:`~lang/types Int`

.. var:: MADV_DONTNEED -> :cover:`~lang/types Int`

.. var:: MS_ASYNC -> :cover:`~lang/types Int`

.. var:: MS_SYNC -> :cover:`~lang/types Int`

.. var:: MS_INVALIDATE -> :cover:`~lang/types Int`

