io/Writer
=========

.. module:: io/Writer

.. class:: Writer
    
    :extends: :class:`~lang/types Object` 
    .. method:: close
        
    .. method:: write~chr (chr: :cover:`~lang/types Char` )
        
    .. method:: write (chars: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types SizeT` 
        
    .. method:: write~implicitLength (chars: :cover:`~lang/types String` ) -> :cover:`~lang/types SizeT` 
        
    .. method:: write~fromReader (source: :class:`~io/Reader Reader` , bufferSize: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types SizeT` 
        
        Copies data from a Reader into this Writer.
        
        :param bufferSize: size in bytes of the internal transfer buffer
        :return: total bytes transfered
        
        
    .. method:: write~fromReaderDefaultBufferSize (source: :class:`~io/Reader Reader` )
        
        Same as write(source, bufferSize) except uses a default buffer size of 8192 bytes.
        
        
