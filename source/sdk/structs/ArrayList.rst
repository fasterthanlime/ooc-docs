structs/ArrayList
=================

.. module:: structs/ArrayList

.. class:: ArrayList<T>
    
    :extends: :class:`~structs/List List<T>` 
    .. staticmethod:: new -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. method:: init
        
    .. staticmethod:: new~withCapacity (capacity: :cover:`~lang/types Int` ) -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. method:: init~withCapacity (capacity: :cover:`~lang/types Int` )
        
    .. staticmethod:: new~withData (data: T *, size: :cover:`~lang/types Int` ) -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. method:: init~withData (data: T *, size: :cover:`~lang/types Int` )
        
    .. method:: add (element: T )
        
    .. method:: add~withIndex (index: :cover:`~lang/types Int` , element: T )
        
    .. method:: clear
        
    .. method:: get (index: :cover:`~lang/types Int` ) -> T 
        
    .. method:: indexOf (element: T ) -> :cover:`~lang/types Int` 
        
    .. method:: lastIndexOf (element: T ) -> :cover:`~lang/types Int` 
        
    .. method:: removeAt (index: :cover:`~lang/types Int` ) -> T 
        
    .. method:: remove (element: T ) -> :cover:`~lang/types Bool` 
        
        Removes a single instance of the specified element from this list,
        if it is present (optional operation).
        @return true if at least one occurence of the element has been
        removed
        
        
    .. method:: set (index: :cover:`~lang/types Int` , element: T ) -> T 
        
        Replaces the element at the specified position in this list with
        the specified element.
        
        
    .. method:: size -> :cover:`~lang/types Int` 
        
        @return the number of elements in this list.
        
        
    .. method:: ensureCapacity (newSize: :cover:`~lang/types Int` )
        
        Increases the capacity of this ArrayList instance, if necessary,
        to ensure that it can hold at least the number of elements
        specified by the minimum capacity argument.
        
        
    .. method:: grow
        
        private
        
    .. method:: checkIndex (index: :cover:`~lang/types Int` )
        
        private
        
    .. method:: iterator -> :class:`~lang/types Iterator<T>` 
        
    .. method:: clone -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. method:: toArray -> :cover:`~lang/types Pointer` 
        
        
        
    .. field:: data -> T *
    
    .. field:: capacity -> :cover:`~lang/types Int` 
    
    .. field:: size -> :cover:`~lang/types Int` 
    
.. class:: ArrayListIterator<T>
    
    :extends: :class:`~lang/types Iterator<T>` 
    .. staticmethod:: new~iter (list: :class:`~structs/ArrayList ArrayList<T>` ) -> :class:`~structs/ArrayList ArrayListIterator<T>` 
        
    .. method:: init~iter (list: :class:`~structs/ArrayList ArrayList<T>` )
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: next -> T 
        
    .. method:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. method:: prev -> T 
        
    .. method:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: list -> :class:`~structs/ArrayList ArrayList<T>` 
    
    .. field:: index -> :cover:`~lang/types Int` 
    
