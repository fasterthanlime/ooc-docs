text/StringBuffer
=================

.. module:: text/StringBuffer

.. class:: StringBuffer
    
    .. staticmemberfunction:: new -> :class:`~text/StringBuffer StringBuffer` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withCapa (capacity: :cover:`~lang/types SizeT` ) -> :class:`~text/StringBuffer StringBuffer` 
        
    .. memberfunction:: init~withCapa (capacity: :cover:`~lang/types SizeT` )
        
    .. staticmemberfunction:: new~withContent (data: :cover:`~lang/types String` ) -> :class:`~text/StringBuffer StringBuffer` 
        
    .. memberfunction:: init~withContent (data: :cover:`~lang/types String` )
        
    .. memberfunction:: close
        
    .. memberfunction:: write~chr (chr: :cover:`~lang/types Char` )
        
    .. memberfunction:: write (chars: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: append~str (str: :cover:`~lang/types String` )
        
    .. memberfunction:: append~strWithLength (str: :cover:`~lang/types String` , length: :cover:`~lang/types SizeT` )
        
    .. memberfunction:: append~chr (chr: :cover:`~lang/types Char` )
        
    .. memberfunction:: checkLength (min: :cover:`~lang/types SizeT` )
        
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. field:: size -> :cover:`~lang/types SizeT` 
    
    .. field:: capacity -> :cover:`~lang/types SizeT` 
    
    .. field:: data -> :cover:`~lang/types String` 
    
