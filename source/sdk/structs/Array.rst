structs/Array
=============

.. module:: structs/Array

.. class:: Array<T>
    
    .. staticmemberfunction:: new (size: :cover:`~lang/types SizeT`) -> :class:`~structs/Array Array<T>`
        
    .. memberfunction:: init (size: :cover:`~lang/types SizeT`)
        
    .. staticmemberfunction:: new~withData (data: :cover:`~lang/types Pointer`, size: :cover:`~lang/types SizeT`) -> :class:`~structs/Array Array<T>`
        
    .. memberfunction:: init~withData (data: :cover:`~lang/types Pointer`, size: :cover:`~lang/types SizeT`)
        
    .. memberfunction:: get (i: :cover:`~lang/types Int`) -> T
        
    .. memberfunction:: set (i: :cover:`~lang/types Int`, value: T)
        
    .. memberfunction:: size -> :cover:`~lang/types Int`
        
    .. memberfunction:: iterator -> :class:`~lang/types Iterator<T>`
        
    .. memberfunction:: lastIndex -> :cover:`~lang/types SizeT`
        
    .. memberfunction:: isEmpty -> :cover:`~lang/types Bool`
        
    .. memberfunction:: each (f: Func)
        
    .. field:: size -> :cover:`~lang/types SizeT`
    
    .. field:: data -> T*
    
.. class:: ArrayIterator<T>
    
    .. staticmemberfunction:: new (array: :class:`~structs/Array Array<T>`) -> :class:`~structs/Array ArrayIterator<T>`
        
    .. memberfunction:: init (array: :class:`~structs/Array Array<T>`)
        
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool`
        
    .. memberfunction:: next -> T
        
    .. memberfunction:: hasPrev -> :cover:`~lang/types Bool`
        
    .. memberfunction:: prev -> T
        
    .. memberfunction:: remove -> :cover:`~lang/types Bool`
        
    .. field:: T -> :class:`~lang/types Class`
    
    .. field:: array -> :class:`~structs/Array Array<T>`
    
    .. field:: i -> :cover:`~lang/types Int`
    
