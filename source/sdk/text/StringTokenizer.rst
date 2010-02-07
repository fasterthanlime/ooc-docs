text/StringTokenizer
====================

.. module:: text/StringTokenizer

.. class:: StringTokenizer
    
    .. staticmemberfunction:: new~withCharWithoutMaxSplits (input: :cover:`~text/StringTokenizer String`, delim: :cover:`~lang/types Char`) -> :class:`~text/StringTokenizer StringTokenizer`
        
    .. memberfunction:: init~withCharWithoutMaxSplits (input: :cover:`~text/StringTokenizer String`, delim: :cover:`~lang/types Char`)
        
    .. staticmemberfunction:: new~withStringWithoutMaxSplits (input, delim: :cover:`~text/StringTokenizer String`) -> :class:`~text/StringTokenizer StringTokenizer`
        
    .. memberfunction:: init~withStringWithoutMaxSplits (input, delim: :cover:`~text/StringTokenizer String`)
        
    .. staticmemberfunction:: new~withChar (input: :cover:`~text/StringTokenizer String`, delim: :cover:`~lang/types Char`, maxSplits: :cover:`~lang/types Int`) -> :class:`~text/StringTokenizer StringTokenizer`
        
    .. memberfunction:: init~withChar (input: :cover:`~text/StringTokenizer String`, delim: :cover:`~lang/types Char`, maxSplits: :cover:`~lang/types Int`)
        
    .. staticmemberfunction:: new~withString (input, delim: :cover:`~text/StringTokenizer String`, maxSplits: :cover:`~lang/types Int`) -> :class:`~text/StringTokenizer StringTokenizer`
        
    .. memberfunction:: init~withString (input, delim: :cover:`~text/StringTokenizer String`, maxSplits: :cover:`~lang/types Int`)
        
    .. memberfunction:: iterator -> :class:`~lang/types Iterator<T>`
        
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool`
        
    .. memberfunction:: nextToken -> :cover:`~text/StringTokenizer String`
        
        @return the next token, or null if we're at the end.
        
        
    .. field:: input -> :cover:`~text/StringTokenizer String`
    
    .. field:: delim -> :cover:`~text/StringTokenizer String`
    
    .. field:: index -> :cover:`~lang/types Int`
    
    .. field:: length -> :cover:`~lang/types Int`
    
    .. field:: maxSplits -> :cover:`~lang/types Int`
    
    .. field:: splits -> :cover:`~lang/types Int`
    
    .. field:: empties -> :cover:`~lang/types Bool`
    
.. class:: StringTokenizerIterator<T>
    
    .. staticmemberfunction:: new (st: :class:`~text/StringTokenizer StringTokenizer`) -> :class:`~text/StringTokenizer StringTokenizerIterator<T>`
        
    .. memberfunction:: init (st: :class:`~text/StringTokenizer StringTokenizer`)
        
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool`
        
    .. memberfunction:: next -> T
        
    .. memberfunction:: hasPrev -> :cover:`~lang/types Bool`
        
    .. memberfunction:: prev -> T
        
    .. memberfunction:: remove -> :cover:`~lang/types Bool`
        
    .. field:: st -> :class:`~text/StringTokenizer StringTokenizer`
    
    .. field:: index -> :cover:`~lang/types Int`
    
.. cover:: String
    
    .. memberfunction:: split~withString (s: :cover:`~text/StringTokenizer String`, maxSplits: :cover:`~lang/types Int`) -> :class:`~text/StringTokenizer StringTokenizer`
        
    .. memberfunction:: split~withChar (c: :cover:`~lang/types Char`, maxSplits: :cover:`~lang/types Int`) -> :class:`~text/StringTokenizer StringTokenizer`
        
    .. memberfunction:: split~withStringWithoutMaxSplits (s: :cover:`~text/StringTokenizer String`) -> :class:`~text/StringTokenizer StringTokenizer`
        
    .. memberfunction:: split~withCharWithoutMaxSplits (c: :cover:`~lang/types Char`) -> :class:`~text/StringTokenizer StringTokenizer`
        
    .. memberfunction:: split~withStringWithEmpties (s: :cover:`~text/StringTokenizer String`, empties: :cover:`~lang/types Bool`) -> :class:`~text/StringTokenizer StringTokenizer`
        
    .. memberfunction:: split~withCharWithEmpties (c: :cover:`~lang/types Char`, empties: :cover:`~lang/types Bool`) -> :class:`~text/StringTokenizer StringTokenizer`
        
