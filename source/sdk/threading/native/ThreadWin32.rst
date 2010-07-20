threading/native/ThreadWin32
============================

.. module:: threading/native/ThreadWin32

.. function:: CreateThread (...) -> :cover:`~threading/native/ThreadWin32 Handle` 
    
.. function:: WaitForSingleObject (...) -> :cover:`~lang/types Long` 
    
.. cover:: Handle
    
    :from: ``HANDLE``
.. class:: ThreadWin32
    
    :extends: :class:`~threading/Thread Thread` 
    .. staticmethod:: new~win (runnable: :class:`~threading/Runnable Runnable` ) -> :class:`~threading/native/ThreadWin32 ThreadWin32` 
        
    .. method:: init~win (runnable: :class:`~threading/Runnable Runnable` )
        
    .. method:: start -> :cover:`~lang/types Int` 
        
    .. method:: wait -> :cover:`~lang/types Int` 
        
    .. field:: handle -> :cover:`~threading/native/ThreadWin32 Handle` 
    
    .. field:: threadID -> :cover:`~lang/types Long` 
    
.. var:: INVALID_HANDLE_VALUE -> :cover:`~threading/native/ThreadWin32 Handle` 

.. var:: WAIT_OBJECT_0 -> :cover:`~lang/types Long` 

.. var:: INFINITE -> :cover:`~lang/types Long` 

