text/regexp/RegexpBackend
=========================

.. module:: text/regexp/RegexpBackend

.. class:: RegexpBackend
    
    .. memberfunction:: setPattern (pattern: String, options: Int)
        
    .. memberfunction:: getPattern -> String
        
    .. memberfunction:: getName -> String
        
    .. memberfunction:: matches (haystack: String) -> Bool
        
    .. memberfunction:: matches~withOptions (haystack: String, options: Int) -> Bool
        
    .. field:: PCRE -> Int
    
    .. field:: POSIX -> Int
    
    .. field:: DEFAULT_TYPE -> Int
    
    .. field:: pattern -> String
    
