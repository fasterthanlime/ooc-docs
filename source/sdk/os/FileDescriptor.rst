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
        
    

.. globalVariable:: STDIN_FILENO

.. globalVariable:: STDOUT_FILENO

.. globalVariable:: STDERR_FILENO

