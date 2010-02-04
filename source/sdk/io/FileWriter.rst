io/FileWriter
=============

.. module:: io/FileWriter

.. class:: FileWriter
    
    .. memberfunction:: new~withFile (fileObject: File, append: Bool) -> FileWriter
        
    
    .. memberfunction:: init~withFile (fileObject: File, append: Bool)
        
    
    .. memberfunction:: new~withFileOverwrite (fileObject: File) -> FileWriter
        
    
    .. memberfunction:: init~withFileOverwrite (fileObject: File)
        
    
    .. memberfunction:: new~withName (fileName: String, append: Bool) -> FileWriter
        
    
    .. memberfunction:: init~withName (fileName: String, append: Bool)
        
    
    .. memberfunction:: new~withNameAndFileOverwrite (fileName: String) -> FileWriter
        
    
    .. memberfunction:: init~withNameAndFileOverwrite (fileName: String)
        
    
    .. memberfunction:: new~withNameOverwrite (fileName: String) -> FileWriter
        
    
    .. memberfunction:: init~withNameOverwrite (fileName: String)
        
    
    .. memberfunction:: write (chars: String, length: SizeT) -> SizeT
        
    
    .. memberfunction:: write~chr (chr: Char)
        
    
    .. memberfunction:: close
        
    
    .. memberfunction:: writef (fmt: String, ...)
        
    
    .. memberfunction:: vwritef (fmt: String, args: VaList)
        
    
    .. field:: file
    

