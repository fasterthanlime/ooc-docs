structs/List
============

.. module:: structs/List

.. class:: List<T>
    
    :extends: :class:`~lang/types Iterable<T>` 
    .. method:: add (element: T )
        
        Appends the specified element to the end of this list.
        
        
    .. method:: add~withIndex (index: :cover:`~lang/types Int` , element: T )
        
        Inserts the specified element at the specified position in
        this list. 
        
        
    .. method:: addAll (list: :class:`~lang/types Iterable<T>` )
        
        Appends all of the elements in the specified Collection to the
        end of this list, in the order that they are returned by the
        specified Collection's Iterator.
        
        
    .. method:: addAll~atStart (start: :cover:`~lang/types Int` , list: :class:`~lang/types Iterable<T>` )
        
        Inserts all of the elements in the specified Collection into
        this list, starting at the specified position.
        
        
    .. method:: clear
        
        Removes all of the elements from this list.
        
        
    .. method:: removeLast -> :cover:`~lang/types Bool` 
        
        Removes the last element of the list, if any (=non-empty list).
        @return true if it has removed an element, false if the list
        was empty.
        
        
    .. method:: contains (element: T ) -> :cover:`~lang/types Bool` 
        
        @return true if this list contains the specified element.
        
        
    .. method:: replace (oldie, kiddo: T ) -> :cover:`~lang/types Bool` 
        
        @return true if oldie has been replaced by kiddo
        
        
    .. method:: get (index: :cover:`~lang/types Int` ) -> T 
        
        @return the element at the specified position in this list.
        
        
    .. method:: indexOf (element: T ) -> :cover:`~lang/types Int` 
        
        @return the index of the first occurence of the given argument,
        (testing for equality using the equals method), or -1 if not found
        
        
    .. method:: isEmpty -> :cover:`~lang/types Bool` 
        
        @return true if this list has no elements.
        
        
    .. method:: lastIndexOf (element: T ) -> :cover:`~lang/types Int` 
        
        @return the index of the last occurrence of the specified object
        in this list.
        
        
    .. method:: removeAt (index: :cover:`~lang/types Int` ) -> T 
        
        Removes the element at the specified position in this list.
        @return the element just removed
        
        
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
        
        
    .. method:: iterator -> :class:`~lang/types Iterator<T>` 
        
        @return an interator on this list
        
        
    .. method:: clone -> :class:`~structs/List List<T>` 
        
        @return a copy of this list
        
        
    .. method:: first -> T 
        
        @return the first element of this list
        
        
    .. method:: last -> T 
        
        @return the last element of this list
        
        
    .. method:: lastIndex -> :cover:`~lang/types Int` 
        
        @return the last index of this list (e.g. size() - 1)
        
        
    .. method:: reverse
        
        Reverse this list (destructive)
        
        
    .. method:: toArray -> :cover:`~lang/types Pointer` 
        
        Convert this list to a raw C array
        
        
    .. method:: each (f: Func )
        
    .. method:: join~string (str: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
    .. method:: join~char (chr: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
