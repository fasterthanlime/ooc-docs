os/Process
==========

.. module:: os/Process

.. class:: Process
    
    .. staticmemberfunction:: new (args: ArrayList<T>) -> Process
        
    .. staticmemberfunction:: new~withEnv (args: ArrayList<T>, env: HashMap<T>) -> Process
        
    .. memberfunction:: setStdout (stdOut: Pipe)
        
    .. memberfunction:: setStdin (stdIn: Pipe)
        
    .. memberfunction:: setStderr (stdErr: Pipe)
        
    .. memberfunction:: setEnv (env: HashMap<T>)
        
    .. memberfunction:: setCwd (cwd: String)
        
    .. memberfunction:: execute -> Int
        
        Execute the process and wait for it to end 
        
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
        
        
    .. field:: args -> ArrayList<T>
    
    .. field:: executable -> String
    
    .. field:: stdOut -> Pipe
    
    .. field:: stdIn -> Pipe
    
    .. field:: stdErr -> Pipe
    
    .. field:: buf -> String*
    
    .. field:: env -> HashMap<T>
    
    .. field:: cwd -> String
    
