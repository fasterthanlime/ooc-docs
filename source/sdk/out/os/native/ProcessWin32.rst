os/native/ProcessWin32
======================

.. module:: os/native/ProcessWin32

.. function:: ZeroMemory (:cover:`~lang/types Pointer` , :cover:`~lang/types SizeT` )
    
.. function:: CreateProcess (...) -> :cover:`~lang/types Bool` 
    
.. function:: WaitForSingleObject (...)
    
.. function:: GetExitCodeProcess (...) -> :cover:`~lang/types Int` 
    
.. function:: CloseHandle (:cover:`~native/win32/types Handle` )
    
.. cover:: StartupInfo
    
    :from: ``STARTUPINFO``
.. cover:: ProcessInformation
    
    :from: ``PROCESS_INFORMATION``
.. class:: ProcessWin32
    
    :extends: :class:`~os/Process Process` 
    .. staticmethod:: new~win32 (args: :class:`~structs/ArrayList ArrayList<T>` ) -> :class:`~os/native/ProcessWin32 ProcessWin32` 
        
    .. method:: init~win32 (args: :class:`~structs/ArrayList ArrayList<T>` )
        
    .. method:: wait -> :cover:`~lang/types Int` 
        
        Wait for the process to end. Bad things will happen if you haven't called `executeNoWait` before.
        
    .. method:: executeNoWait
        
        Execute the process without waiting for it to end. You have to call `wait` manually.
        
    .. field:: si -> :cover:`~os/native/ProcessWin32 StartupInfo` 
    
    .. field:: pi -> :cover:`~os/native/ProcessWin32 ProcessInformation` 
    
    .. field:: cmdLine -> :cover:`~lang/types String` 
    
.. var:: INFINITE -> :cover:`~lang/types Long` 

.. var:: WAIT_OBJECT_0 -> :cover:`~lang/types Long` 

