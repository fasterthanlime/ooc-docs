io/native/FileWin32
===================

.. module:: io/native/FileWin32

.. function:: FindFirstFile (:cover:`~lang/types String` , :cover:`~io/native/FileWin32 FindData` *) -> :cover:`~native/win32/types Handle` 
    
.. function:: FindNextFile (:cover:`~native/win32/types Handle` , :cover:`~io/native/FileWin32 FindData` *) -> :cover:`~lang/types Bool` 
    
.. function:: FindClose (:cover:`~native/win32/types Handle` )
    
.. function:: GetFileAttributes (:cover:`~lang/types String` ) -> :cover:`~lang/types Long` 
    
.. function:: CreateDirectory (:cover:`~lang/types String` , :cover:`~lang/types Pointer` ) -> :cover:`~lang/types Bool` 
    
.. function:: _remove (path: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
    
.. cover:: FindData
    
.. class:: FileWin32
    
    .. staticmemberfunction:: new~win32 (path: :cover:`~lang/types String` ) -> :class:`~io/native/FileWin32 FileWin32` 
        
    .. memberfunction:: init~win32 (path: :cover:`~lang/types String` )
        
    .. memberfunction:: exists -> :cover:`~lang/types Bool` 
        
        @return true if the file exists and can be
        opened for reading
        
        
    .. memberfunction:: findSingle (ffdPtr: :cover:`~io/native/FileWin32 FindData` *)
        
    .. memberfunction:: findFirst (ffdPtr: :cover:`~io/native/FileWin32 FindData` *) -> :cover:`~native/win32/types Handle` 
        
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
        
        
    .. memberfunction:: mkdir~withMode (mode: :cover:`~lang/types Int32` ) -> :cover:`~lang/types Int` 
        
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
        
        
    .. memberfunction:: getChildrenNames -> :class:`~structs/ArrayList ArrayList<T>` 
        
        List the name of the children of this path
        Works only on directories, obviously
        
        
    .. memberfunction:: getChildren -> :class:`~structs/ArrayList ArrayList<T>` 
        
        List the children of this path
        Works only on directories, obviously
        
        
.. var:: FILE_ATTRIBUTE_DIRECTORY -> :cover:`~lang/types Long` 

.. var:: FILE_ATTRIBUTE_REPARSE_POINT -> :cover:`~lang/types Long` 

.. var:: FILE_ATTRIBUTE_NORMAL -> :cover:`~lang/types Long` 

