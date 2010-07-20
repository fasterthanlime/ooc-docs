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
    
    :from: ``mode_t``
.. cover:: FileStat
    
    :from: ``struct stat``
.. class:: FileUnix
    
    :extends: :class:`~io/File File` 
    .. staticmethod:: new~unix (path: :cover:`~lang/types String` ) -> :class:`~io/native/FileUnix FileUnix` 
        
    .. method:: init~unix (path: :cover:`~lang/types String` )
        
    .. method:: isDir -> :cover:`~lang/types Bool` 
        
        @return true if it's a directory
        
        
    .. method:: isFile -> :cover:`~lang/types Bool` 
        
        @return true if it's a file (ie. not a directory nor a symbolic link)
        
        
    .. method:: isLink -> :cover:`~lang/types Bool` 
        
        @return true if the file is a symbolic link
        
        
    .. method:: size -> :cover:`~lang/types LLong` 
        
        @return the size of the file, in bytes
        
        
    .. method:: ownerPerm -> :cover:`~lang/types Int` 
        
        @return the permissions for the owner of this file
        
        
    .. method:: groupPerm -> :cover:`~lang/types Int` 
        
        @return the permissions for the group of this file
        
        
    .. method:: otherPerm -> :cover:`~lang/types Int` 
        
        @return the permissions for the others (not owner, not group)
        
        
    .. method:: lastAccessed -> :cover:`~lang/types Long` 
        
        @return the time of last access, or -1 if it doesn't exist
        
        
    .. method:: lastModified -> :cover:`~lang/types Long` 
        
        @return the time of last modification, or -1 if it doesn't exist
        
        
    .. method:: created -> :cover:`~lang/types Long` 
        
        @return the time of creation, or -1 if it doesn't exist
        
        
    .. method:: isRelative -> :cover:`~lang/types Bool` 
        
        @return true if the function is relative to the current directory
        
        
    .. method:: getAbsolutePath -> :cover:`~lang/types String` 
        
        The absolute path, e.g. "my/dir" => "/current/directory/my/dir"
        
        
    .. method:: getAbsoluteFile -> :class:`~io/File File` 
        
        A file corresponding to the absolute path
        @see getAbsolutePath
        
        
    .. method:: getChildrenNames -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. method:: getChildren -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. method:: mkdir~withMode (mode: :cover:`~lang/types Int32` ) -> :cover:`~lang/types Int` 
        
