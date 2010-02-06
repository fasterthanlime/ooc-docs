text/Shlex
==========

.. module:: text/Shlex

.. class:: Shlex
    
    .. staticmemberfunction:: new -> Shlex
        
    .. memberfunction:: init
        
    .. memberfunction:: _add (unquote: Bool)
        
    .. memberfunction:: close -> ArrayList<T>
        
    .. memberfunction:: feed~char (chr: Char)
        
    .. memberfunction:: feed~string (s: String)
        
    .. staticmemberfunction:: split (s: String) -> ArrayList<T>
        
    .. field:: state -> Int
    
    .. field:: buffer -> StringBuffer
    
    .. field:: result -> ArrayList<T>
    
    .. field:: backslash -> Bool
    
.. data:: WAIT -> Int

.. data:: WORD -> Int

.. data:: SQUOTED -> Int

.. data:: DQUOTED -> Int

