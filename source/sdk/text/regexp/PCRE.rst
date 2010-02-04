text/regexp/PCRE
================

.. module:: text/regexp/PCRE

.. function:: pcre_compile (String, Int, Char**, Int*, Pointer) -> Pcre
    
.. function:: pcre_exec (Pcre, Pointer, String, Int, Int, Int, Int*, Int) -> Int
    
.. function:: pcre_free (Pointer)
    
.. cover:: Pcre
    
.. class:: PCRE
    
    .. staticmemberfunction:: new -> PCRE
        
    .. memberfunction:: init
        
    .. memberfunction:: setPattern (pattern: String, options: Int)
        
    .. memberfunction:: getName -> String
        
    .. memberfunction:: matches (haystack: String) -> Bool
        
    .. memberfunction:: matches~withOptions (haystack: String, options: Int) -> Bool
        
    .. field:: CASELESS
    
    .. field:: error
    
    .. field:: errorNum
    
    .. field:: re
    
.. data:: PCRE_DEBUG

