os/Env
======

.. module:: os/Env

.. function:: getenv (path: String) -> String
    
.. function:: setenv (key, value: String, overwrite: Bool) -> Int
    
.. function:: unsetenv (key: String) -> Int
    
.. function:: putenv (str: String) -> Int
    
.. class:: Env
    
    .. staticmemberfunction:: new -> Env
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: get (variableName: String) -> String
        
    .. staticmemberfunction:: set (key, value: String, overwrite: Bool) -> Int
        
    .. staticmemberfunction:: set~overwrite (key, value: String) -> Int
        
    .. staticmemberfunction:: unset (key: String) -> Int
        
