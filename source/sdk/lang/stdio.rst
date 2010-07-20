lang/stdio
==========

.. module:: lang/stdio

.. function:: println~withStr (str: :cover:`~lang/types String` )
    
.. function:: println
    
.. function:: printf (:cover:`~lang/types Char` *, ...) -> :cover:`~lang/types Int` 
    
.. function:: fprintf (:cover:`~lang/stdio FStream` , :cover:`~lang/types Char` *, ...) -> :cover:`~lang/types Int` 
    
.. function:: sprintf (:cover:`~lang/types Char` *, :cover:`~lang/types Char` *, ...) -> :cover:`~lang/types Int` 
    
.. function:: snprintf (:cover:`~lang/types Char` *, :cover:`~lang/types Int` , :cover:`~lang/types Char` *, ...) -> :cover:`~lang/types Int` 
    
.. function:: vprintf (:cover:`~lang/types Char` *, :cover:`~lang/vararg VaList` ) -> :cover:`~lang/types Int` 
    
.. function:: vfprintf (:cover:`~lang/stdio FStream` , :cover:`~lang/types Char` *, :cover:`~lang/vararg VaList` ) -> :cover:`~lang/types Int` 
    
.. function:: vsprintf (:cover:`~lang/types Char` *, :cover:`~lang/types Char` *, :cover:`~lang/vararg VaList` ) -> :cover:`~lang/types Int` 
    
.. function:: vsnprintf (:cover:`~lang/types Char` *, :cover:`~lang/types Int` , :cover:`~lang/types Char` *, :cover:`~lang/vararg VaList` ) -> :cover:`~lang/types Int` 
    
.. function:: fread (ptr: :cover:`~lang/types Pointer` , size, nmemb: :cover:`~lang/types SizeT` , stream: :cover:`~lang/stdio FStream` ) -> :cover:`~lang/types SizeT` 
    
.. function:: fwrite (ptr: :cover:`~lang/types Pointer` , size, nmemb: :cover:`~lang/types SizeT` , stream: :cover:`~lang/stdio FStream` ) -> :cover:`~lang/types SizeT` 
    
.. function:: feof (stream: :cover:`~lang/stdio FStream` ) -> :cover:`~lang/types Int` 
    
.. function:: fopen (:cover:`~lang/types Char` *, :cover:`~lang/types Char` *) -> :cover:`~lang/stdio FStream` 
    
.. function:: fclose (:cover:`~lang/stdio FStream` ) -> :cover:`~lang/types Int` 
    
.. function:: fflush (stream: :cover:`~lang/stdio FStream` )
    
.. function:: fputc (:cover:`~lang/types Char` , :cover:`~lang/stdio FStream` )
    
.. function:: fputs (:cover:`~lang/types Char` *, :cover:`~lang/stdio FStream` )
    
.. function:: scanf (format: :cover:`~lang/types Char` *, ...) -> :cover:`~lang/types Int` 
    
.. function:: fscanf (stream: :cover:`~lang/stdio FStream` , format: :cover:`~lang/types Char` *, ...) -> :cover:`~lang/types Int` 
    
.. function:: sscanf (str, format: :cover:`~lang/types Char` *, ...) -> :cover:`~lang/types Int` 
    
.. function:: vscanf (format: :cover:`~lang/types Char` *, ap: :cover:`~lang/vararg VaList` ) -> :cover:`~lang/types Int` 
    
.. function:: vfscanf (stream: :cover:`~lang/stdio FStream` , format: :cover:`~lang/types Char` *, ap: :cover:`~lang/vararg VaList` ) -> :cover:`~lang/types Int` 
    
.. function:: vsscanf (str, format: :cover:`~lang/types Char` *, ap: :cover:`~lang/vararg VaList` ) -> :cover:`~lang/types Int` 
    
.. function:: fgets (str: :cover:`~lang/types Char` *, length: :cover:`~lang/types SizeT` , stream: :cover:`~lang/stdio FStream` ) -> :cover:`~lang/types Char` *
    
.. cover:: FILE
    
.. cover:: FStream
    
    :from: ``FILE*``
    .. method:: open (filename: :cover:`~lang/types String` , mode: :cover:`~lang/types String` ) -> :cover:`~lang/stdio FStream` 
        
    .. method:: close -> :cover:`~lang/types Int` 
        
    .. method:: flush
        
    .. method:: readChar -> :cover:`~lang/types Char` 
        
    .. method:: readLine -> :cover:`~lang/types String` 
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: write~chr (chr: :cover:`~lang/types Char` )
        
    .. method:: write (str: :cover:`~lang/types String` )
        
    .. method:: write~precise (str: :cover:`~lang/types Char` *, offset, length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types SizeT` 
        
.. var:: stdout -> :cover:`~lang/stdio FStream` 

.. var:: stderr -> :cover:`~lang/stdio FStream` 

.. var:: stdin -> :cover:`~lang/stdio FStream` 

