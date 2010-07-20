structs/OrderedMultiMap
=======================

.. module:: structs/OrderedMultiMap

.. class:: OrderedMultiMap<K, V>
    
    :extends: :class:`~structs/MultiMap MultiMap<K, V>` 
    .. staticmethod:: new -> :class:`~structs/OrderedMultiMap OrderedMultiMap<K, V>` 
        
    .. method:: init
        
    .. method:: getKeys -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. method:: _containsKey (key: K ) -> :cover:`~lang/types Bool` 
        
    .. method:: put (key: K , value: V ) -> :cover:`~lang/types Bool` 
        
    .. method:: remove (key: K ) -> :cover:`~lang/types Bool` 
        
    .. field:: orderedKeys -> :class:`~structs/ArrayList ArrayList<T>` 
    
