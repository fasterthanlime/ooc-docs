structs/MultiMap
================

.. module:: structs/MultiMap

.. class:: MultiMap<T>
    
    :extends: :class:`~structs/HashMap HashMap<T>` 
    .. staticmemberfunction:: new~multiMap -> :class:`~structs/MultiMap MultiMap<T>` 
        
    .. memberfunction:: init~multiMap
        
    .. memberfunction:: put (key: :cover:`~lang/types String` , value: T ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: remove (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: getAll (key: :cover:`~lang/types String` ) -> T 
        
    .. memberfunction:: get (key: :cover:`~lang/types String` ) -> T 
        
    .. memberfunction:: iterator -> :class:`~lang/types Iterator<T>` 
        
.. class:: MultiMapValueIterator<T>
    
    :extends: :class:`~lang/types Iterator<T>` 
    .. staticmemberfunction:: new (map: :class:`~structs/MultiMap MultiMap<T>` ) -> :class:`~structs/MultiMap MultiMapValueIterator<T>` 
        
    .. memberfunction:: init (map: :class:`~structs/MultiMap MultiMap<T>` )
        
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: next -> T 
        
    .. memberfunction:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: prev -> T 
        
    .. memberfunction:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: map -> :class:`~structs/MultiMap MultiMap<T>` 
    
    .. field:: index -> :cover:`~lang/types Int` 
    
    .. field:: sub -> :class:`~lang/types Iterator<T>` 
    
