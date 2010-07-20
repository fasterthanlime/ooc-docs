structs/MultiMap
================

.. module:: structs/MultiMap

.. class:: MultiMap<K, V>
    
    :extends: :class:`~structs/HashMap HashMap<K, V>` 
    .. staticmethod:: new~multiMap -> :class:`~structs/MultiMap MultiMap<K, V>` 
        
    .. method:: init~multiMap
        
    .. staticmethod:: new~multiMapWithCapa (capacity: :cover:`~lang/types UInt` ) -> :class:`~structs/MultiMap MultiMap<K, V>` 
        
    .. method:: init~multiMapWithCapa (capacity: :cover:`~lang/types UInt` )
        
    .. method:: get~_super (key: K ) -> K 
        
    .. method:: put~_super (key: K , value: V ) -> :cover:`~lang/types Bool` 
        
    .. method:: put (key: K , value: V ) -> :cover:`~lang/types Bool` 
        
    .. method:: remove (key: K ) -> :cover:`~lang/types Bool` 
        
    .. method:: getAll (key: K ) -> V 
        
    .. method:: get (key: K ) -> V 
        
    .. method:: iterator -> :class:`~lang/types Iterator<T>` 
        
.. class:: MultiMapValueIterator<K, V>
    
    :extends: :class:`~lang/types Iterator<T>` 
    .. staticmethod:: new (map: :class:`~structs/MultiMap MultiMap<K, V>` ) -> :class:`~structs/MultiMap MultiMapValueIterator<K, V>` 
        
    .. method:: init (map: :class:`~structs/MultiMap MultiMap<K, V>` )
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: next -> V 
        
    .. method:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. method:: prev -> V 
        
    .. method:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: V -> :class:`~lang/types Class` 
    
    .. field:: K -> :class:`~lang/types Class` 
    
    .. field:: map -> :class:`~structs/MultiMap MultiMap<K, V>` 
    
    .. field:: index -> :cover:`~lang/types Int` 
    
    .. field:: sub -> :class:`~lang/types Iterator<T>` 
    
