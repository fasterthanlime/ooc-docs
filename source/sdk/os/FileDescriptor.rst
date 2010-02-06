os/FileDescriptor
=================

.. module:: os/FileDescriptor

.. function:: open (String, Int) -> Int
    
.. function:: write (FileDescriptor, Pointer, Int) -> Int
    
.. function:: read (FileDescriptor, Pointer, Int) -> Int
    
.. function:: close (FileDescriptor) -> Int
    
.. cover:: FileDescriptor
    
    .. memberfunction:: write (data: Pointer, len: Int) -> Int
        
    .. memberfunction:: write~string (str: String) -> Int
        
    .. memberfunction:: read~toBuf (buf: Pointer, len: Int) -> Int
        
    .. memberfunction:: read~evilAlloc (len: Int) -> Pointer
        
    .. memberfunction:: close -> Int
        
    .. memberfunction:: _errMsg (var: Int, funcName: String)
        
.. data:: STDIN_FILENO -> FileDescriptor

.. data:: STDOUT_FILENO -> FileDescriptor

.. data:: STDERR_FILENO -> FileDescriptor

