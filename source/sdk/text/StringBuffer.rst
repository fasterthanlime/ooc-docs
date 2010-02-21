text/StringBuffer
=================

.. module:: text/StringBuffer

.. class:: Buffer
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new -> :class:`~text/StringBuffer Buffer` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withCapa (capacity: :cover:`~lang/types SizeT` ) -> :class:`~text/StringBuffer Buffer` 
        
    .. memberfunction:: init~withCapa (capacity: :cover:`~lang/types SizeT` )
        
    .. staticmemberfunction:: new~withContent (data: :cover:`~lang/types String` ) -> :class:`~text/StringBuffer Buffer` 
        
    .. memberfunction:: init~withContent (data: :cover:`~lang/types String` )
        
    .. memberfunction:: append~str (str: :cover:`~lang/types String` )
        
    .. memberfunction:: append~strWithLength (str: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` )
        
    .. memberfunction:: append~chr (chr: :cover:`~lang/types Char` )
        
    .. memberfunction:: get~strWithLengthOffset (str: :cover:`~lang/types String` , offset, length: :cover:`~lang/types SizeT` )
        
    .. memberfunction:: get~chr (offset: :cover:`~lang/types Int` ) -> :cover:`~lang/types Char` 
        
    .. memberfunction:: checkLength (min: :cover:`~lang/types SizeT` )
        
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. field:: size -> :cover:`~lang/types SizeT` 
    
    .. field:: capacity -> :cover:`~lang/types SizeT` 
    
    .. field:: data -> :cover:`~lang/types String` 
    
.. class:: BufferWriter
    
    :extends: :class:`~io/Writer Writer` 
    .. staticmemberfunction:: new -> :class:`~text/StringBuffer BufferWriter` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withBuffer (buffer: :class:`~text/StringBuffer Buffer` ) -> :class:`~text/StringBuffer BufferWriter` 
        
    .. memberfunction:: init~withBuffer (buffer: :class:`~text/StringBuffer Buffer` )
        
    .. memberfunction:: buffer -> :class:`~text/StringBuffer Buffer` 
        
    .. memberfunction:: close
        
    .. memberfunction:: write~chr (chr: :cover:`~lang/types Char` )
        
    .. memberfunction:: write (chars: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types SizeT` 
        
    .. field:: buffer -> :class:`~text/StringBuffer Buffer` 
    
.. class:: StringBuffer
    
    :extends: :class:`~text/StringBuffer BufferWriter` 
    .. staticmemberfunction:: new -> :class:`~text/StringBuffer StringBuffer` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withCapa (capacity: :cover:`~lang/types Int` ) -> :class:`~text/StringBuffer StringBuffer` 
        
    .. memberfunction:: init~withCapa (capacity: :cover:`~lang/types Int` )
        
    .. staticmemberfunction:: new~withContent (data: :cover:`~lang/types String` ) -> :class:`~text/StringBuffer StringBuffer` 
        
    .. memberfunction:: init~withContent (data: :cover:`~lang/types String` )
        
    .. memberfunction:: append~str (str: :cover:`~lang/types String` )
        
    .. memberfunction:: append~strWithLength (str: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` )
        
    .. memberfunction:: append~chr (chr: :cover:`~lang/types Char` )
        
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
.. class:: BufferReader
    
    :extends: :class:`~io/Reader Reader` 
    .. staticmemberfunction:: new -> :class:`~text/StringBuffer BufferReader` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withBuffer (buffer: :class:`~text/StringBuffer Buffer` ) -> :class:`~text/StringBuffer BufferReader` 
        
    .. memberfunction:: init~withBuffer (buffer: :class:`~text/StringBuffer Buffer` )
        
    .. memberfunction:: buffer -> :class:`~text/StringBuffer Buffer` 
        
    .. memberfunction:: read (chars: :cover:`~lang/types String` , offset, count: :cover:`~lang/types Int` ) -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: read~char -> :cover:`~lang/types Char` 
        
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: rewind (offset: :cover:`~lang/types Int` )
        
    .. memberfunction:: mark -> :cover:`~lang/types Long` 
        
    .. memberfunction:: reset (marker: :cover:`~lang/types Long` )
        
    .. field:: buffer -> :class:`~text/StringBuffer Buffer` 
    
