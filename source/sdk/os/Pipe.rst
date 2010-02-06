os/Pipe
=======

.. module:: os/Pipe

.. class:: Pipe
    
    .. staticmemberfunction:: new -> Pipe
        
    .. memberfunction:: read (len: Int) -> Pointer
        
        read 'len' bytes at most from the pipe 
        
    .. memberfunction:: write~string (str: String) -> Int
        
        write a string to the pipe 
        
    .. memberfunction:: write (data: Pointer, len: Int) -> Int
        
        write 'len' bytes of 'data' to the pipe 
        
    .. memberfunction:: close (mode: Char) -> Int
        
        close the pipe, either in reading or writing 
        @param arg 'r' = close in reading, 'w' = close in writing
        
        
