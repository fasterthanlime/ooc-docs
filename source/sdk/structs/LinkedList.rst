structs/LinkedList
==================

.. module:: structs/LinkedList

.. function:: getchar
    
.. class:: LinkedList<T>
    
    .. staticmemberfunction:: new -> LinkedList<T>
        
    .. memberfunction:: init
        
    .. memberfunction:: add (data: T)
        
    .. memberfunction:: add~withIndex (index: Int, data: T)
        
    .. memberfunction:: clear
        
    .. memberfunction:: get (index: Int) -> T
        
    .. memberfunction:: getNode (index: Int) -> Node<T>
        
    .. memberfunction:: indexOf (data: T) -> Int
        
    .. memberfunction:: lastIndexOf (data: T) -> Int
        
    .. memberfunction:: removeAt (index: Int) -> T
        
    .. memberfunction:: remove (data: T) -> Bool
        
    .. memberfunction:: removeNode (toRemove: Node<T>) -> Bool
        
    .. memberfunction:: set (index: Int, data: T) -> T
        
    .. memberfunction:: size -> Int
        
    .. memberfunction:: iterator -> LinkedListIterator<T>
        
    .. memberfunction:: clone -> LinkedList<T>
        
    .. memberfunction:: print
        
    .. field:: size -> Int
    
    .. field:: first -> Node<T>
    
    .. field:: last -> Node<T>
    
