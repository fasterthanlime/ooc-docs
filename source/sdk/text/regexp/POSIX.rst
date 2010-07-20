text/regexp/POSIX
=================

.. module:: text/regexp/POSIX

.. class:: POSIX
    
    :extends: :class:`~text/regexp/RegexpBackend RegexpBackend` 
    .. staticmethod:: new -> :class:`~text/regexp/POSIX POSIX` 
        
    .. method:: init
        
    .. method:: setPattern (pattern: :cover:`~lang/types String` , options: :cover:`~lang/types Int` )
        
    .. method:: getName -> :cover:`~lang/types String` 
        
    .. method:: matches (haystack: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. method:: matches~withOptions (haystack: :cover:`~lang/types String` , options: :cover:`~lang/types Int` ) -> :cover:`~lang/types Bool` 
        
