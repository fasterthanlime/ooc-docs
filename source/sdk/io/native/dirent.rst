io/native/dirent
================

.. module:: io/native/dirent

.. function:: closedir (:cover:`~io/native/dirent DirPtr` ) -> :cover:`~lang/types Int` 
    
.. function:: opendir (:cover:`~lang/types String` ) -> :cover:`~io/native/dirent DirPtr` 
    
.. function:: readdir (:cover:`~io/native/dirent DirPtr` ) -> :cover:`~io/native/dirent DirEnt` *
    
.. function:: readdir_r (:cover:`~io/native/dirent DirPtr` , :cover:`~io/native/dirent DirEnt` *, :cover:`~io/native/dirent DirEnt` **) -> :cover:`~lang/types Int` 
    
.. function:: rewinddir (:cover:`~io/native/dirent DirPtr` )
    
.. function:: seekdir (:cover:`~io/native/dirent DirPtr` , :cover:`~lang/types Long` )
    
.. function:: telldir (:cover:`~io/native/dirent DirPtr` ) -> :cover:`~lang/types Long` 
    
.. cover:: DirPtr
    
.. cover:: DirEnt
    
