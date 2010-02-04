io/FileReader
=============

.. module:: io/FileReader

.. function:: fopen (filename, mode: Char*) -> FILE*
    

.. function:: fread (ptr: Pointer, size, count: SizeT, stream: FILE*) -> SizeT
    

.. function:: feof (stream: FILE*) -> Int
    

.. function:: fseek (stream: FILE*, offset: Long, origin: Int) -> Int
    

.. function:: SEEK_CUR
    

.. function:: SEEK_SET
    

.. function:: SEEK_END
    

.. function:: ftell (stream: FILE*) -> Long
    

.. class:: FileReader
    
    .. memberfunction:: new~withFile (fileObject: File) -> FileReader
        
    
    .. memberfunction:: init~withFile (fileObject: File)
        
    
    .. memberfunction:: new~withName (fileName: String) -> FileReader
        
    
    .. memberfunction:: init~withName (fileName: String)
        
    
    .. memberfunction:: read (chars: String, offset, count: Int) -> SizeT
        
    
    .. memberfunction:: read~char -> Char
        
    
    .. memberfunction:: readLine -> String
        
    
    .. memberfunction:: hasNext -> Bool
        
    
    .. memberfunction:: rewind (offset: Int)
        
    
    .. memberfunction:: mark -> Long
        
    
    .. memberfunction:: reset (marker: Long)
        
    
    .. memberfunction:: close
        
    
    .. field:: file
    

