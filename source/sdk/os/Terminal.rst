os/Terminal
===========

.. module:: os/Terminal

.. class:: Attr
    
    .. staticmemberfunction:: new -> :class:`~os/Terminal Attr` 
        
    .. memberfunction:: init
        
    .. field:: reset -> :cover:`~lang/types Int` 
    
    .. field:: bright -> :cover:`~lang/types Int` 
    
    .. field:: dim -> :cover:`~lang/types Int` 
    
    .. field:: under -> :cover:`~lang/types Int` 
    
    .. field:: blink -> :cover:`~lang/types Int` 
    
    .. field:: reverse -> :cover:`~lang/types Int` 
    
    .. field:: hidden -> :cover:`~lang/types Int` 
    
.. class:: Color
    
    .. staticmemberfunction:: new -> :class:`~os/Terminal Color` 
        
    .. memberfunction:: init
        
    .. field:: black -> :cover:`~lang/types Int` 
    
    .. field:: red -> :cover:`~lang/types Int` 
    
    .. field:: green -> :cover:`~lang/types Int` 
    
    .. field:: yellow -> :cover:`~lang/types Int` 
    
    .. field:: blue -> :cover:`~lang/types Int` 
    
    .. field:: magenta -> :cover:`~lang/types Int` 
    
    .. field:: cyan -> :cover:`~lang/types Int` 
    
    .. field:: grey -> :cover:`~lang/types Int` 
    
    .. field:: white -> :cover:`~lang/types Int` 
    
.. class:: Terminal
    
    .. staticmemberfunction:: new -> :class:`~os/Terminal Terminal` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: setColor (f, b: :cover:`~lang/types Int` )
        
        Set foreground and background color 
        
    .. staticmemberfunction:: setFgColor (c: :cover:`~lang/types Int` )
        
        Set foreground color 
        
    .. staticmemberfunction:: setBgColor (c: :cover:`~lang/types Int` )
        
        Set background color 
        
    .. staticmemberfunction:: setAttr (att: :cover:`~lang/types Int` )
        
        Set text attribute 
        
    .. staticmemberfunction:: reset
        
        Reset the terminal colors and attributes 
        
