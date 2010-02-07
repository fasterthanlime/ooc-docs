structs/List
============

.. module:: structs/List

.. class:: List<T>
    
    :extends: :class:`~lang/types Iterable<T>` 
    .. memberfunction:: add (element: T )
        
        Appends the specified element to the end of this list.
        
        
    .. memberfunction:: add~withIndex (index: :cover:`~lang/types Int` , element: T )
        
        Inserts the specified element at the specified position in
        this list. 
        
        
    .. memberfunction:: addAll (list: :class:`~lang/types Iterable<T>` )
        
        Appends all of the elements in the specified Collection to the
        end of this list, in the order that they are returned by the
        specified Collection's Iterator.
        
        
    .. memberfunction:: addAll~atStart (start: :cover:`~lang/types Int` , list: :class:`~lang/types Iterable<T>` )
        
        Inserts all of the elements in the specified Collection into
        this list, starting at the specified position.
        
        
    .. memberfunction:: clear
        
        Removes all of the elements from this list.
        
        
    .. memberfunction:: removeLast -> :cover:`~lang/types Bool` 
        
        Removes the last element of the list, if any (=non-empty list).
        @return true if it has removed an element, false if the list
        was empty.
        
        
    .. memberfunction:: contains (element: T ) -> :cover:`~lang/types Bool` 
        
        @return true if this list contains the specified element.
        
        
    .. memberfunction:: replace (oldie, kiddo: T ) -> :cover:`~lang/types Bool` 
        
        @return true if oldie has been replaced by kiddo
        
        
    .. memberfunction:: get (index: :cover:`~lang/types Int` ) -> T 
        
        @return the element at the specified position in this list.
        
        
    .. memberfunction:: indexOf (element: T ) -> :cover:`~lang/types Int` 
        
        @return the index of the first occurence of the given argument,
        (testing for equality using the equals method), or -1 if not found
        
        
    .. memberfunction:: isEmpty -> :cover:`~lang/types Bool` 
        
        @return true if this list has no elements.
        
        
    .. memberfunction:: lastIndexOf (element: T ) -> :cover:`~lang/types Int` 
        
        @return the index of the last occurrence of the specified object
        in this list.
        
        
    .. memberfunction:: removeAt (index: :cover:`~lang/types Int` ) -> T 
        
        Removes the element at the specified position in this list.
        @return the element just removed
        
        
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
        
        
    .. memberfunction:: iterator -> :class:`~lang/types Iterator<T>` 
        
        @return an interator on this list
        
        
    .. memberfunction:: clone -> :class:`~structs/List List<T>` 
        
        @return a copy of this list
        
        
    .. memberfunction:: first -> T 
        
        @return the first element of this list
        
        
    .. memberfunction:: last -> T 
        
        @return the last element of this list
        
        
    .. memberfunction:: lastIndex -> :cover:`~lang/types Int` 
        
        @return the last index of this list (e.g. size() - 1)
        
        
    .. memberfunction:: reverse
        
        Reverse this list (destructive)
        
        
    .. memberfunction:: toArray -> :cover:`~lang/types Pointer` 
        
        Convert this list to a raw C array
        
        
    .. memberfunction:: each (f: Func )
        
    .. memberfunction:: join~string (str: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: join~char (chr: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
