io/Reader
=========

.. module:: io/Reader

.. class:: Reader
    
    :extends: :class:`~lang/types Object` 
    .. method:: read (chars: :cover:`~lang/types String` , offset, count: :cover:`~lang/types Int` ) -> :cover:`~lang/types SizeT` 
        
    .. method:: read~char -> :cover:`~lang/types Char` 
        
    .. method:: readUntil (end: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
    .. method:: readLine -> :cover:`~lang/types String` 
        
    .. method:: peek -> :cover:`~lang/types Char` 
        
    .. method:: skipWhile (unwanted: :cover:`~lang/types Char` )
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: rewind (offset: :cover:`~lang/types Int` )
        
    .. method:: mark -> :cover:`~lang/types Long` 
        
    .. method:: reset (marker: :cover:`~lang/types Long` )
        
    .. method:: skip (offset: :cover:`~lang/types Int` )
        
    .. field:: marker -> :cover:`~lang/types Long` 
    
