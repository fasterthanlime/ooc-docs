lang/types
==========

.. module:: lang/types

.. function:: atoi (:cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
    
.. function:: atol (:cover:`~lang/types String` ) -> :cover:`~lang/types Long` 
    
.. cover:: Void
    
    :from: ``void``
.. cover:: Pointer
    
    :from: ``void*``
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
.. cover:: Char
    
    :from: ``char``
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
    
    :extends: :cover:`~lang/types Char` 
    :from: ``signed char``
.. cover:: UChar
    
    :extends: :cover:`~lang/types Char` 
    :from: ``unsigned char``
.. cover:: WChar
    
    :from: ``wchar_t``
.. cover:: String
    
    :from: ``Char*``
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
        
    .. memberfunction:: trim~string (s: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
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
    
    :from: ``signed long long``
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. memberfunction:: toHexString -> :cover:`~lang/types String` 
        
    .. memberfunction:: isOdd -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isEven -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: in (range: :cover:`~lang/types Range` ) -> :cover:`~lang/types Bool` 
        
.. cover:: Long
    
    :extends: :cover:`~lang/types LLong` 
    :from: ``signed long``
.. cover:: Int
    
    :extends: :cover:`~lang/types LLong` 
    :from: ``signed int``
.. cover:: Short
    
    :extends: :cover:`~lang/types LLong` 
    :from: ``signed short``
.. cover:: ULLong
    
    :extends: :cover:`~lang/types LLong` 
    :from: ``unsigned long long``
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. memberfunction:: in (range: :cover:`~lang/types Range` ) -> :cover:`~lang/types Bool` 
        
.. cover:: ULong
    
    :extends: :cover:`~lang/types ULLong` 
    :from: ``unsigned long``
.. cover:: UInt
    
    :extends: :cover:`~lang/types ULLong` 
    :from: ``unsigned int``
.. cover:: UShort
    
    :extends: :cover:`~lang/types ULLong` 
    :from: ``unsigned short``
.. cover:: Int8
    
    :extends: :cover:`~lang/types LLong` 
    :from: ``int8_t``
.. cover:: Int16
    
    :extends: :cover:`~lang/types LLong` 
    :from: ``int16_t``
.. cover:: Int32
    
    :extends: :cover:`~lang/types LLong` 
    :from: ``int32_t``
.. cover:: Int64
    
    :extends: :cover:`~lang/types LLong` 
    :from: ``int64_t``
.. cover:: UInt8
    
    :extends: :cover:`~lang/types ULLong` 
    :from: ``uint8_t``
.. cover:: UInt16
    
    :extends: :cover:`~lang/types ULLong` 
    :from: ``uint16_t``
.. cover:: UInt32
    
    :extends: :cover:`~lang/types ULLong` 
    :from: ``uint32_t``
.. cover:: UInt64
    
    :extends: :cover:`~lang/types ULLong` 
    :from: ``uint64_t``
.. cover:: Octet
    
    :extends: :cover:`~lang/types ULLong` 
    :from: ``UInt8``
.. cover:: SizeT
    
    :extends: :cover:`~lang/types LLong` 
    :from: ``size_t``
.. cover:: PtrDiffT
    
    :extends: :cover:`~lang/types LLong` 
    :from: ``ptrdiff_t``
.. cover:: Bool
    
    :from: ``bool``
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
.. cover:: Float
    
    :extends: :cover:`~lang/types LDouble` 
    :from: ``float``
.. cover:: Double
    
    :extends: :cover:`~lang/types LDouble` 
    :from: ``double``
.. cover:: LDouble
    
    :from: ``long double``
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. memberfunction:: abs -> :cover:`~lang/types LDouble` 
        
.. cover:: Range
    
    .. memberfunction:: new (min, max: :cover:`~lang/types Int` ) -> :cover:`~lang/types Range` 
        
.. class:: Class
    
    :extends: :class:`~lang/types Object` 
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
    
    :extends: :class:`~lang/types Object` 
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: next -> T 
        
    .. memberfunction:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: prev -> T 
        
    .. memberfunction:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: T -> :class:`~lang/types Class` 
    
.. class:: Iterable<T>
    
    :extends: :class:`~lang/types Object` 
    .. memberfunction:: iterator -> :class:`~lang/types Iterator<T>` 
        
    .. memberfunction:: toArrayList -> :class:`~structs/ArrayList ArrayList<T>` 
        
        @return the contents of the iterable as ArrayList.
        
        
    .. field:: T -> :class:`~lang/types Class` 
    
.. class:: Interface
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new (realThis, funcs: :class:`~lang/types Object` ) -> :class:`~lang/types Interface` 
        
    .. memberfunction:: init (realThis, funcs: :class:`~lang/types Object` )
        
    .. field:: realThis -> :class:`~lang/types Object` 
    
    .. field:: funcs -> :class:`~lang/types Object` 
    
.. class:: Exception
    
    :extends: :class:`~lang/types Object` 
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
    
    :extends: :class:`~lang/types Iterator<T>` 
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
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new -> :class:`~lang/types None` 
        
    .. memberfunction:: init
        
.. class:: Cell<T>
    
    :extends: :class:`~lang/types Object` 
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

