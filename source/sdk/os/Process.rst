os/Process
==========

.. module:: os/Process

.. class:: Process
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new (args: :class:`~structs/ArrayList ArrayList<T>` ) -> :class:`~os/Process Process` 
        
    .. staticmethod:: new~withEnv (args: :class:`~structs/ArrayList ArrayList<T>` , env: :class:`~structs/HashMap HashMap<K,V>` ) -> :class:`~os/Process Process` 
        
    .. method:: setStdout (stdOut: :class:`~os/Pipe Pipe` )
        
    .. method:: setStdin (stdIn: :class:`~os/Pipe Pipe` )
        
    .. method:: setStderr (stdErr: :class:`~os/Pipe Pipe` )
        
    .. method:: setEnv (env: :class:`~structs/HashMap HashMap<K,V>` )
        
    .. method:: setCwd (cwd: :cover:`~lang/types String` )
        
    .. method:: execute -> :cover:`~lang/types Int` 
        
        Execute the process and wait for it to end
        
    .. method:: wait -> :cover:`~lang/types Int` 
        
        Wait for the process to end. Bad things will happen if you haven't called `executeNoWait` before.
        
    .. method:: executeNoWait
        
        Execute the process without waiting for it to end. You have to call `wait` manually.
        
    .. method:: getOutput -> :cover:`~lang/types String` 
        
        Execute the process, and return all the output to stdout
        as a string, if the program exited normally.
        If there was an error (e.g. the return code wasn't 0), this function
        will return null
        
        
    .. method:: getErrOutput -> :cover:`~lang/types String` 
        
        Execute the process, and return all the output to stderr
        as a string
        
        
    .. method:: communicate (data: :cover:`~lang/types String` , stdoutData, stderrData: :cover:`~lang/types String` *) -> :cover:`~lang/types Int` 
        
        Send `data` to the process, wait for the process to end and get the
        stdout and stderr data. You have to do `setStdIn(Pipe new())`/
        `setStdOut(Pipe new())`/`setStdErr(Pipe new())`
        before in order to send / get the data. You have to run `executeNoWait` before.
        You can pass null as data, stdoutData or stderrData.
        
        
    .. field:: args -> :class:`~structs/ArrayList ArrayList<T>` 
    
    .. field:: executable -> :cover:`~lang/types String` 
    
    .. field:: stdOut -> :class:`~os/Pipe Pipe` 
    
    .. field:: stdIn -> :class:`~os/Pipe Pipe` 
    
    .. field:: stdErr -> :class:`~os/Pipe Pipe` 
    
    .. field:: buf -> :cover:`~lang/types String` *
    
    .. field:: env -> :class:`~structs/HashMap HashMap<K,V>` 
    
    .. field:: cwd -> :cover:`~lang/types String` 
    
