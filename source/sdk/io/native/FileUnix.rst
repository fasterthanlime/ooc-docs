io/native/FileUnix
==================

.. module:: io/native/FileUnix

.. function:: realpath (path, resolved: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
    
.. function:: _getcwd (buf: :cover:`~lang/types String` , size: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types String` 
    
.. function:: S_ISDIR (...) -> :cover:`~lang/types Bool` 
    
.. function:: S_ISREG (...) -> :cover:`~lang/types Bool` 
    
.. function:: S_ISLNK (...) -> :cover:`~lang/types Bool` 
    
.. function:: S_IRWXU (...)
    
.. function:: S_IRWXG (...)
    
.. function:: S_IRWXO (...)
    
.. function:: lstat (:cover:`~lang/types String` , :cover:`~io/native/FileUnix FileStat` *) -> :cover:`~lang/types Int` 
    
.. function:: _mkdir (:cover:`~lang/types String` , :cover:`~io/native/FileUnix ModeT` ) -> :cover:`~lang/types Int` 
    
.. function:: remove (path: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
    
.. function:: _remove (path: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
    
.. cover:: ModeT
    
.. cover:: FileStat
    
.. class:: FileUnix
    
    .. staticmemberfunction:: new~unix (path: :cover:`~lang/types String` ) -> :class:`~io/native/FileUnix FileUnix` 
        
    .. memberfunction:: init~unix (path: :cover:`~lang/types String` )
        
    .. memberfunction:: isDir -> :cover:`~lang/types Bool` 
        
        @return true if it's a directory
        
        
    .. memberfunction:: isFile -> :cover:`~lang/types Bool` 
        
        @return true if it's a file (ie. not a directory nor a symbolic link)
        
        
    .. memberfunction:: isLink -> :cover:`~lang/types Bool` 
        
        @return true if the file is a symbolic link
        
        
    .. memberfunction:: size -> :cover:`~lang/types LLong` 
        
        @return the size of the file, in bytes
        
        
    .. memberfunction:: ownerPerm -> :cover:`~lang/types Int` 
        
        @return the permissions for the owner of this file
        
        
    .. memberfunction:: groupPerm -> :cover:`~lang/types Int` 
        
        @return the permissions for the group of this file
        
        
    .. memberfunction:: otherPerm -> :cover:`~lang/types Int` 
        
        @return the permissions for the others (not owner, not group)
        
        
    .. memberfunction:: lastAccessed -> :cover:`~lang/types Long` 
        
        @return the time of last access
        
        
    .. memberfunction:: lastModified -> :cover:`~lang/types Long` 
        
        @return the time of last modification
        
        
    .. memberfunction:: created -> :cover:`~lang/types Long` 
        
        @return the time of creation
        
        
    .. memberfunction:: isRelative -> :cover:`~lang/types Bool` 
        
        @return true if the function is relative to the current directory
        
        
    .. memberfunction:: getAbsolutePath -> :cover:`~lang/types String` 
        
        The absolute path, e.g. "my/dir" => "/current/directory/my/dir"
        
        
    .. memberfunction:: getAbsoluteFile -> :class:`~io/File File` 
        
        A file corresponding to the absolute path
        @see getAbsolutePath
        
        
    .. memberfunction:: getChildrenNames -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. memberfunction:: getChildren -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. memberfunction:: mkdir~withMode (mode: :cover:`~lang/types Int32` ) -> :cover:`~lang/types Int` 
        
