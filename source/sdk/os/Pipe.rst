os/Pipe
=======

.. module:: os/Pipe

.. class:: Pipe
    
    .. staticmemberfunction:: new -> :class:`~os/Pipe Pipe`
        
    .. memberfunction:: read (len: :cover:`~lang/types Int`) -> :cover:`~lang/types Pointer`
        
        read 'len' bytes at most from the pipe 
        
    .. memberfunction:: write~string (str: :cover:`~lang/types String`) -> :cover:`~lang/types Int`
        
        write a string to the pipe 
        
    .. memberfunction:: write (data: :cover:`~lang/types Pointer`, len: :cover:`~lang/types Int`) -> :cover:`~lang/types Int`
        
        write 'len' bytes of 'data' to the pipe 
        
    .. memberfunction:: close (mode: :cover:`~lang/types Char`) -> :cover:`~lang/types Int`
        
        close the pipe, either in reading or writing 
        @param arg 'r' = close in reading, 'w' = close in writing
        
        
