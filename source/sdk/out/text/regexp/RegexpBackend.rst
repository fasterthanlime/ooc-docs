text/regexp/RegexpBackend
=========================

.. module:: text/regexp/RegexpBackend

.. class:: RegexpBackend
    
    :extends: :class:`~lang/types Object` 
    .. method:: setPattern (pattern: :cover:`~lang/types String` , options: :cover:`~lang/types Int` )
        
    .. method:: getPattern -> :cover:`~lang/types String` 
        
    .. method:: getName -> :cover:`~lang/types String` 
        
    .. method:: matches (haystack: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. method:: matches~withOptions (haystack: :cover:`~lang/types String` , options: :cover:`~lang/types Int` ) -> :cover:`~lang/types Bool` 
        
    .. field:: PCRE -> :cover:`~lang/types Int` 
    
    .. field:: POSIX -> :cover:`~lang/types Int` 
    
    .. field:: DEFAULT_TYPE -> :cover:`~lang/types Int` 
    
    .. field:: pattern -> :cover:`~lang/types String` 
    
