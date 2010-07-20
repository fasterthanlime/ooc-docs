threading/Mutex
===============

.. module:: threading/Mutex

.. class:: Mutex
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new (recursive: :cover:`~lang/types Bool` ) -> :class:`~threading/Mutex Mutex` 
        
        Create a new mutex object.
        
        :recursive: if true this mutex will allow for recursive locking in the same thread
        
        
    .. staticmethod:: new~fast -> :class:`~threading/Mutex Mutex` 
        
        Create a new mutex object. Non-recursive, fast.
        
        
    .. method:: acquire
        
        Acquire a lock on the mutex and blocking until it becomes available.
        
        
    .. method:: tryAcquire -> :cover:`~lang/types Bool` 
        
        Try to acquire a lock on the mutex, but does not block if unavailable.
        
        :return: true if mutex successfully locked, false if not available
        
        
    .. method:: release
        
        Release the lock on the mutex so other threads can acquire it.
        
        
