os/Pipe
=======

.. module:: os/Pipe

.. class:: Pipe
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~os/Pipe Pipe` 
        
    .. method:: read (len: :cover:`~lang/types Int` ) -> :cover:`~lang/types Pointer` 
        
        read 'len' bytes at most from the pipe
        
    .. method:: write~string (str: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
        write a string to the pipe
        
    .. method:: write (data: :cover:`~lang/types Pointer` , len: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
        write 'len' bytes of 'data' to the pipe
        
    .. method:: close (mode: :cover:`~lang/types Char` ) -> :cover:`~lang/types Int` 
        
        close the pipe, either in reading or writing
        @param arg 'r' = close in reading, 'w' = close in writing
        
        
