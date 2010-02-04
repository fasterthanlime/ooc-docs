os/Env
======

.. module:: os/Env

.. function:: getenv (path: String) -> String
    

.. function:: setenv (key, value: String, overwrite: Bool) -> Int
    

.. function:: unsetenv (key: String) -> Int
    

.. function:: putenv (str: String) -> Int
    

.. class:: Env
    
    .. memberfunction:: new -> Env
        
    
    .. memberfunction:: init
        
    
    .. memberfunction:: get (variableName: String) -> String
        
    
    .. memberfunction:: set (key, value: String, overwrite: Bool) -> Int
        
    
    .. memberfunction:: set~overwrite (key, value: String) -> Int
        
    
    .. memberfunction:: unset (key: String) -> Int
        
    

