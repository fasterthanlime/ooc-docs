os/PipeReader
=============

.. module:: os/PipeReader

.. class:: PipeReader
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new (pipe: :class:`~os/Pipe Pipe` ) -> :class:`~os/PipeReader PipeReader` 
        
    .. method:: init (pipe: :class:`~os/Pipe Pipe` )
        
    .. method:: read -> :cover:`~lang/types String` 
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: toString -> :cover:`~lang/types String` 
        
    .. field:: eof -> :cover:`~lang/types Bool` 
    
    .. field:: pipe -> :class:`~os/Pipe Pipe` 
    
    .. field:: buf -> :cover:`~lang/types String` 
    
    .. field:: BUF_SIZE -> :cover:`~lang/types Int` 
    
