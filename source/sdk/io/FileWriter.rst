io/FileWriter
=============

.. module:: io/FileWriter

.. class:: FileWriter
    
    .. staticmemberfunction:: new~withFile (fileObject: File, append: Bool) -> FileWriter
        
    .. memberfunction:: init~withFile (fileObject: File, append: Bool)
        
    .. staticmemberfunction:: new~withFileOverwrite (fileObject: File) -> FileWriter
        
    .. memberfunction:: init~withFileOverwrite (fileObject: File)
        
    .. staticmemberfunction:: new~withName (fileName: String, append: Bool) -> FileWriter
        
    .. memberfunction:: init~withName (fileName: String, append: Bool)
        
    .. staticmemberfunction:: new~withNameAndFileOverwrite (fileName: String) -> FileWriter
        
    .. memberfunction:: init~withNameAndFileOverwrite (fileName: String)
        
    .. staticmemberfunction:: new~withNameOverwrite (fileName: String) -> FileWriter
        
    .. memberfunction:: init~withNameOverwrite (fileName: String)
        
    .. memberfunction:: write (chars: String, length: SizeT) -> SizeT
        
    .. memberfunction:: write~chr (chr: Char)
        
    .. memberfunction:: close
        
    .. memberfunction:: writef (fmt: String, ...)
        
    .. memberfunction:: vwritef (fmt: String, args: VaList)
        
    .. field:: file -> FStream
    
