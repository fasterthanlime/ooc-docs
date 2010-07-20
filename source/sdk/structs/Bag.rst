structs/Bag
===========

.. module:: structs/Bag

.. class:: Bag
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new~withCapacity (len: :cover:`~lang/types Int` ) -> :class:`~structs/Bag Bag` 
        
    .. method:: init~withCapacity (len: :cover:`~lang/types Int` )
        
    .. staticmethod:: new -> :class:`~structs/Bag Bag` 
        
    .. method:: init
        
    .. method:: add (element: T )
        
    .. method:: add~withIndex (index: :cover:`~lang/types Int` , element: T )
        
    .. method:: clear
        
    .. method:: get (index: :cover:`~lang/types Int` , T: :class:`~lang/types Class` ) -> T 
        
    .. method:: indexOf (element: T ) -> :cover:`~lang/types Int` 
        
    .. method:: lastIndexOf (element: T ) -> :cover:`~lang/types Int` 
        
    .. method:: removeAt (index: :cover:`~lang/types Int` , T: :class:`~lang/types Class` ) -> T 
        
    .. method:: remove (element: T ) -> :cover:`~lang/types Bool` 
        
    .. method:: set (index: :cover:`~lang/types Int` , element: T )
        
    .. method:: size -> :cover:`~lang/types Int` 
        
    .. field:: data -> :class:`~structs/ArrayList ArrayList<T>` 
    
