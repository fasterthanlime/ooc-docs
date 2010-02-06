io/native/FileWin32
===================

.. module:: io/native/FileWin32

.. function:: FindFirstFile (String, FindData*) -> Handle
    
.. function:: FindNextFile (Handle, FindData*) -> Bool
    
.. function:: FindClose (Handle)
    
.. function:: GetFileAttributes (String) -> Long
    
.. function:: CreateDirectory (String, Pointer) -> Bool
    
.. function:: _remove (path: String) -> Int
    
.. cover:: FindData
    
.. class:: FileWin32
    
    .. staticmemberfunction:: new~win32 (path: String) -> FileWin32
        
    .. memberfunction:: init~win32 (path: String)
        
    .. memberfunction:: exists -> Bool
        
        @return true if the file exists and can be
        opened for reading
        
        
    .. memberfunction:: findSingle (ffdPtr: FindData*)
        
    .. memberfunction:: findFirst (ffdPtr: FindData*) -> Handle
        
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
        
        
    .. memberfunction:: mkdir~withMode (mode: Int32) -> Int
        
    .. memberfunction:: lastAccessed -> Long
        
        @return the time of last access
        
        
    .. memberfunction:: lastModified -> Long
        
        @return the time of last modification
        
        
    .. memberfunction:: created -> Long
        
        @return the time of creation
        
        
    .. memberfunction:: isRelative -> Bool
        
        @return true if the function is relative to the current directory
        
        
    .. memberfunction:: getAbsolutePath -> String
        
        The absolute path, e.g. "my/dir" => "/current/directory/my/dir"
        
        
    .. memberfunction:: getChildrenNames -> ArrayList<T>
        
        List the name of the children of this path
        Works only on directories, obviously
        
        
    .. memberfunction:: getChildren -> ArrayList<T>
        
        List the children of this path
        Works only on directories, obviously
        
        
.. data:: FILE_ATTRIBUTE_DIRECTORY -> Long

.. data:: FILE_ATTRIBUTE_REPARSE_POINT -> Long

.. data:: FILE_ATTRIBUTE_NORMAL -> Long

