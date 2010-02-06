text/StringBuffer
=================

.. module:: text/StringBuffer

.. class:: StringBuffer
    
    .. staticmemberfunction:: new -> StringBuffer
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withCapa (capacity: SizeT) -> StringBuffer
        
    .. memberfunction:: init~withCapa (capacity: SizeT)
        
    .. staticmemberfunction:: new~withContent (data: String) -> StringBuffer
        
    .. memberfunction:: init~withContent (data: String)
        
    .. memberfunction:: close
        
    .. memberfunction:: write~chr (chr: Char)
        
    .. memberfunction:: write (chars: String, length: SizeT) -> SizeT
        
    .. memberfunction:: append~str (str: String)
        
    .. memberfunction:: append~strWithLength (str: String, length: SizeT)
        
    .. memberfunction:: append~chr (chr: Char)
        
    .. memberfunction:: checkLength (min: SizeT)
        
    .. memberfunction:: toString -> String
        
    .. field:: size -> SizeT
    
    .. field:: capacity -> SizeT
    
    .. field:: data -> String
    
