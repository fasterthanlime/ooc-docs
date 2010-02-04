os/Pipe
=======

.. module:: os/Pipe

.. function:: open (String, Int) -> Int
    

.. function:: write (Int, Pointer, Int) -> Int
    

.. function:: read (Int, Pointer, Int) -> Int
    

.. function:: close (Int) -> Int
    

.. class:: Pipe
    
    .. memberfunction:: new~withFDs (readFD, writeFD: FileDescriptor) -> Pipe
        
    
    .. memberfunction:: init~withFDs (readFD, writeFD: FileDescriptor)
        
    
    .. memberfunction:: new -> Pipe
        
    
    .. memberfunction:: init
        
    
    .. memberfunction:: read (len: Int) -> Pointer
        
    
    .. memberfunction:: write~string (str: String) -> Int
        
    
    .. memberfunction:: write (data: Pointer, len: Int) -> Int
        
    
    .. memberfunction:: close (arg: Char) -> Int
        
    
    .. field:: readFD
    
    .. field:: writeFD
    

