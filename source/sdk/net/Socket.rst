net/Socket
==========

.. module:: net/Socket

.. class:: Socket
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new (family, type, protocol: :cover:`~lang/types Int` ) -> :class:`~net/Socket Socket` 
        
    .. memberfunction:: init (family, type, protocol: :cover:`~lang/types Int` )
        
    .. memberfunction:: close
        
    .. memberfunction:: ioctl (request: :cover:`~lang/types Int` , arg: :cover:`~lang/types Pointer` )
        
    .. memberfunction:: available -> :cover:`~lang/types Int` 
        
    .. field:: descriptor -> :cover:`~lang/types Int` 
    
    .. field:: family -> :cover:`~lang/types Int` 
    
    .. field:: type -> :cover:`~lang/types Int` 
    
    .. field:: protocol -> :cover:`~lang/types Int` 
    
.. cover:: SocketFamily
    
.. cover:: SocketType
    
.. cover:: SocketMsgFlags
    
