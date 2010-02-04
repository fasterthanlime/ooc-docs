os/mmap
=======

.. module:: os/mmap

.. function:: mmap (Pointer, SizeT, Int, Int, Int, Int) -> Pointer
    
.. function:: munmap (Pointer, SizeT) -> Int
    
.. function:: mprotect (Pointer, SizeT, Int) -> Int
    
.. function:: madvise (Pointer, SizeT, Int) -> Int
    
.. function:: mincore (Pointer, SizeT, Char*) -> Int
    
.. function:: minherit (Pointer, SizeT, Int) -> Int
    
.. function:: msync (Pointer, SizeT, Int) -> Int
    
.. function:: mlock (Pointer, SizeT) -> Int
    
.. function:: munlock (Pointer, SizeT) -> Int
    
.. data:: PROT_EXEC

.. data:: PROT_WRITE

.. data:: PROT_READ

.. data:: PROT_NONE

.. data:: MAP_FIXED

.. data:: MAP_SHARED

.. data:: MAP_PRIVATE

.. data:: MAP_DENYWRITE

.. data:: MAP_EXECUTABLE

.. data:: MAP_NORESERVE

.. data:: MAP_LOCKED

.. data:: MAP_GROWSDOWN

.. data:: MAP_ANONYMOUS

.. data:: MAP_ANON

.. data:: MAP_FILE

.. data:: MAP_32BIT

.. data:: MAP_POPULATE

.. data:: MAP_NONBLOCK

.. data:: MAP_FAILED

.. data:: MADV_NORMAL

.. data:: MADV_SEQUENTIAL

.. data:: MADV_RANDOM

.. data:: MADV_WILLNEED

.. data:: MADV_DONTNEED

.. data:: MS_ASYNC

.. data:: MS_SYNC

.. data:: MS_INVALIDATE

