structs/LinkedList
==================

.. module:: structs/LinkedList

.. function:: getchar
    
.. class:: LinkedList<T>
    
    :extends: :class:`~structs/List List<T>` 
    .. staticmethod:: new -> :class:`~structs/LinkedList LinkedList<T>` 
        
    .. method:: init
        
    .. method:: add (data: T )
        
    .. method:: add~withIndex (index: :cover:`~lang/types Int` , data: T )
        
    .. method:: clear
        
    .. method:: get (index: :cover:`~lang/types Int` ) -> T 
        
    .. method:: getNode (index: :cover:`~lang/types Int` ) -> :class:`~structs/LinkedList Node<T>` 
        
    .. method:: indexOf (data: T ) -> :cover:`~lang/types Int` 
        
    .. method:: lastIndexOf (data: T ) -> :cover:`~lang/types Int` 
        
    .. method:: removeAt (index: :cover:`~lang/types Int` ) -> T 
        
    .. method:: remove (data: T ) -> :cover:`~lang/types Bool` 
        
    .. method:: removeNode (toRemove: :class:`~structs/LinkedList Node<T>` ) -> :cover:`~lang/types Bool` 
        
    .. method:: set (index: :cover:`~lang/types Int` , data: T ) -> T 
        
    .. method:: size -> :cover:`~lang/types Int` 
        
    .. method:: iterator -> :class:`~structs/LinkedList LinkedListIterator<T>` 
        
    .. method:: clone -> :class:`~structs/LinkedList LinkedList<T>` 
        
    .. method:: print
        
    .. field:: size -> :cover:`~lang/types Int` 
    
    .. field:: first -> :class:`~structs/LinkedList Node<T>` 
    
    .. field:: last -> :class:`~structs/LinkedList Node<T>` 
    
.. class:: Node<T>
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~structs/LinkedList Node<T>` 
        
    .. method:: init
        
    .. staticmethod:: new~withParams (prev, next: :class:`~structs/LinkedList Node<T>` , data: T ) -> :class:`~structs/LinkedList Node<T>` 
        
    .. method:: init~withParams (prev, next: :class:`~structs/LinkedList Node<T>` , data: T )
        
    .. field:: T -> :class:`~lang/types Class` 
    
    .. field:: prev -> :class:`~structs/LinkedList Node<T>` 
    
    .. field:: next -> :class:`~structs/LinkedList Node<T>` 
    
    .. field:: data -> T 
    
.. class:: LinkedListIterator<T>
    
    :extends: :class:`~lang/types Iterator<T>` 
    .. staticmethod:: new (list: :class:`~structs/LinkedList LinkedList<T>` ) -> :class:`~structs/LinkedList LinkedListIterator<T>` 
        
    .. method:: init (list: :class:`~structs/LinkedList LinkedList<T>` )
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: next -> T 
        
    .. method:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. method:: prev -> T 
        
    .. method:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: current -> :class:`~structs/LinkedList Node<T>` 
    
    .. field:: list -> :class:`~structs/LinkedList LinkedList<T>` 
    
