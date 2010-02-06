structs/Array
=============

.. module:: structs/Array

.. class:: Array<T>
    
    .. staticmemberfunction:: new (size: SizeT) -> Array<T>
        
    .. memberfunction:: init (size: SizeT)
        
    .. staticmemberfunction:: new~withData (data: Pointer, size: SizeT) -> Array<T>
        
    .. memberfunction:: init~withData (data: Pointer, size: SizeT)
        
    .. memberfunction:: get (i: Int) -> T
        
    .. memberfunction:: set (i: Int, value: T)
        
    .. memberfunction:: size -> Int
        
    .. memberfunction:: iterator -> Iterator<T>
        
    .. memberfunction:: lastIndex -> SizeT
        
    .. memberfunction:: isEmpty -> Bool
        
    .. memberfunction:: each (f: Func)
        
    .. field:: size -> SizeT
    
    .. field:: data -> T*
    
.. class:: ArrayIterator<T>
    
    .. staticmemberfunction:: new (array: Array<T>) -> ArrayIterator<T>
        
    .. memberfunction:: init (array: Array<T>)
        
    .. memberfunction:: hasNext -> Bool
        
    .. memberfunction:: next -> T
        
    .. memberfunction:: hasPrev -> Bool
        
    .. memberfunction:: prev -> T
        
    .. memberfunction:: remove -> Bool
        
    .. field:: T -> Class
    
    .. field:: array -> Array<T>
    
    .. field:: i -> Int
    
