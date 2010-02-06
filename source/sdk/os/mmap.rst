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
    
.. data:: PROT_EXEC -> Int

.. data:: PROT_WRITE -> Int

.. data:: PROT_READ -> Int

.. data:: PROT_NONE -> Int

.. data:: MAP_FIXED -> Int

.. data:: MAP_SHARED -> Int

.. data:: MAP_PRIVATE -> Int

.. data:: MAP_DENYWRITE -> Int

.. data:: MAP_EXECUTABLE -> Int

.. data:: MAP_NORESERVE -> Int

.. data:: MAP_LOCKED -> Int

.. data:: MAP_GROWSDOWN -> Int

.. data:: MAP_ANONYMOUS -> Int

.. data:: MAP_ANON -> Int

.. data:: MAP_FILE -> Int

.. data:: MAP_32BIT -> Int

.. data:: MAP_POPULATE -> Int

.. data:: MAP_NONBLOCK -> Int

.. data:: MAP_FAILED -> Pointer

.. data:: MADV_NORMAL -> Int

.. data:: MADV_SEQUENTIAL -> Int

.. data:: MADV_RANDOM -> Int

.. data:: MADV_WILLNEED -> Int

.. data:: MADV_DONTNEED -> Int

.. data:: MS_ASYNC -> Int

.. data:: MS_SYNC -> Int

.. data:: MS_INVALIDATE -> Int

