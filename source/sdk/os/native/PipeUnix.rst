os/native/PipeUnix
==================

.. module:: os/native/PipeUnix

.. class:: PipeUnix
    
    :extends: :class:`~os/Pipe Pipe` 
    .. staticmemberfunction:: new~withFDs (readFD, writeFD: :cover:`~os/FileDescriptor FileDescriptor` ) -> :class:`~os/native/PipeUnix PipeUnix` 
        
    .. memberfunction:: init~withFDs (readFD, writeFD: :cover:`~os/FileDescriptor FileDescriptor` )
        
    .. staticmemberfunction:: new~twos -> :class:`~os/native/PipeUnix PipeUnix` 
        
    .. memberfunction:: init~twos
        
    .. memberfunction:: read (len: :cover:`~lang/types Int` ) -> :cover:`~lang/types Pointer` 
        
        read 'len' bytes at most from the pipe
        
    .. memberfunction:: write (data: :cover:`~lang/types Pointer` , len: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
        write 'len' bytes of 'data' to the pipe
        
    .. memberfunction:: close (mode: :cover:`~lang/types Char` ) -> :cover:`~lang/types Int` 
        
        close the pipe, either in reading or writing
        @param arg 'r' = close in reading, 'w' = close in writing
        
        
    .. field:: readFD -> :cover:`~os/FileDescriptor FileDescriptor` 
    
    .. field:: writeFD -> :cover:`~os/FileDescriptor FileDescriptor` 
    
