structs/Bag
===========

.. module:: structs/Bag

.. class:: Bag
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new~withCapacity (len: :cover:`~lang/types Int` ) -> :class:`~structs/Bag Bag` 
        
    .. memberfunction:: init~withCapacity (len: :cover:`~lang/types Int` )
        
    .. staticmemberfunction:: new -> :class:`~structs/Bag Bag` 
        
    .. memberfunction:: init
        
    .. memberfunction:: add (element: T )
        
    .. memberfunction:: add~withIndex (index: :cover:`~lang/types Int` , element: T )
        
    .. memberfunction:: clear
        
    .. memberfunction:: get (index: :cover:`~lang/types Int` , T: :class:`~lang/types Class` ) -> T 
        
    .. memberfunction:: indexOf (element: T ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: lastIndexOf (element: T ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: removeAt (index: :cover:`~lang/types Int` , T: :class:`~lang/types Class` ) -> T 
        
    .. memberfunction:: remove (element: T ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: set (index: :cover:`~lang/types Int` , element: T )
        
    .. memberfunction:: size -> :cover:`~lang/types Int` 
        
    .. field:: data -> :class:`~structs/ArrayList ArrayList<T>` 
    
