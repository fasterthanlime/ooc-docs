io/FileWriter
=============

.. module:: io/FileWriter

.. class:: FileWriter
    
    .. staticmemberfunction:: new~withFile (fileObject: :class:`~io/File File` , append: :cover:`~lang/types Bool` ) -> :class:`~io/FileWriter FileWriter` 
        
    .. memberfunction:: init~withFile (fileObject: :class:`~io/File File` , append: :cover:`~lang/types Bool` )
        
    .. staticmemberfunction:: new~withFileOverwrite (fileObject: :class:`~io/File File` ) -> :class:`~io/FileWriter FileWriter` 
        
    .. memberfunction:: init~withFileOverwrite (fileObject: :class:`~io/File File` )
        
    .. staticmemberfunction:: new~withName (fileName: :cover:`~lang/types String` , append: :cover:`~lang/types Bool` ) -> :class:`~io/FileWriter FileWriter` 
        
    .. memberfunction:: init~withName (fileName: :cover:`~lang/types String` , append: :cover:`~lang/types Bool` )
        
    .. staticmemberfunction:: new~withNameAndFileOverwrite (fileName: :cover:`~lang/types String` ) -> :class:`~io/FileWriter FileWriter` 
        
    .. memberfunction:: init~withNameAndFileOverwrite (fileName: :cover:`~lang/types String` )
        
    .. staticmemberfunction:: new~withNameOverwrite (fileName: :cover:`~lang/types String` ) -> :class:`~io/FileWriter FileWriter` 
        
    .. memberfunction:: init~withNameOverwrite (fileName: :cover:`~lang/types String` )
        
    .. memberfunction:: write (chars: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: write~chr (chr: :cover:`~lang/types Char` )
        
    .. memberfunction:: close
        
    .. memberfunction:: writef (fmt: :cover:`~lang/types String` , ...)
        
    .. memberfunction:: vwritef (fmt: :cover:`~lang/types String` , args: :cover:`~lang/vararg VaList` )
        
    .. field:: file -> :cover:`~lang/stdio FStream` 
    
