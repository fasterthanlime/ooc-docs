text/regexp/PCRE
================

.. module:: text/regexp/PCRE

.. function:: pcre_compile (:cover:`~lang/types String` , :cover:`~lang/types Int` , :cover:`~lang/types Char` **, :cover:`~lang/types Int` *, :cover:`~lang/types Pointer` ) -> :cover:`~text/regexp/PCRE Pcre` 
    
.. function:: pcre_exec (:cover:`~text/regexp/PCRE Pcre` , :cover:`~lang/types Pointer` , :cover:`~lang/types String` , :cover:`~lang/types Int` , :cover:`~lang/types Int` , :cover:`~lang/types Int` , :cover:`~lang/types Int` *, :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: pcre_free (:cover:`~lang/types Pointer` )
    
.. cover:: Pcre
    
    :from: ``pcre*``
.. class:: PCRE
    
    :extends: :class:`~text/regexp/RegexpBackend RegexpBackend` 
    .. staticmethod:: new -> :class:`~text/regexp/PCRE PCRE` 
        
    .. method:: init
        
    .. method:: setPattern (pattern: :cover:`~lang/types String` , options: :cover:`~lang/types Int` )
        
    .. method:: getName -> :cover:`~lang/types String` 
        
    .. method:: matches (haystack: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. method:: matches~withOptions (haystack: :cover:`~lang/types String` , options: :cover:`~lang/types Int` ) -> :cover:`~lang/types Bool` 
        
    .. field:: CASELESS -> :cover:`~lang/types Int` 
    
    .. field:: error -> :cover:`~lang/types String` 
    
    .. field:: errorNum -> :cover:`~lang/types Int` 
    
    .. field:: re -> :cover:`~text/regexp/PCRE Pcre` 
    
.. var:: PCRE_DEBUG -> :cover:`~lang/types Bool` 

