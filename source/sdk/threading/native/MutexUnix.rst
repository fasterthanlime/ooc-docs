threading/native/MutexUnix
==========================

.. module:: threading/native/MutexUnix

.. function:: pthread_mutexattr_init (...) -> :cover:`~lang/types Int` 
    
.. function:: pthread_mutexattr_destroy (...) -> :cover:`~lang/types Int` 
    
.. function:: pthread_mutexattr_settype (...) -> :cover:`~lang/types Int` 
    
.. function:: pthread_mutex_init (...) -> :cover:`~lang/types Int` 
    
.. function:: pthread_mutex_destroy (...) -> :cover:`~lang/types Int` 
    
.. function:: pthread_mutex_lock (...) -> :cover:`~lang/types Int` 
    
.. function:: pthread_mutex_trylock (...) -> :cover:`~lang/types Int` 
    
.. function:: pthread_mutex_unlock (...) -> :cover:`~lang/types Int` 
    
.. cover:: PThreadMutexAttr
    
    :from: ``pthread_mutexattr_t``
    PThread Mutex Attribute cover
    
.. cover:: PThreadMutex
    
    :from: ``pthread_mutex_t``
    PThread Mutex cover
    
.. class:: MutexUnix
    
    :extends: :class:`~threading/Mutex Mutex` 
    .. staticmethod:: new (recursive: :cover:`~lang/types Bool` ) -> :class:`~threading/native/MutexUnix MutexUnix` 
        
    .. method:: init (recursive: :cover:`~lang/types Bool` )
        
    .. method:: acquire
        
    .. method:: tryAcquire -> :cover:`~lang/types Bool` 
        
    .. method:: release
        
    .. field:: mutex -> :cover:`~threading/native/MutexUnix PThreadMutex` 
    
.. var:: PTHREAD_MUTEX_RECURSIVE -> :cover:`~lang/types Int` 

.. var:: PTHREAD_MUTEX_NORMAL -> :cover:`~lang/types Int` 

