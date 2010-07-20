threading/native/ThreadUnix
===========================

.. module:: threading/native/ThreadUnix

.. function:: pthread_create (...) -> :cover:`~lang/types Int` 
    
.. function:: pthread_join (...) -> :cover:`~lang/types Int` 
    
.. cover:: PThread
    
    :from: ``pthread_t``
.. class:: ThreadUnix
    
    :extends: :class:`~threading/Thread Thread` 
    .. staticmethod:: new~unix (runnable: :class:`~threading/Runnable Runnable` ) -> :class:`~threading/native/ThreadUnix ThreadUnix` 
        
    .. method:: init~unix (runnable: :class:`~threading/Runnable Runnable` )
        
    .. method:: start -> :cover:`~lang/types Int` 
        
    .. method:: wait -> :cover:`~lang/types Int` 
        
    .. field:: pthread -> :cover:`~threading/native/ThreadUnix PThread` 
    
