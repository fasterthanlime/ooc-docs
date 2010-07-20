text/Buffer
===========

.. module:: text/Buffer

.. class:: Buffer
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~text/Buffer Buffer` 
        
    .. method:: init
        
    .. staticmethod:: new~withCapa (capacity: :cover:`~lang/types SizeT` ) -> :class:`~text/Buffer Buffer` 
        
    .. method:: init~withCapa (capacity: :cover:`~lang/types SizeT` )
        
    .. staticmethod:: new~withContent (data: :cover:`~lang/types String` ) -> :class:`~text/Buffer Buffer` 
        
    .. method:: init~withContent (data: :cover:`~lang/types String` )
        
    .. method:: append~str (str: :cover:`~lang/types String` )
        
    .. method:: append~strWithLength (str: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` )
        
    .. method:: append~chr (chr: :cover:`~lang/types Char` )
        
    .. method:: get~strWithLengthOffset (str: :cover:`~lang/types String` , offset, length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Int` 
        
    .. method:: get~chr (offset: :cover:`~lang/types Int` ) -> :cover:`~lang/types Char` 
        
    .. method:: checkLength (min: :cover:`~lang/types SizeT` )
        
    .. method:: toString -> :cover:`~lang/types String` 
        
    .. field:: size -> :cover:`~lang/types SizeT` 
    
    .. field:: capacity -> :cover:`~lang/types SizeT` 
    
    .. field:: data -> :cover:`~lang/types String` 
    
.. class:: BufferWriter
    
    :extends: :class:`~io/Writer Writer` 
    .. staticmethod:: new -> :class:`~text/Buffer BufferWriter` 
        
    .. method:: init
        
    .. staticmethod:: new~withBuffer (buffer: :class:`~text/Buffer Buffer` ) -> :class:`~text/Buffer BufferWriter` 
        
    .. method:: init~withBuffer (buffer: :class:`~text/Buffer Buffer` )
        
    .. method:: buffer -> :class:`~text/Buffer Buffer` 
        
    .. method:: close
        
    .. method:: write~chr (chr: :cover:`~lang/types Char` )
        
    .. method:: write (chars: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types SizeT` 
        
    .. field:: buffer -> :class:`~text/Buffer Buffer` 
    
.. class:: BufferReader
    
    :extends: :class:`~io/Reader Reader` 
    .. staticmethod:: new -> :class:`~text/Buffer BufferReader` 
        
    .. method:: init
        
    .. staticmethod:: new~withBuffer (buffer: :class:`~text/Buffer Buffer` ) -> :class:`~text/Buffer BufferReader` 
        
    .. method:: init~withBuffer (buffer: :class:`~text/Buffer Buffer` )
        
    .. method:: buffer -> :class:`~text/Buffer Buffer` 
        
    .. method:: read (chars: :cover:`~lang/types String` , offset, count: :cover:`~lang/types Int` ) -> :cover:`~lang/types SizeT` 
        
    .. method:: read~char -> :cover:`~lang/types Char` 
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: rewind (offset: :cover:`~lang/types Int` )
        
    .. method:: mark -> :cover:`~lang/types Long` 
        
    .. method:: reset (marker: :cover:`~lang/types Long` )
        
    .. field:: buffer -> :class:`~text/Buffer Buffer` 
    
