net/StreamSocket
================

.. module:: net/StreamSocket

.. class:: StreamSocket
    
    :extends: :class:`~net/Socket Socket` 
    .. staticmethod:: new~addr (remote: :class:`~net/Address SocketAddress` ) -> :class:`~net/StreamSocket StreamSocket` 
        
    .. method:: init~addr (remote: :class:`~net/Address SocketAddress` )
        
    .. staticmethod:: new~addrDescriptor (remote: :class:`~net/Address SocketAddress` , descriptor: :cover:`~lang/types Int` ) -> :class:`~net/StreamSocket StreamSocket` 
        
    .. method:: init~addrDescriptor (remote: :class:`~net/Address SocketAddress` , descriptor: :cover:`~lang/types Int` )
        
    .. staticmethod:: new~hostAndPort (host: :cover:`~lang/types String` , port: :cover:`~lang/types Int` ) -> :class:`~net/StreamSocket StreamSocket` 
        
    .. method:: init~hostAndPort (host: :cover:`~lang/types String` , port: :cover:`~lang/types Int` )
        
    .. staticmethod:: new~family (host: :cover:`~lang/types String` , port, family: :cover:`~lang/types Int` ) -> :class:`~net/StreamSocket StreamSocket` 
        
    .. method:: init~family (host: :cover:`~lang/types String` , port, family: :cover:`~lang/types Int` )
        
    .. method:: connect
        
    .. method:: reader -> :class:`~net/StreamSocket StreamSocketReader` 
        
    .. method:: writer -> :class:`~net/StreamSocket StreamSocketWriter` 
        
    .. method:: send~withLength (data: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` , flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. method:: send~withFlags (data: :cover:`~lang/types String` , flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. method:: send (data: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
    .. method:: sendByte~withFlags (byte: :cover:`~lang/types Char` , flags: :cover:`~lang/types Int` )
        
    .. method:: sendByte (byte: :cover:`~lang/types Char` )
        
    .. method:: receive~withFlags (buffer: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` , flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. method:: receive (buffer: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Int` 
        
    .. method:: receiveByte~withFlags (flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Char` 
        
    .. method:: receiveByte -> :cover:`~lang/types Char` 
        
    .. field:: remote -> :class:`~net/Address SocketAddress` 
    
.. class:: StreamSocketReader
    
    :extends: :class:`~io/Reader Reader` 
    .. staticmethod:: new (source: :class:`~net/StreamSocket StreamSocket` ) -> :class:`~net/StreamSocket StreamSocketReader` 
        
    .. method:: init (source: :class:`~net/StreamSocket StreamSocket` )
        
    .. method:: read (chars: :cover:`~lang/types String` , offset, count: :cover:`~lang/types Int` ) -> :cover:`~lang/types SizeT` 
        
    .. method:: read~char -> :cover:`~lang/types Char` 
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: rewind (offset: :cover:`~lang/types Int` )
        
    .. method:: mark -> :cover:`~lang/types Long` 
        
    .. method:: reset (marker: :cover:`~lang/types Long` )
        
    .. field:: source -> :class:`~net/StreamSocket StreamSocket` 
    
.. class:: StreamSocketWriter
    
    :extends: :class:`~io/Writer Writer` 
    .. staticmethod:: new (dest: :class:`~net/StreamSocket StreamSocket` ) -> :class:`~net/StreamSocket StreamSocketWriter` 
        
    .. method:: init (dest: :class:`~net/StreamSocket StreamSocket` )
        
    .. method:: close
        
    .. method:: write~chr (chr: :cover:`~lang/types Char` )
        
    .. method:: write (chars: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types SizeT` 
        
    .. field:: dest -> :class:`~net/StreamSocket StreamSocket` 
    
