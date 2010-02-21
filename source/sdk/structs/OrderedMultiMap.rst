structs/OrderedMultiMap
=======================

.. module:: structs/OrderedMultiMap

.. class:: OrderedMultiMap<T>
    
    :extends: :class:`~structs/MultiMap MultiMap<T>` 
    .. staticmemberfunction:: new -> :class:`~structs/OrderedMultiMap OrderedMultiMap<T>` 
        
    .. memberfunction:: init
        
    .. memberfunction:: getKeys -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. memberfunction:: _containsKey (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: put (key: :cover:`~lang/types String` , value: T ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: remove (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. field:: orderedKeys -> :class:`~structs/ArrayList ArrayList<T>` 
    
