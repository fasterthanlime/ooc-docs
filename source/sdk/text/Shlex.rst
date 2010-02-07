text/Shlex
==========

.. module:: text/Shlex

.. class:: Shlex
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new -> :class:`~text/Shlex Shlex` 
        
    .. memberfunction:: init
        
    .. memberfunction:: _add (unquote: :cover:`~lang/types Bool` )
        
    .. memberfunction:: close -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. memberfunction:: feed~char (chr: :cover:`~lang/types Char` )
        
    .. memberfunction:: feed~string (s: :cover:`~lang/types String` )
        
    .. staticmemberfunction:: split (s: :cover:`~lang/types String` ) -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. field:: state -> :cover:`~lang/types Int` 
    
    .. field:: buffer -> :class:`~text/StringBuffer StringBuffer` 
    
    .. field:: result -> :class:`~structs/ArrayList ArrayList<T>` 
    
    .. field:: backslash -> :cover:`~lang/types Bool` 
    
.. var:: WAIT -> :cover:`~lang/types Int` 

.. var:: WORD -> :cover:`~lang/types Int` 

.. var:: SQUOTED -> :cover:`~lang/types Int` 

.. var:: DQUOTED -> :cover:`~lang/types Int` 

