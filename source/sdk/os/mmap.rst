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
    

.. globalVariable:: PROT_EXEC

.. globalVariable:: PROT_WRITE

.. globalVariable:: PROT_READ

.. globalVariable:: PROT_NONE

.. globalVariable:: MAP_FIXED

.. globalVariable:: MAP_SHARED

.. globalVariable:: MAP_PRIVATE

.. globalVariable:: MAP_DENYWRITE

.. globalVariable:: MAP_EXECUTABLE

.. globalVariable:: MAP_NORESERVE

.. globalVariable:: MAP_LOCKED

.. globalVariable:: MAP_GROWSDOWN

.. globalVariable:: MAP_ANONYMOUS

.. globalVariable:: MAP_ANON

.. globalVariable:: MAP_FILE

.. globalVariable:: MAP_32BIT

.. globalVariable:: MAP_POPULATE

.. globalVariable:: MAP_NONBLOCK

.. globalVariable:: MAP_FAILED

.. globalVariable:: MADV_NORMAL

.. globalVariable:: MADV_SEQUENTIAL

.. globalVariable:: MADV_RANDOM

.. globalVariable:: MADV_WILLNEED

.. globalVariable:: MADV_DONTNEED

.. globalVariable:: MS_ASYNC

.. globalVariable:: MS_SYNC

.. globalVariable:: MS_INVALIDATE

