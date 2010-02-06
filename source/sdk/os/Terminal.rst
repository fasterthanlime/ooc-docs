os/Terminal
===========

.. module:: os/Terminal

.. class:: Attr
    
    .. staticmemberfunction:: new -> Attr
        
    .. memberfunction:: init
        
    .. field:: reset -> Int
    
    .. field:: bright -> Int
    
    .. field:: dim -> Int
    
    .. field:: under -> Int
    
    .. field:: blink -> Int
    
    .. field:: reverse -> Int
    
    .. field:: hidden -> Int
    
.. class:: Color
    
    .. staticmemberfunction:: new -> Color
        
    .. memberfunction:: init
        
    .. field:: black -> Int
    
    .. field:: red -> Int
    
    .. field:: green -> Int
    
    .. field:: yellow -> Int
    
    .. field:: blue -> Int
    
    .. field:: magenta -> Int
    
    .. field:: cyan -> Int
    
    .. field:: grey -> Int
    
    .. field:: white -> Int
    
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
        
