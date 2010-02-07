io/File
=======

.. module:: io/File

.. class:: File
    
    :extends: :class:`~lang/types Object` 
    .. memberfunction:: getPath -> :cover:`~lang/types String` 
        
    .. staticmemberfunction:: new (path: :cover:`~lang/types String` ) -> :class:`~io/File File` 
        
    .. staticmemberfunction:: new~parentFile (parent: :class:`~io/File File` , path: :cover:`~lang/types String` ) -> :class:`~io/File File` 
        
    .. staticmemberfunction:: new~parentPath (parent, path: :cover:`~lang/types String` ) -> :class:`~io/File File` 
        
    .. memberfunction:: isDir -> :cover:`~lang/types Bool` 
        
        :return: true if it's a directory
        
        
    .. memberfunction:: isFile -> :cover:`~lang/types Bool` 
        
        :return: true if it's a file (ie. not a directory nor a symbolic link)
        
        
    .. memberfunction:: isLink -> :cover:`~lang/types Bool` 
        
        :return: true if the file is a symbolic link
        
        
    .. memberfunction:: size -> :cover:`~lang/types LLong` 
        
        :return: the size of the file, in bytes
        
        
    .. memberfunction:: exists -> :cover:`~lang/types Bool` 
        
        :return: true if the file exists and can be
        opened for reading
        
        
    .. memberfunction:: ownerPerm -> :cover:`~lang/types Int` 
        
        :return: the permissions for the owner of this file
        
        
    .. memberfunction:: groupPerm -> :cover:`~lang/types Int` 
        
        :return: the permissions for the group of this file
        
        
    .. memberfunction:: otherPerm -> :cover:`~lang/types Int` 
        
        :return: the permissions for the others (not owner, not group)
        
        
    .. memberfunction:: name -> :cover:`~lang/types String` 
        
        :return: the last part of the path, e.g. for /etc/init.d/bluetooth
        name() will return 'bluetooth'
        
        
    .. memberfunction:: parent -> :class:`~io/File File` 
        
        :return: the parent of this file, e.g. for /etc/init.d/bluetooth
        it will return /etc/init.d/ (as a File), or null if it's the
        root directory.
        
        
    .. memberfunction:: parentName -> :cover:`~lang/types String` 
        
        :return: the parent of this file, e.g. for /etc/init.d/bluetooth
        it will return /etc/init.d/ (as a File), or null if it's the
        root directory.
        
        
    .. memberfunction:: mkdir -> :cover:`~lang/types Int` 
        
        create a directory at the path specified by this file,
        with permissions 0c755 by default
        
        
    .. memberfunction:: mkdir~withMode (mode: :cover:`~lang/types Int32` ) -> :cover:`~lang/types Int` 
        
        create a directory at the path specified by this file
        
        :param mode: The permissions at the creation of the directory
        
        
    .. memberfunction:: mkdirs
        
        create a directory at the path specified by this file,
        and all the parent directories if needed,
        with permissions 0c755 by default
        
        
    .. memberfunction:: mkdirs~withMode (mode: :cover:`~lang/types Int32` ) -> :cover:`~lang/types Int` 
        
        create a directory at the path specified by this file,
        and all the parent directories if needed
        
        :param mode: The permissions at the creation of the directory
        
        
    .. memberfunction:: lastAccessed -> :cover:`~lang/types Long` 
        
        :return: the time of last access
        
        
    .. memberfunction:: lastModified -> :cover:`~lang/types Long` 
        
        :return: the time of last modification
        
        
    .. memberfunction:: created -> :cover:`~lang/types Long` 
        
        :return: the time of creation
        
        
    .. memberfunction:: isRelative -> :cover:`~lang/types Bool` 
        
        :return: true if the function is relative to the current directory
        
        
    .. memberfunction:: getAbsolutePath -> :cover:`~lang/types String` 
        
        The absolute path, e.g. "my/dir" => "/current/directory/my/dir"
        
        
    .. memberfunction:: getAbsoluteFile -> :class:`~io/File File` 
        
        A file corresponding to the absolute path
        
        :see: getAbsolutePath
        
        
    .. memberfunction:: getChildrenNames -> :class:`~structs/ArrayList ArrayList<T>` 
        
        List the name of the children of this path
        Works only on directories, obviously
        
        
    .. memberfunction:: getChildren -> :class:`~structs/ArrayList ArrayList<T>` 
        
        List the children of this path
        Works only on directories, obviously
        
        
    .. memberfunction:: remove -> :cover:`~lang/types Int` 
        
        Tries to remove the file. This only works for files, not directories.
        
        
    .. memberfunction:: copyTo (dstFile: :class:`~io/File File` )
        
        Copies the content of this file to another
        
        :param dstFile: the file to copy to
        
        
    .. memberfunction:: getChild (name: :cover:`~lang/types String` ) -> :class:`~io/File File` 
        
        Get a child of this path
        
        :param name: The name of the child, relatively to this path
        
        
    .. staticmemberfunction:: getCwd -> :cover:`~lang/types String` 
        
        :return: the current working directory
        
        
    .. field:: MAX_PATH_LENGTH -> :cover:`~lang/types Int` 
    
    .. field:: path -> :cover:`~lang/types String` 
    
    .. field:: separator -> :cover:`~lang/types Char` 
    
    .. field:: pathDelimiter -> :cover:`~lang/types Char` 
    
