text/StringTokenizer
====================

.. module:: text/StringTokenizer

.. class:: StringTokenizer
    
    .. staticmemberfunction:: new~withCharWithoutMaxSplits (input: String, delim: Char) -> StringTokenizer
        
    .. memberfunction:: init~withCharWithoutMaxSplits (input: String, delim: Char)
        
    .. staticmemberfunction:: new~withStringWithoutMaxSplits (input, delim: String) -> StringTokenizer
        
    .. memberfunction:: init~withStringWithoutMaxSplits (input, delim: String)
        
    .. staticmemberfunction:: new~withChar (input: String, delim: Char, maxSplits: Int) -> StringTokenizer
        
    .. memberfunction:: init~withChar (input: String, delim: Char, maxSplits: Int)
        
    .. staticmemberfunction:: new~withString (input, delim: String, maxSplits: Int) -> StringTokenizer
        
    .. memberfunction:: init~withString (input, delim: String, maxSplits: Int)
        
    .. memberfunction:: iterator -> Iterator<T>
        
    .. memberfunction:: hasNext -> Bool
        
    .. memberfunction:: nextToken -> String
        
        @return the next token, or null if we're at the end.
        
        
    .. field:: input
    
    .. field:: delim
    
    .. field:: index
    
    .. field:: length
    
    .. field:: maxSplits
    
    .. field:: splits
    
    .. field:: empties
    
.. class:: StringTokenizerIterator<T>
    
    .. staticmemberfunction:: new (st: StringTokenizer) -> StringTokenizerIterator<T>
        
    .. memberfunction:: init (st: StringTokenizer)
        
    .. memberfunction:: hasNext -> Bool
        
    .. memberfunction:: next -> T
        
    .. memberfunction:: hasPrev -> Bool
        
    .. memberfunction:: prev -> T
        
    .. memberfunction:: remove -> Bool
        
    .. field:: st
    
    .. field:: index
    
.. cover:: String
    
    .. memberfunction:: split~withString (s: String, maxSplits: Int) -> StringTokenizer
        
    .. memberfunction:: split~withChar (c: Char, maxSplits: Int) -> StringTokenizer
        
    .. memberfunction:: split~withStringWithoutMaxSplits (s: String) -> StringTokenizer
        
    .. memberfunction:: split~withCharWithoutMaxSplits (c: Char) -> StringTokenizer
        
    .. memberfunction:: split~withStringWithEmpties (s: String, empties: Bool) -> StringTokenizer
        
    .. memberfunction:: split~withCharWithEmpties (c: Char, empties: Bool) -> StringTokenizer
        
