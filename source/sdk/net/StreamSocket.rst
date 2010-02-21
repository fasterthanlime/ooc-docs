net/StreamSocket
================

.. module:: net/StreamSocket

.. class:: StreamSocket
    
    :extends: :class:`~net/Socket Socket` 
    .. staticmemberfunction:: new~addr (remote: :class:`~net/Address SocketAddress` ) -> :class:`~net/StreamSocket StreamSocket` 
        
    .. memberfunction:: init~addr (remote: :class:`~net/Address SocketAddress` )
        
    .. staticmemberfunction:: new~hostAndPort (host: :cover:`~lang/types String` , port: :cover:`~lang/types Int` ) -> :class:`~net/StreamSocket StreamSocket` 
        
    .. memberfunction:: init~hostAndPort (host: :cover:`~lang/types String` , port: :cover:`~lang/types Int` )
        
    .. staticmemberfunction:: new~family (host: :cover:`~lang/types String` , port, family: :cover:`~lang/types Int` ) -> :class:`~net/StreamSocket StreamSocket` 
        
    .. memberfunction:: init~family (host: :cover:`~lang/types String` , port, family: :cover:`~lang/types Int` )
        
    .. memberfunction:: connect
        
    .. memberfunction:: reader -> :class:`~net/StreamSocket StreamSocketReader` 
        
    .. memberfunction:: writer -> :class:`~net/StreamSocket StreamSocketWriter` 
        
    .. memberfunction:: send~withLength (data: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` , flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: send~withFlags (data: :cover:`~lang/types String` , flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: send (data: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: sendByte~withFlags (byte: :cover:`~lang/types Char` , flags: :cover:`~lang/types Int` )
        
    .. memberfunction:: sendByte (byte: :cover:`~lang/types Char` )
        
    .. memberfunction:: receive~withFlags (buffer: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` , flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: receive (buffer: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: receiveByte~withFlags (flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Char` 
        
    .. memberfunction:: receiveByte -> :cover:`~lang/types Char` 
        
    .. field:: remote -> :class:`~net/Address SocketAddress` 
    
.. class:: StreamSocketReader
    
    :extends: :class:`~io/Reader Reader` 
    .. staticmemberfunction:: new (source: :class:`~net/StreamSocket StreamSocket` ) -> :class:`~net/StreamSocket StreamSocketReader` 
        
    .. memberfunction:: init (source: :class:`~net/StreamSocket StreamSocket` )
        
    .. memberfunction:: read (chars: :cover:`~lang/types String` , offset, count: :cover:`~lang/types Int` ) -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: read~char -> :cover:`~lang/types Char` 
        
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: rewind (offset: :cover:`~lang/types Int` )
        
    .. memberfunction:: mark -> :cover:`~lang/types Long` 
        
    .. memberfunction:: reset (marker: :cover:`~lang/types Long` )
        
    .. field:: source -> :class:`~net/StreamSocket StreamSocket` 
    
.. class:: StreamSocketWriter
    
    :extends: :class:`~io/Writer Writer` 
    .. staticmemberfunction:: new (dest: :class:`~net/StreamSocket StreamSocket` ) -> :class:`~net/StreamSocket StreamSocketWriter` 
        
    .. memberfunction:: init (dest: :class:`~net/StreamSocket StreamSocket` )
        
    .. memberfunction:: close
        
    .. memberfunction:: write~chr (chr: :cover:`~lang/types Char` )
        
    .. memberfunction:: write (chars: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types SizeT` 
        
    .. field:: dest -> :class:`~net/StreamSocket StreamSocket` 
    
