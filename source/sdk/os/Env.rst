os/Env
======

.. module:: os/Env

.. function:: getenv (path: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
    
.. function:: setenv (key, value: :cover:`~lang/types String` , overwrite: :cover:`~lang/types Bool` ) -> :cover:`~lang/types Int` 
    
.. function:: unsetenv (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
    
.. function:: putenv (str: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
    
.. class:: Env
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~os/Env Env` 
        
    .. method:: init
        
    .. staticmethod:: get (variableName: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
    .. staticmethod:: set (key, value: :cover:`~lang/types String` , overwrite: :cover:`~lang/types Bool` ) -> :cover:`~lang/types Int` 
        
    .. staticmethod:: set~overwrite (key, value: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
    .. staticmethod:: unset (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
