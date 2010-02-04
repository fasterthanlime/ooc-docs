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
        
    .. field:: state
    
    .. field:: buffer
    
    .. field:: result
    
    .. field:: backslash
    
.. data:: WAIT

.. data:: WORD

.. data:: SQUOTED

.. data:: DQUOTED

