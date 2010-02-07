lang/types
==========

.. module:: lang/types

.. function:: atoi (:cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
    
.. function:: atol (:cover:`~lang/types String` ) -> :cover:`~lang/types Long` 
    
.. cover:: Void
    
.. cover:: Pointer
    
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
.. cover:: Char
    
    .. memberfunction:: isAlphaNumeric -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isAlpha -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isLower -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isUpper -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isDigit -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isHexDigit -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isControl -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isGraph -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isPrintable -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isPunctuation -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isWhitespace -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isBlank -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: toInt -> :cover:`~lang/types Int` 
        
    .. memberfunction:: toLower -> :cover:`~lang/types Char` 
        
    .. memberfunction:: toUpper -> :cover:`~lang/types Char` 
        
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. memberfunction:: print
        
    .. memberfunction:: println
        
.. cover:: SChar
    
.. cover:: UChar
    
.. cover:: WChar
    
.. cover:: String
    
    .. memberfunction:: new~withLength (length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: new~withChar (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: compare (other: :cover:`~lang/types String` , start, length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Bool` 
        
        compare `length` characters of `this` with `other`, starting at `start`. 
        
    .. memberfunction:: compare~implicitLength (other: :cover:`~lang/types String` , start: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: compare~whole (other: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: length -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: equals (other: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: toInt -> :cover:`~lang/types Int` 
        
    .. memberfunction:: toLong -> :cover:`~lang/types Long` 
        
    .. memberfunction:: toLLong -> :cover:`~lang/types LLong` 
        
    .. memberfunction:: toDouble -> :cover:`~lang/types Double` 
        
    .. memberfunction:: toFloat -> :cover:`~lang/types Float` 
        
    .. memberfunction:: isEmpty -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: startsWith (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: startsWith~withChar (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: endsWith (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: indexOf~charZero (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: indexOf~char (c: :cover:`~lang/types Char` , start: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: indexOf~stringZero (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: indexOf~string (s: :cover:`~lang/types String` , start: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: contains~char (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: contains~string (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: trim~space -> :cover:`~lang/types String` 
        
    .. memberfunction:: trim (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: first -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: lastIndex -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: last -> :cover:`~lang/types Char` 
        
    .. memberfunction:: lastIndexOf (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: substring~tillEnd (start: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: substring (start, end: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: reverse -> :cover:`~lang/types String` 
        
    .. memberfunction:: print
        
    .. memberfunction:: println
        
    .. memberfunction:: times (count: :cover:`~lang/types Int` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: clone -> :cover:`~lang/types String` 
        
    .. memberfunction:: append (other: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: append~char (other: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: count~char (what: :cover:`~lang/types Char` ) -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: count~string (what: :cover:`~lang/types String` ) -> :cover:`~lang/types SizeT` 
        
    .. memberfunction:: replace (oldie, kiddo: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: replace~string (oldie, kiddo: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: prepend (other: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: prepend~char (other: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
    .. memberfunction:: toLower -> :cover:`~lang/types String` 
        
    .. memberfunction:: toUpper -> :cover:`~lang/types String` 
        
    .. memberfunction:: charAt (index: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Char` 
        
    .. memberfunction:: format (...) -> :cover:`~lang/types String` 
        
    .. memberfunction:: scanf (format: :cover:`~lang/types String` , ...) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: iterator -> :class:`~lang/types StringIterator<T>` 
        
.. cover:: LLong
    
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. memberfunction:: toHexString -> :cover:`~lang/types String` 
        
    .. memberfunction:: isOdd -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isEven -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: in (range: :cover:`~lang/types Range` ) -> :cover:`~lang/types Bool` 
        
.. cover:: Long
    
.. cover:: Int
    
.. cover:: Short
    
.. cover:: ULLong
    
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. memberfunction:: in (range: :cover:`~lang/types Range` ) -> :cover:`~lang/types Bool` 
        
.. cover:: ULong
    
.. cover:: UInt
    
.. cover:: UShort
    
.. cover:: Int8
    
.. cover:: Int16
    
.. cover:: Int32
    
.. cover:: Int64
    
.. cover:: UInt8
    
.. cover:: UInt16
    
.. cover:: UInt32
    
.. cover:: UInt64
    
.. cover:: Octet
    
.. cover:: SizeT
    
.. cover:: PtrDiffT
    
.. cover:: Bool
    
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
.. cover:: Float
    
.. cover:: Double
    
.. cover:: LDouble
    
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. memberfunction:: abs -> :cover:`~lang/types LDouble` 
        
.. cover:: Range
    
    .. memberfunction:: new (min, max: :cover:`~lang/types Int` ) -> :cover:`~lang/types Range` 
        
.. class:: Class
    
    .. memberfunction:: alloc -> :class:`~lang/types Object` 
        
    .. memberfunction:: inheritsFrom (T: :class:`~lang/types Class` ) -> :cover:`~lang/types Bool` 
        
    .. field:: instanceSize -> :cover:`~lang/types SizeT` 
    
    .. field:: size -> :cover:`~lang/types SizeT` 
    
    .. field:: name -> :cover:`~lang/types String` 
    
    .. field:: super -> :class:`~lang/types Class` 
    
    .. field:: __defaults__ -> Func 
    
    .. field:: __destroy__ -> Func 
    
    .. field:: __load__ -> Func 
    
.. class:: Object
    
    .. memberfunction:: instanceOf (T: :class:`~lang/types Class` ) -> :cover:`~lang/types Bool` 
        
    .. field:: class -> :class:`~lang/types Class` 
    
.. class:: Iterator<T>
    
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: next -> T 
        
    .. memberfunction:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: prev -> T 
        
    .. memberfunction:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: T -> :class:`~lang/types Class` 
    
.. class:: Iterable<T>
    
    .. memberfunction:: iterator -> :class:`~lang/types Iterator<T>` 
        
    .. memberfunction:: toArrayList -> :class:`~structs/ArrayList ArrayList<T>` 
        
        @return the contents of the iterable as ArrayList.
        
        
    .. field:: T -> :class:`~lang/types Class` 
    
.. class:: Interface
    
    .. staticmemberfunction:: new (realThis, funcs: :class:`~lang/types Object` ) -> :class:`~lang/types Interface` 
        
    .. memberfunction:: init (realThis, funcs: :class:`~lang/types Object` )
        
    .. field:: realThis -> :class:`~lang/types Object` 
    
    .. field:: funcs -> :class:`~lang/types Object` 
    
.. class:: Exception
    
    .. staticmemberfunction:: new (origin: :class:`~lang/types Class` , msg: :cover:`~lang/types String` ) -> :class:`~lang/types Exception` 
        
    .. memberfunction:: init (origin: :class:`~lang/types Class` , msg: :cover:`~lang/types String` )
        
    .. staticmemberfunction:: new~noOrigin (msg: :cover:`~lang/types String` ) -> :class:`~lang/types Exception` 
        
    .. memberfunction:: init~noOrigin (msg: :cover:`~lang/types String` )
        
    .. memberfunction:: crash
        
    .. memberfunction:: getMessage -> :cover:`~lang/types String` 
        
    .. memberfunction:: print
        
    .. memberfunction:: throw
        
    .. field:: origin -> :class:`~lang/types Class` 
    
    .. field:: msg -> :cover:`~lang/types String` 
    
.. class:: StringIterator<T>
    
    .. staticmemberfunction:: new (str: :cover:`~lang/types String` ) -> :class:`~lang/types StringIterator<T>` 
        
    .. memberfunction:: init (str: :cover:`~lang/types String` )
        
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: next -> T 
        
    .. memberfunction:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: prev -> T 
        
    .. memberfunction:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: i -> :cover:`~lang/types Int` 
    
    .. field:: str -> :cover:`~lang/types String` 
    
.. class:: None
    
    .. staticmemberfunction:: new -> :class:`~lang/types None` 
        
    .. memberfunction:: init
        
.. class:: Cell<T>
    
    .. staticmemberfunction:: new (val: T ) -> :class:`~lang/types Cell<T>` 
        
    .. memberfunction:: init (val: T )
        
    .. field:: T -> :class:`~lang/types Class` 
    
    .. field:: val -> T 
    
.. var:: DBL_MAX -> :cover:`~lang/types Double` 

.. var:: DBL_MIN -> :cover:`~lang/types Double` 

.. var:: FLT_MAX -> :cover:`~lang/types Float` 

.. var:: FLT_MIN -> :cover:`~lang/types Float` 

.. var:: LDBL_MAX -> :cover:`~lang/types LDouble` 

.. var:: LDBL_MIN -> :cover:`~lang/types LDouble` 

