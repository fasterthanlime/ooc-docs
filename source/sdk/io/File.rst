io/File
=======

.. module:: io/File

.. class:: File
    
    .. memberfunction:: getPath -> String
        
    .. staticmemberfunction:: new (path: String) -> File
        
    .. staticmemberfunction:: new~parentFile (parent: File, path: String) -> File
        
    .. staticmemberfunction:: new~parentPath (parent, path: String) -> File
        
    .. memberfunction:: isDir -> Bool
        
        :return: true if it's a directory
        
        
    .. memberfunction:: isFile -> Bool
        
        :return: true if it's a file (ie. not a directory nor a symbolic link)
        
        
    .. memberfunction:: isLink -> Bool
        
        :return: true if the file is a symbolic link
        
        
    .. memberfunction:: size -> LLong
        
        :return: the size of the file, in bytes
        
        
    .. memberfunction:: exists -> Bool
        
        :return: true if the file exists and can be
        opened for reading
        
        
    .. memberfunction:: ownerPerm -> Int
        
        :return: the permissions for the owner of this file
        
        
    .. memberfunction:: groupPerm -> Int
        
        :return: the permissions for the group of this file
        
        
    .. memberfunction:: otherPerm -> Int
        
        :return: the permissions for the others (not owner, not group)
        
        
    .. memberfunction:: name -> String
        
        :return: the last part of the path, e.g. for /etc/init.d/bluetooth
        name() will return 'bluetooth'
        
        
    .. memberfunction:: parent -> File
        
        :return: the parent of this file, e.g. for /etc/init.d/bluetooth
        it will return /etc/init.d/ (as a File), or null if it's the
        root directory.
        
        
    .. memberfunction:: parentName -> String
        
        :return: the parent of this file, e.g. for /etc/init.d/bluetooth
        it will return /etc/init.d/ (as a File), or null if it's the
        root directory.
        
        
    .. memberfunction:: mkdir -> Int
        
        create a directory at the path specified by this file,
        with permissions 0c755 by default
        
        
    .. memberfunction:: mkdir~withMode (mode: Int32) -> Int
        
        create a directory at the path specified by this file
        
        :param mode: The permissions at the creation of the directory
        
        
    .. memberfunction:: mkdirs
        
        create a directory at the path specified by this file,
        and all the parent directories if needed,
        with permissions 0c755 by default
        
        
    .. memberfunction:: mkdirs~withMode (mode: Int32) -> Int
        
        create a directory at the path specified by this file,
        and all the parent directories if needed
        
        :param mode: The permissions at the creation of the directory
        
        
    .. memberfunction:: lastAccessed -> Long
        
        :return: the time of last access
        
        
    .. memberfunction:: lastModified -> Long
        
        :return: the time of last modification
        
        
    .. memberfunction:: created -> Long
        
        :return: the time of creation
        
        
    .. memberfunction:: isRelative -> Bool
        
        :return: true if the function is relative to the current directory
        
        
    .. memberfunction:: getAbsolutePath -> String
        
        The absolute path, e.g. "my/dir" => "/current/directory/my/dir"
        
        
    .. memberfunction:: getAbsoluteFile -> File
        
        A file corresponding to the absolute path
        
        :see: getAbsolutePath
        
        
    .. memberfunction:: getChildrenNames -> ArrayList<T>
        
        List the name of the children of this path
        Works only on directories, obviously
        
        
    .. memberfunction:: getChildren -> ArrayList<T>
        
        List the children of this path
        Works only on directories, obviously
        
        
    .. memberfunction:: remove -> Int
        
        Tries to remove the file. This only works for files, not directories.
        
        
    .. memberfunction:: copyTo (dstFile: File)
        
        Copies the content of this file to another
        
        :param dstFile: the file to copy to
        
        
    .. memberfunction:: getChild (name: String) -> File
        
        Get a child of this path
        
        :param name: The name of the child, relatively to this path
        
        
    .. staticmemberfunction:: getCwd -> String
        
        :return: the current working directory
        
        
    .. field:: MAX_PATH_LENGTH -> Int
    
    .. field:: path -> String
    
    .. field:: separator -> Char
    
    .. field:: pathDelimiter -> Char
    
