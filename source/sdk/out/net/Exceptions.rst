net/Exceptions
==============

.. module:: net/Exceptions

.. function:: strerror (:cover:`~lang/types Int` ) -> :cover:`~lang/types String` 
    
.. class:: NetError
    
    :extends: :class:`~lang/types Exception` 
    .. staticmethod:: new -> :class:`~net/Exceptions NetError` 
        
    .. method:: init
        
.. class:: InvalidAddress
    
    :extends: :class:`~net/Exceptions NetError` 
    .. staticmethod:: new -> :class:`~net/Exceptions InvalidAddress` 
        
    .. method:: init
        
.. class:: DNSError
    
    :extends: :class:`~net/Exceptions NetError` 
    .. staticmethod:: new -> :class:`~net/Exceptions DNSError` 
        
    .. method:: init
        
.. class:: SocketError
    
    :extends: :class:`~net/Exceptions NetError` 
    .. staticmethod:: new -> :class:`~net/Exceptions SocketError` 
        
    .. method:: init
        
.. var:: errno -> :cover:`~lang/types Int` 

