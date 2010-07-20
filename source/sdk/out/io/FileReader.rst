io/FileReader
=============

.. module:: io/FileReader

.. function:: fopen (filename, mode: :cover:`~lang/types Char` *) -> :cover:`~lang/stdio FILE` *
    
.. function:: fread (ptr: :cover:`~lang/types Pointer` , size, count: :cover:`~lang/types SizeT` , stream: :cover:`~lang/stdio FILE` *) -> :cover:`~lang/types SizeT` 
    
.. function:: ferror (stream: :cover:`~lang/stdio FILE` *) -> :cover:`~lang/types Int` 
    
.. function:: feof (stream: :cover:`~lang/stdio FILE` *) -> :cover:`~lang/types Int` 
    
.. function:: fseek (stream: :cover:`~lang/stdio FILE` *, offset: :cover:`~lang/types Long` , origin: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: ftell (stream: :cover:`~lang/stdio FILE` *) -> :cover:`~lang/types Long` 
    
.. class:: FileReader
    
    :extends: :class:`~io/Reader Reader` 
    .. staticmethod:: new~withFile (fileObject: :class:`~io/File File` ) -> :class:`~io/FileReader FileReader` 
        
    .. method:: init~withFile (fileObject: :class:`~io/File File` )
        
    .. staticmethod:: new~withName (fileName: :cover:`~lang/types String` ) -> :class:`~io/FileReader FileReader` 
        
    .. method:: init~withName (fileName: :cover:`~lang/types String` )
        
    .. staticmethod:: new~withMode (fileName, mode: :cover:`~lang/types String` ) -> :class:`~io/FileReader FileReader` 
        
    .. method:: init~withMode (fileName, mode: :cover:`~lang/types String` )
        
    .. method:: read (chars: :cover:`~lang/types String` , offset, count: :cover:`~lang/types Int` ) -> :cover:`~lang/types SizeT` 
        
    .. method:: read~char -> :cover:`~lang/types Char` 
        
    .. method:: readLine -> :cover:`~lang/types String` 
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: rewind (offset: :cover:`~lang/types Int` )
        
    .. method:: mark -> :cover:`~lang/types Long` 
        
    .. method:: reset (marker: :cover:`~lang/types Long` )
        
    .. method:: close
        
    .. field:: file -> :cover:`~lang/stdio FILE` *
    
.. var:: SEEK_CUR -> :cover:`~lang/types Int` 

.. var:: SEEK_SET -> :cover:`~lang/types Int` 

.. var:: SEEK_END -> :cover:`~lang/types Int` 

