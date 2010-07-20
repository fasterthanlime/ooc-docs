net/ServerSocket
================

.. module:: net/ServerSocket

.. class:: ServerSocket
    
    :extends: :class:`~net/Socket Socket` 
    .. staticmethod:: new -> :class:`~net/ServerSocket ServerSocket` 
        
    .. method:: init
        
    .. method:: bind (port: :cover:`~lang/types Int` )
        
        Bind a local port to the socket.
        
        
    .. method:: bind~withAddr (addr: :class:`~net/Address SocketAddress` )
        
        Bind a local address to the socket.
        
        
    .. method:: listen (backlog: :cover:`~lang/types Int` )
        
        Places the socket into a listening state.
        
        
    .. method:: accept -> :class:`~net/StreamSocket StreamSocket` 
        
        Accept an incoming connection and returns it.
        
        This method will normally block if no connection is
        available immediately.
        
        
