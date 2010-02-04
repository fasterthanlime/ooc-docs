text/EscapeSequence
===================

.. module:: text/EscapeSequence

.. class:: EscapeSequence
    
    .. memberfunction:: new -> EscapeSequence
        
    
    .. memberfunction:: init
        
    
    .. memberfunction:: getCharacter (sequence: String, chr: Char*) -> Int
        
        This is a function for decoding an escape sequence. It supports
        the most common escape sequences and also hexadecimal (\x0a) and
        octal (\101) escape sequences.
        You have to pass the escape sequence *without* the leading backslash
        as `sequence` and a pointer to the result char as `chr`.
        The return value is one of `EscapeSequence valid` (`chr` contains a
        valid value now), `EscapeSequence needMore` (`chr`'s content is
        undefined, the escape sequence is incomplete (the case for "\x1") and
        `EscapeSequence invalid` (like for "\u").
        
        
    
    .. memberfunction:: unescape (s: String) -> String
        
        Unescape the string `s`. This will handle hexadecimal, octal and one-character escape
        escape sequences. Unknown escape sequences will just get the '\\' stripped. ("\\u" -> "u")
        
        
    
    .. field:: valid
    
    .. field:: needMore
    
    .. field:: invalid
    

