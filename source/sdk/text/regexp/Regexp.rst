text/regexp/Regexp
==================

.. module:: text/regexp/Regexp

.. class:: Regexp
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~text/regexp/Regexp Regexp` 
        
    .. method:: init
        
    .. staticmethod:: new~withType (type: :cover:`~lang/types Int` ) -> :class:`~text/regexp/Regexp Regexp` 
        
    .. method:: init~withType (type: :cover:`~lang/types Int` )
        
    .. staticmethod:: new~withPattern (pattern: :cover:`~lang/types String` ) -> :class:`~text/regexp/Regexp Regexp` 
        
    .. method:: init~withPattern (pattern: :cover:`~lang/types String` )
        
    .. staticmethod:: new~withPatternAndOptions (pattern: :cover:`~lang/types String` , options: :cover:`~lang/types Int` ) -> :class:`~text/regexp/Regexp Regexp` 
        
    .. method:: init~withPatternAndOptions (pattern: :cover:`~lang/types String` , options: :cover:`~lang/types Int` )
        
    .. method:: setup
        
    .. method:: setPattern~withOptions (pattern: :cover:`~lang/types String` , options: :cover:`~lang/types Int` )
        
    .. method:: setPattern (pattern: :cover:`~lang/types String` )
        
    .. method:: getPattern -> :cover:`~lang/types String` 
        
    .. method:: matches (haystack: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. method:: matches~withOptions (haystack: :cover:`~lang/types String` , options: :cover:`~lang/types Int` ) -> :cover:`~lang/types Bool` 
        
    .. method:: getEngine -> :cover:`~lang/types Int` 
        
    .. method:: getEngineName -> :cover:`~lang/types String` 
        
    .. field:: regexpBackend -> :class:`~text/regexp/RegexpBackend RegexpBackend` 
    
    .. field:: type -> :cover:`~lang/types Int` 
    
