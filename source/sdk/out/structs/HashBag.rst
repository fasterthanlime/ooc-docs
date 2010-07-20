structs/HashBag
===============

.. module:: structs/HashBag

.. class:: HashBag
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~structs/HashBag HashBag` 
        
    .. method:: init
        
    .. staticmethod:: new~withCapacity (capacity: :cover:`~lang/types Int` ) -> :class:`~structs/HashBag HashBag` 
        
    .. method:: init~withCapacity (capacity: :cover:`~lang/types Int` )
        
    .. method:: get (key: :cover:`~lang/types String` , T: :class:`~lang/types Class` ) -> T 
        
    .. method:: getEntry (key: :cover:`~lang/types String` , V: :class:`~lang/types Class` ) -> :class:`~structs/HashMap HashEntry<K, V>` 
        
    .. method:: put (key: :cover:`~lang/types String` , value: T ) -> :cover:`~lang/types Bool` 
        
    .. method:: add (key: :cover:`~lang/types String` , value: T ) -> :cover:`~lang/types Bool` 
        
    .. method:: isEmpty -> :cover:`~lang/types Bool` 
        
    .. method:: remove (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. method:: size -> :cover:`~lang/types Int` 
        
    .. method:: contains (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. field:: myMap -> :class:`~structs/HashMap HashMap<K, V>` 
    
