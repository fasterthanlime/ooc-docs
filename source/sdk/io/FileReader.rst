io/FileReader
=============

.. module:: io/FileReader

.. function:: fopen (filename, mode: :cover:`~lang/types Char` *) -> :cover:`~lang/stdio FILE` *
    
.. function:: fread (ptr: :cover:`~lang/types Pointer` , size, count: :cover:`~lang/types SizeT` , stream: :cover:`~lang/stdio FILE` *) -> :cover:`~lang/types SizeT` 
    
.. function:: feof (stream: :cover:`~lang/stdio FILE` *) -> :cover:`~lang/types Int` 
    
.. function:: fseek (stream: :cover:`~lang/stdio FILE` *, offset: :cover:`~lang/types Long` , origin: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: SEEK_CUR
    
.. function:: SEEK_SET
    
.. function:: SEEK_END
    
.. function:: ftell (stream: :cover:`~lang/stdio FILE` *) -> :cover:`~lang/types Long` 
    
.. class:: FileReader
    
    :extends: :class:`~io/Reader Reader` 
    .. staticmemberfunction:: new~withFile (fileObject: :class:`~io/File File` ) -> :class:`~io/FileReader FileReader` 
        
    .. memberfunction:: init~withFile (fileObject: :class:`~io/File File` )
        
    .. staticmemberfunction:: new~withName (fileName: :cover:`~lang/types String` ) -> :class:`~io/FileReader FileReader` 
        
    .. memberfunction:: init~withName (fileName: :cover:`~lang/types String` )
        
    .. memberfunction:: read (chars: :cover:`~lang/types String` , offset, count: :cover:`~lang/types Int` ) -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: read~char -> :cover:`~lang/types Char` 
        
    .. memberfunction:: readLine -> :cover:`~lang/types String` 
        
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: rewind (offset: :cover:`~lang/types Int` )
        
    .. memberfunction:: mark -> :cover:`~lang/types Long` 
        
    .. memberfunction:: reset (marker: :cover:`~lang/types Long` )
        
    .. memberfunction:: close
        
    .. field:: file -> :cover:`~lang/stdio FILE` *
    
