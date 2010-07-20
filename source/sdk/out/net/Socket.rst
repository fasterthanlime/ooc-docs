net/Socket
==========

.. module:: net/Socket

.. class:: Socket
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new~sock (family, type, protocol: :cover:`~lang/types Int` ) -> :class:`~net/Socket Socket` 
        
    .. method:: init~sock (family, type, protocol: :cover:`~lang/types Int` )
        
    .. staticmethod:: new~descriptor (family, type, protocol, descriptor: :cover:`~lang/types Int` ) -> :class:`~net/Socket Socket` 
        
    .. method:: init~descriptor (family, type, protocol, descriptor: :cover:`~lang/types Int` )
        
    .. method:: close
        
    .. method:: ioctl (request: :cover:`~lang/types Int` , arg: :cover:`~lang/types Pointer` )
        
    .. method:: available -> :cover:`~lang/types Int` 
        
    .. field:: descriptor -> :cover:`~lang/types Int` 
    
    .. field:: family -> :cover:`~lang/types Int` 
    
    .. field:: type -> :cover:`~lang/types Int` 
    
    .. field:: protocol -> :cover:`~lang/types Int` 
    
.. cover:: SocketFamily
    
.. cover:: SocketType
    
.. cover:: SocketMsgFlags
    
