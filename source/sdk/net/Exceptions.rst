net/Exceptions
==============

.. module:: net/Exceptions

.. function:: strerror (:cover:`~lang/types Int` ) -> :cover:`~lang/types String` 
    
.. class:: NetError
    
    :extends: :class:`~lang/types Exception` 
    .. staticmemberfunction:: new -> :class:`~net/Exceptions NetError` 
        
    .. memberfunction:: init
        
.. class:: InvalidAddress
    
    :extends: :class:`~net/Exceptions NetError` 
    .. staticmemberfunction:: new -> :class:`~net/Exceptions InvalidAddress` 
        
    .. memberfunction:: init
        
.. class:: DNSError
    
    :extends: :class:`~net/Exceptions NetError` 
    .. staticmemberfunction:: new -> :class:`~net/Exceptions DNSError` 
        
    .. memberfunction:: init
        
.. class:: SocketError
    
    :extends: :class:`~net/Exceptions NetError` 
    .. staticmemberfunction:: new -> :class:`~net/Exceptions SocketError` 
        
    .. memberfunction:: init
        
.. var:: errno -> :cover:`~lang/types Int` 

