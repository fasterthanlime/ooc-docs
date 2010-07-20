os/native/ProcessUnix
=====================

.. module:: os/native/ProcessUnix

.. class:: ProcessUnix
    
    :extends: :class:`~os/Process Process` 
    .. staticmethod:: new~unix (args: :class:`~structs/ArrayList ArrayList<T>` ) -> :class:`~os/native/ProcessUnix ProcessUnix` 
        
    .. method:: init~unix (args: :class:`~structs/ArrayList ArrayList<T>` )
        
    .. method:: wait -> :cover:`~lang/types Int` 
        
        Wait for the process to end. Bad things will happen if you haven't called `executeNoWait` before.
        
    .. method:: executeNoWait
        
        Execute the process without waiting for it to end. You have to call `wait` manually.
        
