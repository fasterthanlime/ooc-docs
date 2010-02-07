structs/ArrayList
=================

.. module:: structs/ArrayList

.. class:: ArrayList<T>
    
    :extends: :class:`~structs/List List<T>` 
    .. staticmemberfunction:: new -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: new~withCapacity (capacity: :cover:`~lang/types Int` ) -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. memberfunction:: init~withCapacity (capacity: :cover:`~lang/types Int` )
        
    .. staticmemberfunction:: new~withData (data: T *, size: :cover:`~lang/types Int` ) -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. memberfunction:: init~withData (data: T *, size: :cover:`~lang/types Int` )
        
    .. memberfunction:: add (element: T )
        
    .. memberfunction:: add~withIndex (index: :cover:`~lang/types Int` , element: T )
        
    .. memberfunction:: clear
        
    .. memberfunction:: get (index: :cover:`~lang/types Int` ) -> T 
        
    .. memberfunction:: indexOf (element: T ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: lastIndexOf (element: T ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: removeAt (index: :cover:`~lang/types Int` ) -> T 
        
    .. memberfunction:: remove (element: T ) -> :cover:`~lang/types Bool` 
        
        Removes a single instance of the specified element from this list,
        if it is present (optional operation).
        @return true if at least one occurence of the element has been
        removed
        
        
    .. memberfunction:: set (index: :cover:`~lang/types Int` , element: T ) -> T 
        
        Replaces the element at the specified position in this list with
        the specified element.
        
        
    .. memberfunction:: size -> :cover:`~lang/types Int` 
        
        @return the number of elements in this list.
        
        
    .. memberfunction:: ensureCapacity (newSize: :cover:`~lang/types Int` )
        
        Increases the capacity of this ArrayList instance, if necessary,
        to ensure that it can hold at least the number of elements
        specified by the minimum capacity argument.
        
        
    .. memberfunction:: grow
        
        private
        
    .. memberfunction:: checkIndex (index: :cover:`~lang/types Int` )
        
        private
        
    .. memberfunction:: iterator -> :class:`~lang/types Iterator<T>` 
        
    .. memberfunction:: clone -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. memberfunction:: toArray -> :cover:`~lang/types Pointer` 
        
        
        
    .. field:: data -> T *
    
    .. field:: capacity -> :cover:`~lang/types Int` 
    
    .. field:: size -> :cover:`~lang/types Int` 
    
.. class:: ArrayListIterator<T>
    
    :extends: :class:`~lang/types Iterator<T>` 
    .. staticmemberfunction:: new (list: :class:`~structs/ArrayList ArrayList<T>` ) -> :class:`~structs/ArrayList ArrayListIterator<T>` 
        
    .. memberfunction:: init (list: :class:`~structs/ArrayList ArrayList<T>` )
        
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: next -> T 
        
    .. memberfunction:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: prev -> T 
        
    .. memberfunction:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: list -> :class:`~structs/ArrayList ArrayList<T>` 
    
    .. field:: index -> :cover:`~lang/types Int` 
    
