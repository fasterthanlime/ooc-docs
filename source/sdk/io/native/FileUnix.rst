io/native/FileUnix
==================

.. module:: io/native/FileUnix

.. function:: realpath (path, resolved: String) -> String
    
.. function:: _getcwd (buf: String, size: SizeT) -> String
    
.. function:: S_ISDIR (...) -> Bool
    
.. function:: S_ISREG (...) -> Bool
    
.. function:: S_ISLNK (...) -> Bool
    
.. function:: S_IRWXU (...)
    
.. function:: S_IRWXG (...)
    
.. function:: S_IRWXO (...)
    
.. function:: lstat (String, FileStat*) -> Int
    
.. function:: _mkdir (String, ModeT) -> Int
    
.. function:: remove (path: String) -> Int
    
.. function:: _remove (path: String) -> Int
    
.. cover:: ModeT
    
.. cover:: FileStat
    
.. class:: FileUnix
    
    .. staticmemberfunction:: new~unix (path: String) -> FileUnix
        
    .. memberfunction:: init~unix (path: String)
        
    .. memberfunction:: isDir -> Bool
        
        @return true if it's a directory
        
        
    .. memberfunction:: isFile -> Bool
        
        @return true if it's a file (ie. not a directory nor a symbolic link)
        
        
    .. memberfunction:: isLink -> Bool
        
        @return true if the file is a symbolic link
        
        
    .. memberfunction:: size -> LLong
        
        @return the size of the file, in bytes
        
        
    .. memberfunction:: ownerPerm -> Int
        
        @return the permissions for the owner of this file
        
        
    .. memberfunction:: groupPerm -> Int
        
        @return the permissions for the group of this file
        
        
    .. memberfunction:: otherPerm -> Int
        
        @return the permissions for the others (not owner, not group)
        
        
    .. memberfunction:: lastAccessed -> Long
        
        @return the time of last access
        
        
    .. memberfunction:: lastModified -> Long
        
        @return the time of last modification
        
        
    .. memberfunction:: created -> Long
        
        @return the time of creation
        
        
    .. memberfunction:: getAbsolutePath -> String
        
        The absolute path, e.g. "my/dir" => "/current/directory/my/dir"
        
        
    .. memberfunction:: getAbsoluteFile -> File
        
        A file corresponding to the absolute path
        @see getAbsolutePath
        
        
    .. memberfunction:: getChildrenNames -> ArrayList<T>
        
    .. memberfunction:: getChildren -> ArrayList<T>
        
    .. memberfunction:: mkdir~withMode (mode: Int32) -> Int
        
