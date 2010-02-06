lang/types
==========

.. module:: lang/types

.. function:: atoi (String) -> Int
    
.. function:: atol (String) -> Long
    
.. cover:: Void
    
.. cover:: Pointer
    
    .. memberfunction:: toString -> String
        
.. cover:: Char
    
    .. memberfunction:: isAlphaNumeric -> Bool
        
    .. memberfunction:: isAlpha -> Bool
        
    .. memberfunction:: isLower -> Bool
        
    .. memberfunction:: isUpper -> Bool
        
    .. memberfunction:: isDigit -> Bool
        
    .. memberfunction:: isHexDigit -> Bool
        
    .. memberfunction:: isControl -> Bool
        
    .. memberfunction:: isGraph -> Bool
        
    .. memberfunction:: isPrintable -> Bool
        
    .. memberfunction:: isPunctuation -> Bool
        
    .. memberfunction:: isWhitespace -> Bool
        
    .. memberfunction:: isBlank -> Bool
        
    .. memberfunction:: toInt -> Int
        
    .. memberfunction:: toLower -> Char
        
    .. memberfunction:: toUpper -> Char
        
    .. memberfunction:: toString -> String
        
    .. memberfunction:: print
        
    .. memberfunction:: println
        
.. cover:: SChar
    
.. cover:: UChar
    
.. cover:: WChar
    
.. cover:: String
    
    .. memberfunction:: new~withLength (length: SizeT) -> String
        
    .. memberfunction:: new~withChar (c: Char) -> String
        
    .. memberfunction:: compare (other: String, start, length: SizeT) -> Bool
        
        compare `length` characters of `this` with `other`, starting at `start`. 
        
    .. memberfunction:: compare~implicitLength (other: String, start: SizeT) -> Bool
        
    .. memberfunction:: compare~whole (other: String) -> Bool
        
    .. memberfunction:: length -> SizeT
        
    .. memberfunction:: equals (other: String) -> Bool
        
    .. memberfunction:: toInt -> Int
        
    .. memberfunction:: toLong -> Long
        
    .. memberfunction:: toLLong -> LLong
        
    .. memberfunction:: toDouble -> Double
        
    .. memberfunction:: toFloat -> Float
        
    .. memberfunction:: isEmpty -> Bool
        
    .. memberfunction:: startsWith (s: String) -> Bool
        
    .. memberfunction:: startsWith~withChar (c: Char) -> Bool
        
    .. memberfunction:: endsWith (s: String) -> Bool
        
    .. memberfunction:: indexOf~charZero (c: Char) -> Int
        
    .. memberfunction:: indexOf~char (c: Char, start: Int) -> Int
        
    .. memberfunction:: indexOf~stringZero (s: String) -> Int
        
    .. memberfunction:: indexOf~string (s: String, start: Int) -> Int
        
    .. memberfunction:: contains~char (c: Char) -> Bool
        
    .. memberfunction:: contains~string (s: String) -> Bool
        
    .. memberfunction:: trim~space -> String
        
    .. memberfunction:: trim (c: Char) -> String
        
    .. memberfunction:: first -> SizeT
        
    .. memberfunction:: lastIndex -> SizeT
        
    .. memberfunction:: last -> Char
        
    .. memberfunction:: lastIndexOf (c: Char) -> SizeT
        
    .. memberfunction:: substring~tillEnd (start: SizeT) -> String
        
    .. memberfunction:: substring (start, end: SizeT) -> String
        
    .. memberfunction:: reverse -> String
        
    .. memberfunction:: print
        
    .. memberfunction:: println
        
    .. memberfunction:: times (count: Int) -> String
        
    .. memberfunction:: clone -> String
        
    .. memberfunction:: append (other: String) -> String
        
    .. memberfunction:: append~char (other: Char) -> String
        
    .. memberfunction:: count~char (what: Char) -> SizeT
        
    .. memberfunction:: count~string (what: String) -> SizeT
        
    .. memberfunction:: replace (oldie, kiddo: Char) -> String
        
    .. memberfunction:: replace~string (oldie, kiddo: String) -> String
        
    .. memberfunction:: prepend (other: String) -> String
        
    .. memberfunction:: prepend~char (other: Char) -> String
        
    .. memberfunction:: toLower -> String
        
    .. memberfunction:: toUpper -> String
        
    .. memberfunction:: charAt (index: SizeT) -> Char
        
    .. memberfunction:: format (...) -> String
        
    .. memberfunction:: scanf (format: String, ...) -> Int
        
    .. memberfunction:: iterator -> StringIterator<T>
        
.. cover:: LLong
    
    .. memberfunction:: toString -> String
        
    .. memberfunction:: toHexString -> String
        
    .. memberfunction:: isOdd -> Bool
        
    .. memberfunction:: isEven -> Bool
        
    .. memberfunction:: in (range: Range) -> Bool
        
.. cover:: Long
    
.. cover:: Int
    
.. cover:: Short
    
.. cover:: ULLong
    
    .. memberfunction:: toString -> String
        
    .. memberfunction:: in (range: Range) -> Bool
        
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
    
    .. memberfunction:: toString -> String
        
.. cover:: Float
    
.. cover:: Double
    
.. cover:: LDouble
    
    .. memberfunction:: toString -> String
        
    .. memberfunction:: abs -> LDouble
        
.. cover:: Range
    
    .. memberfunction:: new (min, max: Int) -> Range
        
.. class:: Class
    
    .. memberfunction:: alloc -> Object
        
    .. memberfunction:: inheritsFrom (T: Class) -> Bool
        
    .. field:: instanceSize
    
    .. field:: size
    
    .. field:: name
    
    .. field:: super
    
    .. field:: __defaults__
    
    .. field:: __destroy__
    
    .. field:: __load__
    
.. class:: Object
    
    .. memberfunction:: instanceOf (T: Class) -> Bool
        
    .. field:: class
    
.. class:: Interface
    
    .. staticmemberfunction:: new (realThis, funcs: Object) -> Interface
        
    .. memberfunction:: init (realThis, funcs: Object)
        
    .. field:: realThis
    
    .. field:: funcs
    
.. class:: Exception
    
    .. staticmemberfunction:: new (origin: Class, msg: String) -> Exception
        
    .. memberfunction:: init (origin: Class, msg: String)
        
    .. staticmemberfunction:: new~noOrigin (msg: String) -> Exception
        
    .. memberfunction:: init~noOrigin (msg: String)
        
    .. memberfunction:: crash
        
    .. memberfunction:: getMessage -> String
        
    .. memberfunction:: print
        
    .. memberfunction:: throw
        
    .. field:: origin
    
    .. field:: msg
    
.. class:: None
    
    .. staticmemberfunction:: new -> None
        
    .. memberfunction:: init
        
.. class:: Cell<T>
    
    .. staticmemberfunction:: new (val: T) -> Cell<T>
        
    .. memberfunction:: init (val: T)
        
    .. field:: T
    
    .. field:: val
    
.. data:: DBL_MAX

.. data:: DBL_MIN

.. data:: FLT_MAX

.. data:: FLT_MIN

.. data:: LDBL_MAX

.. data:: LDBL_MIN

