io/File
=======

.. module:: io/File

.. class:: File
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new (path: :cover:`~lang/types String` ) -> :class:`~io/File File` 
        
    .. staticmethod:: new~parentFile (parent: :class:`~io/File File` , path: :cover:`~lang/types String` ) -> :class:`~io/File File` 
        
    .. staticmethod:: new~parentPath (parent, path: :cover:`~lang/types String` ) -> :class:`~io/File File` 
        
    .. method:: isDir -> :cover:`~lang/types Bool` 
        
        :return: true if it's a directory
        
        
    .. method:: isFile -> :cover:`~lang/types Bool` 
        
        :return: true if it's a file (ie. not a directory nor a symbolic link)
        
        
    .. method:: isLink -> :cover:`~lang/types Bool` 
        
        :return: true if the file is a symbolic link
        
        
    .. method:: size -> :cover:`~lang/types LLong` 
        
        :return: the size of the file, in bytes
        
        
    .. method:: exists -> :cover:`~lang/types Bool` 
        
        :return: true if the file exists and can be
        opened for reading
        
        
    .. method:: ownerPerm -> :cover:`~lang/types Int` 
        
        :return: the permissions for the owner of this file
        
        
    .. method:: groupPerm -> :cover:`~lang/types Int` 
        
        :return: the permissions for the group of this file
        
        
    .. method:: otherPerm -> :cover:`~lang/types Int` 
        
        :return: the permissions for the others (not owner, not group)
        
        
    .. method:: name -> :cover:`~lang/types String` 
        
        :return: the last part of the path, e.g. for /etc/init.d/bluetooth
        name() will return 'bluetooth'
        
        
    .. method:: parent -> :class:`~io/File File` 
        
        :return: the parent of this file, e.g. for /etc/init.d/bluetooth
        it will return /etc/init.d/ (as a File), or null if it's the
        root directory.
        
        
    .. method:: parentName -> :cover:`~lang/types String` 
        
        :return: the parent of this file, e.g. for /etc/init.d/bluetooth
        it will return /etc/init.d/ (as a File), or null if it's the
        root directory.
        
        
    .. method:: mkdir -> :cover:`~lang/types Int` 
        
        create a directory at the path specified by this file,
        with permissions 0c755 by default
        
        
    .. method:: mkdir~withMode (mode: :cover:`~lang/types Int32` ) -> :cover:`~lang/types Int` 
        
        create a directory at the path specified by this file
        
        :param mode: The permissions at the creation of the directory
        
        
    .. method:: mkdirs
        
        create a directory at the path specified by this file,
        and all the parent directories if needed,
        with permissions 0c755 by default
        
        
    .. method:: mkdirs~withMode (mode: :cover:`~lang/types Int32` ) -> :cover:`~lang/types Int` 
        
        create a directory at the path specified by this file,
        and all the parent directories if needed
        
        :param mode: The permissions at the creation of the directory
        
        
    .. method:: lastAccessed -> :cover:`~lang/types Long` 
        
        :return: the time of last access
        
        
    .. method:: lastModified -> :cover:`~lang/types Long` 
        
        :return: the time of last modification
        
        
    .. method:: created -> :cover:`~lang/types Long` 
        
        :return: the time of creation
        
        
    .. method:: isRelative -> :cover:`~lang/types Bool` 
        
        :return: true if the function is relative to the current directory
        
        
    .. method:: getPath -> :cover:`~lang/types String` 
        
        the path this file has been created with
        
        
    .. method:: getAbsolutePath -> :cover:`~lang/types String` 
        
        The absolute path, e.g. "my/dir" => "/current/directory/my/dir"
        
        
    .. method:: getAbsoluteFile -> :class:`~io/File File` 
        
        A file corresponding to the absolute path
        
        :see: getAbsolutePath
        
        
    .. method:: getChildrenNames -> :class:`~structs/ArrayList ArrayList<T>` 
        
        List the name of the children of this path
        Works only on directories, obviously
        
        
    .. method:: getChildren -> :class:`~structs/ArrayList ArrayList<T>` 
        
        List the children of this path
        Works only on directories, obviously
        
        
    .. method:: remove -> :cover:`~lang/types Int` 
        
        Tries to remove the file. This only works for files, not directories.
        
        
    .. method:: copyTo (dstFile: :class:`~io/File File` )
        
        Copies the content of this file to another
        
        :param dstFile: the file to copy to
        
        
    .. method:: read -> :cover:`~lang/types String` 
        
    .. method:: write~string (str: :cover:`~lang/types String` )
        
    .. method:: write~reader (reader: :class:`~io/Reader Reader` )
        
    .. method:: getChild (name: :cover:`~lang/types String` ) -> :class:`~io/File File` 
        
        Get a child of this path
        
        :param name: The name of the child, relatively to this path
        
        
    .. staticmethod:: getCwd -> :cover:`~lang/types String` 
        
        :return: the current working directory
        
        
    .. field:: MAX_PATH_LENGTH -> :cover:`~lang/types Int` 
    
    .. field:: path -> :cover:`~lang/types String` 
    
    .. field:: separator -> :cover:`~lang/types Char` 
    
    .. field:: pathDelimiter -> :cover:`~lang/types Char` 
    
