structs/ArrayList
=================

.. module:: structs/ArrayList

.. class:: ArrayList<T>
    
    .. memberfunction:: new -> ArrayList<T>
        
    
    .. memberfunction:: init
        
    
    .. memberfunction:: new~withCapacity (capacity: Int) -> ArrayList<T>
        
    
    .. memberfunction:: init~withCapacity (capacity: Int)
        
    
    .. memberfunction:: new~withData (data: T*, size: Int) -> ArrayList<T>
        
    
    .. memberfunction:: init~withData (data: T*, size: Int)
        
    
    .. memberfunction:: add (element: T)
        
    
    .. memberfunction:: add~withIndex (index: Int, element: T)
        
    
    .. memberfunction:: clear
        
    
    .. memberfunction:: get (index: Int) -> T
        
    
    .. memberfunction:: indexOf (element: T) -> Int
        
    
    .. memberfunction:: lastIndexOf (element: T) -> Int
        
    
    .. memberfunction:: removeAt (index: Int) -> T
        
    
    .. memberfunction:: remove (element: T) -> Bool
        
        Removes a single instance of the specified element from this list,
        if it is present (optional operation).
        @return true if at least one occurence of the element has been
        removed
        
        
    
    .. memberfunction:: set (index: Int, element: T) -> T
        
        Replaces the element at the specified position in this list with
        the specified element.
        
        
    
    .. memberfunction:: size -> Int
        
        @return the number of elements in this list.
        
        
    
    .. memberfunction:: ensureCapacity (newSize: Int)
        
        Increases the capacity of this ArrayList instance, if necessary,
        to ensure that it can hold at least the number of elements
        specified by the minimum capacity argument.
        
        
    
    .. memberfunction:: grow
        
        private 
        
    
    .. memberfunction:: checkIndex (index: Int)
        
        private 
        
    
    .. memberfunction:: iterator -> Iterator<T>
        
    
    .. memberfunction:: clone -> ArrayList<T>
        
    
    .. memberfunction:: toArray -> Pointer
        
        
        
    
    .. field:: data
    
    .. field:: capacity
    
    .. field:: size
    

.. class:: ArrayListIterator<T>
    
    .. memberfunction:: new (list: ArrayList<T>) -> ArrayListIterator<T>
        
    
    .. memberfunction:: init (list: ArrayList<T>)
        
    
    .. memberfunction:: hasNext -> Bool
        
    
    .. memberfunction:: next -> T
        
    
    .. memberfunction:: hasPrev -> Bool
        
    
    .. memberfunction:: prev -> T
        
    
    .. memberfunction:: remove -> Bool
        
    
    .. field:: list
    
    .. field:: index
    

