structs/LinkedList
==================

.. module:: structs/LinkedList

.. function:: getchar
    
.. class:: LinkedList<T>
    
    .. staticmemberfunction:: new -> :class:`~structs/LinkedList LinkedList<T>`
        
    .. memberfunction:: init
        
    .. memberfunction:: add (data: T)
        
    .. memberfunction:: add~withIndex (index: :cover:`~lang/types Int`, data: T)
        
    .. memberfunction:: clear
        
    .. memberfunction:: get (index: :cover:`~lang/types Int`) -> T
        
    .. memberfunction:: getNode (index: :cover:`~lang/types Int`) -> :class:`~structs/LinkedList Node<T>`
        
    .. memberfunction:: indexOf (data: T) -> :cover:`~lang/types Int`
        
    .. memberfunction:: lastIndexOf (data: T) -> :cover:`~lang/types Int`
        
    .. memberfunction:: removeAt (index: :cover:`~lang/types Int`) -> T
        
    .. memberfunction:: remove (data: T) -> :cover:`~lang/types Bool`
        
    .. memberfunction:: removeNode (toRemove: :class:`~structs/LinkedList Node<T>`) -> :cover:`~lang/types Bool`
        
    .. memberfunction:: set (index: :cover:`~lang/types Int`, data: T) -> T
        
    .. memberfunction:: size -> :cover:`~lang/types Int`
        
    .. memberfunction:: iterator -> :class:`~structs/LinkedList LinkedListIterator<T>`
        
    .. memberfunction:: clone -> :class:`~structs/LinkedList LinkedList<T>`
        
    .. memberfunction:: print
        
    .. field:: size -> :cover:`~lang/types Int`
    
    .. field:: first -> :class:`~structs/LinkedList Node<T>`
    
    .. field:: last -> :class:`~structs/LinkedList Node<T>`
    
