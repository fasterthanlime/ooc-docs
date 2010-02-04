lang/stdio
==========

.. module:: lang/stdio

.. function:: println~withStr (str: String)
    
.. function:: println
    
.. function:: printf (String, ...) -> Int
    
.. function:: fprintf (FStream, String, ...) -> Int
    
.. function:: sprintf (String, String, ...) -> Int
    
.. function:: snprintf (String, Int, String, ...) -> Int
    
.. function:: vprintf (String, VaList) -> Int
    
.. function:: vfprintf (FStream, String, VaList) -> Int
    
.. function:: vsprintf (String, String, VaList) -> Int
    
.. function:: vsnprintf (String, Int, String, VaList) -> Int
    
.. function:: fread (ptr: Pointer, size, nmemb: SizeT, stream: FStream) -> SizeT
    
.. function:: fwrite (ptr: Pointer, size, nmemb: SizeT, stream: FStream) -> SizeT
    
.. function:: feof (stream: FStream) -> Int
    
.. function:: fopen (String, String) -> FStream
    
.. function:: fclose (FStream) -> Int
    
.. function:: fflush (stream: FStream)
    
.. function:: fputc (Char, FStream)
    
.. function:: fputs (String, FStream)
    
.. function:: scanf (format: String, ...) -> Int
    
.. function:: fscanf (stream: FStream, format: String, ...) -> Int
    
.. function:: sscanf (str, format: String, ...) -> Int
    
.. function:: vscanf (format: String, ap: VaList) -> Int
    
.. function:: vfscanf (stream: FStream, format: String, ap: VaList) -> Int
    
.. function:: vsscanf (str, format: String, ap: VaList) -> Int
    
.. function:: fgets (str: String, length: SizeT, stream: FStream)
    
.. cover:: FILE
    
.. cover:: FStream
    
    .. memberfunction:: open (filename: String, mode: String) -> FStream
        
    .. memberfunction:: close -> Int
        
    .. memberfunction:: flush
        
    .. memberfunction:: readChar -> Char
        
    .. memberfunction:: readLine -> String
        
    .. memberfunction:: hasNext -> Bool
        
    .. memberfunction:: write~chr (chr: Char)
        
    .. memberfunction:: write (str: String)
        
    .. memberfunction:: write~precise (str: Char*, offset, length: SizeT) -> SizeT
        
.. data:: stdout

.. data:: stderr

.. data:: stdin

