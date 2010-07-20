structs/OrderedMultiMap
=======================

.. module:: structs/OrderedMultiMap

.. class:: OrderedMultiMap<K,V>
    
    :extends: :class:`~structs/MultiMap MultiMap<K,V>` 
    .. staticmethod:: new~ommWithCapa (capacity: :cover:`~lang/types Int` ) -> :class:`~structs/OrderedMultiMap OrderedMultiMap<K,V>` 
        
    .. method:: init~ommWithCapa (capacity: :cover:`~lang/types Int` )
        
    .. staticmethod:: new~omm -> :class:`~structs/OrderedMultiMap OrderedMultiMap<K,V>` 
        
    .. method:: init~omm
        
    .. method:: getKeys -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. method:: _containsKey (key: K ) -> :cover:`~lang/types Bool` 
        
    .. method:: put (key: K , value: V ) -> :cover:`~lang/types Bool` 
        
    .. method:: remove (key: K ) -> :cover:`~lang/types Bool` 
        
    .. field:: orderedKeys -> :class:`~structs/ArrayList ArrayList<T>` 
    
