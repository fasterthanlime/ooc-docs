os/Terminal
===========

.. module:: os/Terminal

.. class:: Attr
    
    .. memberfunction:: new -> Attr
        
    
    .. memberfunction:: init
        
    
    .. field:: reset
    
    .. field:: bright
    
    .. field:: dim
    
    .. field:: under
    
    .. field:: blink
    
    .. field:: reverse
    
    .. field:: hidden
    

.. class:: Color
    
    .. memberfunction:: new -> Color
        
    
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
    
    .. memberfunction:: new -> Terminal
        
    
    .. memberfunction:: init
        
    
    .. memberfunction:: setColor (f, b: Int)
        
        Set foreground and background color 
        
    
    .. memberfunction:: setFgColor (c: Int)
        
        Set foreground color 
        
    
    .. memberfunction:: setBgColor (c: Int)
        
        Set background color 
        
    
    .. memberfunction:: setAttr (att: Int)
        
        Set text attribute 
        
    
    .. memberfunction:: reset
        
        Reset the terminal colors and attributes 
        
    

