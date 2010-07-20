text/Shlex
==========

.. module:: text/Shlex

.. class:: Shlex
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~text/Shlex Shlex` 
        
    .. method:: init
        
    .. method:: _add (unquote: :cover:`~lang/types Bool` )
        
    .. method:: close -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. method:: feed~char (chr: :cover:`~lang/types Char` )
        
    .. method:: feed~string (s: :cover:`~lang/types String` )
        
    .. staticmethod:: split (s: :cover:`~lang/types String` ) -> :class:`~structs/ArrayList ArrayList<T>` 
        
        Split the string following the shell lexer rules and return the splitted parts.
        
    .. field:: state -> :cover:`~lang/types Int` 
    
    .. field:: buffer -> :class:`~text/Buffer Buffer` 
    
    .. field:: result -> :class:`~structs/ArrayList ArrayList<T>` 
    
    .. field:: backslash -> :cover:`~lang/types Bool` 
    
.. var:: WAIT -> :cover:`~lang/types Int` 

.. var:: WORD -> :cover:`~lang/types Int` 

.. var:: SQUOTED -> :cover:`~lang/types Int` 

.. var:: DQUOTED -> :cover:`~lang/types Int` 

