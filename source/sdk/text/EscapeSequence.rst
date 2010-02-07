text/EscapeSequence
===================

.. module:: text/EscapeSequence

.. class:: EscapeSequence
    
    .. staticmemberfunction:: new -> :class:`~text/EscapeSequence EscapeSequence` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: getCharacter (sequence: :cover:`~lang/types String` , chr: :cover:`~lang/types Char` *) -> :cover:`~lang/types Int` 
        
        This is a function for decoding an escape sequence. It supports
        the most common escape sequences and also hexadecimal (\x0a) and
        octal (\101) escape sequences.
        You have to pass the escape sequence *without* the leading backslash
        as `sequence` and a pointer to the result char as `chr`.
        The return value is one of `EscapeSequence valid` (`chr` contains a
        valid value now), `EscapeSequence needMore` (`chr`'s content is
        undefined, the escape sequence is incomplete (the case for "\x1") and
        `EscapeSequence invalid` (like for "\u").
        
        
    .. staticmemberfunction:: unescape (s: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        Unescape the string `s`. This will handle hexadecimal, octal and one-character escape
        escape sequences. Unknown escape sequences will just get the '\\' stripped. ("\\u" -> "u")
        
        
    .. staticmemberfunction:: escape (s: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        Escape a string. This will replace non-printable characters with equivalents like \something or \x??. *
        
    .. field:: valid -> :cover:`~lang/types Int` 
    
    .. field:: needMore -> :cover:`~lang/types Int` 
    
    .. field:: invalid -> :cover:`~lang/types Int` 
    
