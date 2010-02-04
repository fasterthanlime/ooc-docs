text/regexp/Regexp
==================

.. module:: text/regexp/Regexp

.. class:: Regexp
    
    .. staticmemberfunction:: new -> Regexp
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withType (type: Int) -> Regexp
        
    .. memberfunction:: init~withType (type: Int)
        
    .. staticmemberfunction:: new~withPattern (pattern: String) -> Regexp
        
    .. memberfunction:: init~withPattern (pattern: String)
        
    .. staticmemberfunction:: new~withPatternAndOptions (pattern: String, options: Int) -> Regexp
        
    .. memberfunction:: init~withPatternAndOptions (pattern: String, options: Int)
        
    .. memberfunction:: setup
        
    .. memberfunction:: setPattern~withOptions (pattern: String, options: Int)
        
    .. memberfunction:: setPattern (pattern: String)
        
    .. memberfunction:: getPattern -> String
        
    .. memberfunction:: matches (haystack: String) -> Bool
        
    .. memberfunction:: matches~withOptions (haystack: String, options: Int) -> Bool
        
    .. memberfunction:: getEngine -> Int
        
    .. memberfunction:: getEngineName -> String
        
    .. field:: regexpBackend
    
    .. field:: type
    
