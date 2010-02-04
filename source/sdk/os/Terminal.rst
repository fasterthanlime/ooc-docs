os/Terminal
===========

.. module:: os/Terminal

.. class:: Attr
    
    .. staticmemberfunction:: new -> Attr
        
    .. memberfunction:: init
        
    .. field:: reset
    
    .. field:: bright
    
    .. field:: dim
    
    .. field:: under
    
    .. field:: blink
    
    .. field:: reverse
    
    .. field:: hidden
    
.. class:: Color
    
    .. staticmemberfunction:: new -> Color
        
    .. memberfunction:: init
        
    .. field:: black
    
    .. field:: red
    
    .. field:: green
    
    .. field:: yellow
    
    .. field:: blue
    
    .. field:: magenta
    
    .. field:: cyan
    
    .. field:: grey
    
    .. field:: white
    
.. class:: Terminal
    
    .. staticmemberfunction:: new -> Terminal
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: setColor (f, b: Int)
        
        Set foreground and background color 
        
    .. staticmemberfunction:: setFgColor (c: Int)
        
        Set foreground color 
        
    .. staticmemberfunction:: setBgColor (c: Int)
        
        Set background color 
        
    .. staticmemberfunction:: setAttr (att: Int)
        
        Set text attribute 
        
    .. staticmemberfunction:: reset
        
        Reset the terminal colors and attributes 
        
