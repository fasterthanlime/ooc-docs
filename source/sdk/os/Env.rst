os/Env
======

.. module:: os/Env

.. function:: getenv (path: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
    
.. function:: setenv (key, value: :cover:`~lang/types String` , overwrite: :cover:`~lang/types Bool` ) -> :cover:`~lang/types Int` 
    
.. function:: unsetenv (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
    
.. function:: putenv (str: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
    
.. class:: Env
    
    .. staticmemberfunction:: new -> :class:`~os/Env Env` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: get (variableName: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
    .. staticmemberfunction:: set (key, value: :cover:`~lang/types String` , overwrite: :cover:`~lang/types Bool` ) -> :cover:`~lang/types Int` 
        
    .. staticmemberfunction:: set~overwrite (key, value: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
    .. staticmemberfunction:: unset (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
