structs/HashBag
===============

.. module:: structs/HashBag

.. class:: HashBag
    
    .. staticmemberfunction:: new -> HashBag
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withCapacity (capacity: Int) -> HashBag
        
    .. memberfunction:: init~withCapacity (capacity: Int)
        
    .. memberfunction:: get (key: String, T: Class) -> T
        
    .. memberfunction:: getEntry (key: String, T: Class) -> HashEntry<T>
        
    .. memberfunction:: put (key: String, value: T) -> Bool
        
    .. memberfunction:: add (key: String, value: T) -> Bool
        
    .. memberfunction:: isEmpty -> Bool
        
    .. memberfunction:: contains (key: String, T: Class) -> Bool
        
    .. memberfunction:: remove (key: String) -> Bool
        
    .. memberfunction:: size -> Int
        
    .. memberfunction:: exists (key: String) -> Bool
        
    .. field:: myMap -> HashMap<T>
    
