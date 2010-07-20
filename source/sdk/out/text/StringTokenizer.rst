text/StringTokenizer
====================

.. module:: text/StringTokenizer

.. class:: StringTokenizer
    
    :extends: :class:`~lang/types Iterable<T>` 
    .. staticmethod:: new~withCharWithoutMaxSplits (input: :cover:`~text/StringTokenizer String` , delim: :cover:`~lang/types Char` ) -> :class:`~text/StringTokenizer StringTokenizer` 
        
    .. method:: init~withCharWithoutMaxSplits (input: :cover:`~text/StringTokenizer String` , delim: :cover:`~lang/types Char` )
        
    .. staticmethod:: new~withStringWithoutMaxSplits (input, delim: :cover:`~text/StringTokenizer String` ) -> :class:`~text/StringTokenizer StringTokenizer` 
        
    .. method:: init~withStringWithoutMaxSplits (input, delim: :cover:`~text/StringTokenizer String` )
        
    .. staticmethod:: new~withChar (input: :cover:`~text/StringTokenizer String` , delim: :cover:`~lang/types Char` , maxSplits: :cover:`~lang/types Int` ) -> :class:`~text/StringTokenizer StringTokenizer` 
        
    .. method:: init~withChar (input: :cover:`~text/StringTokenizer String` , delim: :cover:`~lang/types Char` , maxSplits: :cover:`~lang/types Int` )
        
    .. staticmethod:: new~withString (input, delim: :cover:`~text/StringTokenizer String` , maxSplits: :cover:`~lang/types Int` ) -> :class:`~text/StringTokenizer StringTokenizer` 
        
    .. method:: init~withString (input, delim: :cover:`~text/StringTokenizer String` , maxSplits: :cover:`~lang/types Int` )
        
    .. method:: iterator -> :class:`~lang/types Iterator<T>` 
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: nextToken -> :cover:`~text/StringTokenizer String` 
        
        @return the next token, or null if we're at the end.
        
        
    .. field:: input -> :cover:`~text/StringTokenizer String` 
    
    .. field:: delim -> :cover:`~text/StringTokenizer String` 
    
    .. field:: index -> :cover:`~lang/types Int` 
    
    .. field:: length -> :cover:`~lang/types Int` 
    
    .. field:: maxSplits -> :cover:`~lang/types Int` 
    
    .. field:: splits -> :cover:`~lang/types Int` 
    
    .. field:: empties -> :cover:`~lang/types Bool` 
    
.. class:: StringTokenizerIterator<T>
    
    :extends: :class:`~lang/types Iterator<T>` 
    .. staticmethod:: new (st: :class:`~text/StringTokenizer StringTokenizer` ) -> :class:`~text/StringTokenizer StringTokenizerIterator<T>` 
        
    .. method:: init (st: :class:`~text/StringTokenizer StringTokenizer` )
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: next -> T 
        
    .. method:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. method:: prev -> T 
        
    .. method:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: st -> :class:`~text/StringTokenizer StringTokenizer` 
    
    .. field:: index -> :cover:`~lang/types Int` 
    
.. cover:: String
    
    :from: ``Char*``
    .. method:: split~withString (s: :cover:`~text/StringTokenizer String` , maxSplits: :cover:`~lang/types Int` ) -> :class:`~text/StringTokenizer StringTokenizer` 
        
    .. method:: split~withChar (c: :cover:`~lang/types Char` , maxSplits: :cover:`~lang/types Int` ) -> :class:`~text/StringTokenizer StringTokenizer` 
        
    .. method:: split~withStringWithoutMaxSplits (s: :cover:`~text/StringTokenizer String` ) -> :class:`~text/StringTokenizer StringTokenizer` 
        
    .. method:: split~withCharWithoutMaxSplits (c: :cover:`~lang/types Char` ) -> :class:`~text/StringTokenizer StringTokenizer` 
        
    .. method:: split~withStringWithEmpties (s: :cover:`~text/StringTokenizer String` , empties: :cover:`~lang/types Bool` ) -> :class:`~text/StringTokenizer StringTokenizer` 
        
    .. method:: split~withCharWithEmpties (c: :cover:`~lang/types Char` , empties: :cover:`~lang/types Bool` ) -> :class:`~text/StringTokenizer StringTokenizer` 
        
