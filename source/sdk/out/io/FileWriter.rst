io/FileWriter
=============

.. module:: io/FileWriter

.. class:: FileWriter
    
    :extends: :class:`~io/Writer Writer` 
    .. staticmethod:: new~withFile (fileObject: :class:`~io/File File` , append: :cover:`~lang/types Bool` ) -> :class:`~io/FileWriter FileWriter` 
        
    .. method:: init~withFile (fileObject: :class:`~io/File File` , append: :cover:`~lang/types Bool` )
        
    .. staticmethod:: new~withFileOverwrite (fileObject: :class:`~io/File File` ) -> :class:`~io/FileWriter FileWriter` 
        
    .. method:: init~withFileOverwrite (fileObject: :class:`~io/File File` )
        
    .. staticmethod:: new~withName (fileName: :cover:`~lang/types String` , append: :cover:`~lang/types Bool` ) -> :class:`~io/FileWriter FileWriter` 
        
    .. method:: init~withName (fileName: :cover:`~lang/types String` , append: :cover:`~lang/types Bool` )
        
    .. staticmethod:: new~withNameOverwrite (fileName: :cover:`~lang/types String` ) -> :class:`~io/FileWriter FileWriter` 
        
    .. method:: init~withNameOverwrite (fileName: :cover:`~lang/types String` )
        
    .. method:: write (chars: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types SizeT` 
        
    .. method:: write~chr (chr: :cover:`~lang/types Char` )
        
    .. method:: close
        
    .. method:: writef (fmt: :cover:`~lang/types String` , ...)
        
    .. method:: vwritef (fmt: :cover:`~lang/types String` , args: :cover:`~lang/vararg VaList` )
        
    .. field:: file -> :cover:`~lang/stdio FStream` 
    
