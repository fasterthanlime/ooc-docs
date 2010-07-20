text/Regexp
===========

.. module:: text/Regexp

.. cover:: Pcre
    
    :from: ``pcre*``
    .. method:: compile (...) -> :cover:`~text/Regexp Pcre` 
        
    .. method:: free
        
    .. method:: exec (...) -> :cover:`~lang/types Int` 
        
    .. method:: getStringNumber (...) -> :cover:`~lang/types Int` 
        
.. cover:: RegexpOption
    
.. class:: Regexp
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: compile~withOptions (pattern: :cover:`~lang/types String` , options: :cover:`~lang/types Int` ) -> :class:`~text/Regexp Regexp` 
        
        Compile a regular expression pattern.
        
        :param pattern: regular expression pattern to compile
        :param options: compiling options.
        :return: new regular expression object if successful, null if error occured.
        
        
    .. staticmethod:: compile (pattern: :cover:`~lang/types String` ) -> :class:`~text/Regexp Regexp` 
        
    .. staticmethod:: new (pcre: :cover:`~text/Regexp Pcre` ) -> :class:`~text/Regexp Regexp` 
        
    .. method:: init (pcre: :cover:`~text/Regexp Pcre` )
        
    .. method:: matches~withLengthAndStart (subject: :cover:`~lang/types String` , start: :cover:`~lang/types Int` , length: :cover:`~lang/types SizeT` ) -> :class:`~text/Regexp Match` 
        
        If one or more characters from the start of the subject string
        matches the pattern, returns a Match object. Returns null if match fails.
        
        :param subject: subject string to test for match
        :param start: offset within subject at which to start matching
        :return: Match object if a match was found, otherwise null
        
        
    .. method:: matches (subject: :cover:`~lang/types String` ) -> :class:`~text/Regexp Match` 
        
    .. field:: errorMsg -> :cover:`~lang/types String` 
    
    .. field:: errorOffset -> :cover:`~lang/types Int` 
    
    .. field:: pcre -> :cover:`~text/Regexp Pcre` 
    
    .. field:: maxSubstrings -> :cover:`~lang/types Int` 
    
.. class:: Match
    
    :extends: :class:`~lang/types Iterable<T>` 
    .. staticmethod:: new (regexp: :class:`~text/Regexp Regexp` , groupCount: :cover:`~lang/types Int` , subject: :cover:`~lang/types String` , ovector: :cover:`~lang/types Int` *) -> :class:`~text/Regexp Match` 
        
    .. method:: init (regexp: :class:`~text/Regexp Regexp` , groupCount: :cover:`~lang/types Int` , subject: :cover:`~lang/types String` , ovector: :cover:`~lang/types Int` *)
        
    .. method:: start~byIndex (index: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
        Returns the starting position of the match group by index.
        
        
    .. method:: end~byIndex (index: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
        Returns the ending position of the match group by index.
        
        
    .. method:: group~byIndex (index: :cover:`~lang/types Int` ) -> :cover:`~lang/types String` 
        
        Returns a subgroup of the matched string by index.
        
        
    .. method:: group~byName (name: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        Returns a subgroup of the matched string by name.
        
        
    .. method:: iterator -> :class:`~lang/types Iterator<T>` 
        
    .. field:: regexp -> :class:`~text/Regexp Regexp` 
    
    .. field:: groupCount -> :cover:`~lang/types Int` 
    
    .. field:: subject -> :cover:`~lang/types String` 
    
    .. field:: ovector -> :cover:`~lang/types Int` *
    
.. class:: MatchGroupIterator<T>
    
    :extends: :class:`~lang/types Iterator<T>` 
    .. staticmethod:: new (matchObject: :class:`~text/Regexp Match` ) -> :class:`~text/Regexp MatchGroupIterator<T>` 
        
    .. method:: init (matchObject: :class:`~text/Regexp Match` )
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: next -> T 
        
    .. method:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. method:: prev -> T 
        
    .. method:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: matchObject -> :class:`~text/Regexp Match` 
    
    .. field:: index -> :cover:`~lang/types Int` 
    
