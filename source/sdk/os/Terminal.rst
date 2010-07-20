os/Terminal
===========

.. module:: os/Terminal

.. class:: Attr
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~os/Terminal Attr` 
        
    .. method:: init
        
    .. field:: reset -> :cover:`~lang/types Int` 
    
    .. field:: bright -> :cover:`~lang/types Int` 
    
    .. field:: dim -> :cover:`~lang/types Int` 
    
    .. field:: under -> :cover:`~lang/types Int` 
    
    .. field:: blink -> :cover:`~lang/types Int` 
    
    .. field:: reverse -> :cover:`~lang/types Int` 
    
    .. field:: hidden -> :cover:`~lang/types Int` 
    
.. class:: Color
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~os/Terminal Color` 
        
    .. method:: init
        
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
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~os/Terminal Terminal` 
        
    .. method:: init
        
    .. staticmethod:: setColor (f, b: :cover:`~lang/types Int` )
        
        Set foreground and background color
        
    .. staticmethod:: setFgColor (c: :cover:`~lang/types Int` )
        
        Set foreground color
        
    .. staticmethod:: setBgColor (c: :cover:`~lang/types Int` )
        
        Set background color
        
    .. staticmethod:: setAttr (att: :cover:`~lang/types Int` )
        
        Set text attribute
        
    .. staticmethod:: reset
        
        Reset the terminal colors and attributes
        
