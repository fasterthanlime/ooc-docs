os/Process
==========

.. module:: os/Process

.. class:: Process
    
    .. memberfunction:: new (args: ArrayList<T>) -> Process
        
    
    .. memberfunction:: init (args: ArrayList<T>)
        
    
    .. memberfunction:: new~withEnv (args: ArrayList<T>, env: HashMap<T>) -> Process
        
    
    .. memberfunction:: init~withEnv (args: ArrayList<T>, env: HashMap<T>)
        
    
    .. memberfunction:: setStdout (stdOut: Pipe)
        
    
    .. memberfunction:: setStdin (stdIn: Pipe)
        
    
    .. memberfunction:: setStderr (stdErr: Pipe)
        
    
    .. memberfunction:: setEnv (env: HashMap<T>)
        
    
    .. memberfunction:: setCwd (cwd: String)
        
    
    .. memberfunction:: execute -> Int
        
    
    .. memberfunction:: wait -> Int
        
        Wait for the process to end. Bad things will happen if you haven't called `executeNoWait` before. 
        
    
    .. memberfunction:: executeNoWait
        
        Execute the process without waiting for it to end. You have to call `wait` manually. 
        
    
    .. memberfunction:: getOutput -> String
        
        Execute the process, and return all the output to stdout
        as a string
        
        
    
    .. memberfunction:: getErrOutput -> String
        
        Execute the process, and return all the output to stderr
        as a string
        
        
    
    .. memberfunction:: communicate (data: String, stdoutData, stderrData: String*) -> Int
        
        Send `data` to the process, wait for the process to end and get the
        stdout and stderr data. You have to do `setStdIn(Pipe new())`/
        `setStdOut(Pipe new())`/`setStdErr(Pipe new())`
        before in order to send / get the data. You have to run `executeNoWait` before.
        You can pass null as data, stdoutData or stderrData.
        
        
    
    .. field:: args
    
    .. field:: executable
    
    .. field:: stdOut
    
    .. field:: stdIn
    
    .. field:: stdErr
    
    .. field:: buf
    
    .. field:: stdoutPipe
    
    .. field:: env
    
    .. field:: cwd
    

