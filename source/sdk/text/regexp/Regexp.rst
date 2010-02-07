text/regexp/Regexp
==================

.. module:: text/regexp/Regexp

.. class:: Regexp
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new -> :class:`~text/regexp/Regexp Regexp` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withType (type: :cover:`~lang/types Int` ) -> :class:`~text/regexp/Regexp Regexp` 
        
    .. memberfunction:: init~withType (type: :cover:`~lang/types Int` )
        
    .. staticmemberfunction:: new~withPattern (pattern: :cover:`~lang/types String` ) -> :class:`~text/regexp/Regexp Regexp` 
        
    .. memberfunction:: init~withPattern (pattern: :cover:`~lang/types String` )
        
    .. staticmemberfunction:: new~withPatternAndOptions (pattern: :cover:`~lang/types String` , options: :cover:`~lang/types Int` ) -> :class:`~text/regexp/Regexp Regexp` 
        
    .. memberfunction:: init~withPatternAndOptions (pattern: :cover:`~lang/types String` , options: :cover:`~lang/types Int` )
        
    .. memberfunction:: setup
        
    .. memberfunction:: setPattern~withOptions (pattern: :cover:`~lang/types String` , options: :cover:`~lang/types Int` )
        
    .. memberfunction:: setPattern (pattern: :cover:`~lang/types String` )
        
    .. memberfunction:: getPattern -> :cover:`~lang/types String` 
        
    .. memberfunction:: matches (haystack: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: matches~withOptions (haystack: :cover:`~lang/types String` , options: :cover:`~lang/types Int` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: getEngine -> :cover:`~lang/types Int` 
        
    .. memberfunction:: getEngineName -> :cover:`~lang/types String` 
        
    .. field:: regexpBackend -> :class:`~text/regexp/RegexpBackend RegexpBackend` 
    
    .. field:: type -> :cover:`~lang/types Int` 
    
