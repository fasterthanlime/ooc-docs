structs/HashBag
===============

.. module:: structs/HashBag

.. class:: HashBag
    
    .. staticmemberfunction:: new -> :class:`~structs/HashBag HashBag` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withCapacity (capacity: :cover:`~lang/types Int` ) -> :class:`~structs/HashBag HashBag` 
        
    .. memberfunction:: init~withCapacity (capacity: :cover:`~lang/types Int` )
        
    .. memberfunction:: get (key: :cover:`~lang/types String` , T: :class:`~lang/types Class` ) -> T 
        
    .. memberfunction:: getEntry (key: :cover:`~lang/types String` , T: :class:`~lang/types Class` ) -> :class:`~structs/HashMap HashEntry<T>` 
        
    .. memberfunction:: put (key: :cover:`~lang/types String` , value: T ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: add (key: :cover:`~lang/types String` , value: T ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isEmpty -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: contains (key: :cover:`~lang/types String` , T: :class:`~lang/types Class` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: remove (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: size -> :cover:`~lang/types Int` 
        
    .. memberfunction:: exists (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. field:: myMap -> :class:`~structs/HashMap HashMap<T>` 
    
