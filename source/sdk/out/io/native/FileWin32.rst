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
    
    :from: ``WIN32_FIND_DATA``
.. class:: FileWin32
    
    :extends: :class:`~io/File File` 
    .. staticmethod:: new~win32 (path: :cover:`~lang/types String` ) -> :class:`~io/native/FileWin32 FileWin32` 
        
    .. method:: init~win32 (path: :cover:`~lang/types String` )
        
    .. method:: exists -> :cover:`~lang/types Bool` 
        
        @return true if the file exists and can be
        opened for reading
        
        
    .. method:: findSingle (ffdPtr: :cover:`~io/native/FileWin32 FindData` *)
        
    .. method:: findFirst (ffdPtr: :cover:`~io/native/FileWin32 FindData` *) -> :cover:`~native/win32/types Handle` 
        
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
        
        
    .. method:: mkdir~withMode (mode: :cover:`~lang/types Int32` ) -> :cover:`~lang/types Int` 
        
    .. method:: lastAccessed -> :cover:`~lang/types Long` 
        
        @return the time of last access
        
        
    .. method:: lastModified -> :cover:`~lang/types Long` 
        
        @return the time of last modification
        
        
    .. method:: created -> :cover:`~lang/types Long` 
        
        @return the time of creation
        
        
    .. method:: isRelative -> :cover:`~lang/types Bool` 
        
        @return true if the function is relative to the current directory
        
        
    .. method:: getAbsolutePath -> :cover:`~lang/types String` 
        
        The absolute path, e.g. "my/dir" => "/current/directory/my/dir"
        
        
    .. method:: getChildrenNames -> :class:`~structs/ArrayList ArrayList<T>` 
        
        List the name of the children of this path
        Works only on directories, obviously
        
        
    .. method:: getChildren -> :class:`~structs/ArrayList ArrayList<T>` 
        
        List the children of this path
        Works only on directories, obviously
        
        
.. var:: FILE_ATTRIBUTE_DIRECTORY -> :cover:`~lang/types Long` 

.. var:: FILE_ATTRIBUTE_NORMAL -> :cover:`~lang/types Long` 

.. var:: FILE_ATTRIBUTE_REPARSE_POINT -> :cover:`~lang/types Long` 

