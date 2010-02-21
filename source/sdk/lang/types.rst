lang/types
==========

.. module:: lang/types

.. function:: strtol (:cover:`~lang/types String` , :cover:`~lang/types Pointer` , :cover:`~lang/types Int` ) -> :cover:`~lang/types Long` 
    
.. function:: strtoll (:cover:`~lang/types String` , :cover:`~lang/types Pointer` , :cover:`~lang/types Int` ) -> :cover:`~lang/types LLong` 
    
.. function:: strtoul (:cover:`~lang/types String` , :cover:`~lang/types Pointer` , :cover:`~lang/types Int` ) -> :cover:`~lang/types ULong` 
    
.. function:: strtof (:cover:`~lang/types String` , :cover:`~lang/types Pointer` ) -> :cover:`~lang/types Float` 
    
.. function:: strtod (:cover:`~lang/types String` , :cover:`~lang/types Pointer` ) -> :cover:`~lang/types Double` 
    
.. function:: strtold (:cover:`~lang/types String` , :cover:`~lang/types Pointer` ) -> :cover:`~lang/types LDouble` 
    
.. cover:: Void
    
    :from: ``void``
.. cover:: Pointer
    
    :from: ``void*``
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
.. cover:: Char
    
    :from: ``char``
    .. memberfunction:: isAlphaNumeric -> :cover:`~lang/types Bool` 
        
        check for an alphanumeric character
        
    .. memberfunction:: isAlpha -> :cover:`~lang/types Bool` 
        
        check for an alphabetic character
        
    .. memberfunction:: isLower -> :cover:`~lang/types Bool` 
        
        check for a lowercase alphabetic character
        
    .. memberfunction:: isUpper -> :cover:`~lang/types Bool` 
        
        check for an uppercase alphabetic character
        
    .. memberfunction:: isDigit -> :cover:`~lang/types Bool` 
        
        check for a decimal digit (0 through 9)
        
    .. memberfunction:: isHexDigit -> :cover:`~lang/types Bool` 
        
        check for a hexadecimal digit (0 1 2 3 4 5 6 7 8 9 a b c d e f A B C D E F)
        
    .. memberfunction:: isControl -> :cover:`~lang/types Bool` 
        
        check for a control character
        
    .. memberfunction:: isGraph -> :cover:`~lang/types Bool` 
        
        check for any printable character except space
        
    .. memberfunction:: isPrintable -> :cover:`~lang/types Bool` 
        
        check for any printable character including space
        
    .. memberfunction:: isPunctuation -> :cover:`~lang/types Bool` 
        
        check for any printable character which is not a space or an alphanumeric character
        
    .. memberfunction:: isWhitespace -> :cover:`~lang/types Bool` 
        
        check for white-space characters: space, form-feed ('\\f'), newline ('\\n'),
        carriage return ('\\r'), horizontal tab ('\\t'), and vertical tab ('\\v') 
        
    .. memberfunction:: isBlank -> :cover:`~lang/types Bool` 
        
        check for a blank character; that is, a space or a tab
        
    .. memberfunction:: toInt -> :cover:`~lang/types Int` 
        
        convert to an integer. This only works for digits, otherwise -1 is returned
        
    .. memberfunction:: toLower -> :cover:`~lang/types Char` 
        
        return the lowered character
        
    .. memberfunction:: toUpper -> :cover:`~lang/types Char` 
        
        return the capitalized character
        
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
        return a one-character string containing this character.
        
    .. memberfunction:: print
        
        write this character to stdout without a following newline.
        
    .. memberfunction:: println
        
        write this character to stdout, followed by a newline
        
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
        
        Create a new string exactly *length* characters long (without the nullbyte).
        The contents of the string are undefined. 
        
    .. memberfunction:: new~withChar (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        Create a new string of the length 1 containing only the character *c
        
    .. memberfunction:: compare (other: :cover:`~lang/types String` , start, length: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Bool` 
        
        compare *length* characters of *this* with *other*, starting at *start*.
        Return true if the two strings are equal, return false if they are not. 
        
    .. memberfunction:: compare~implicitLength (other: :cover:`~lang/types String` , start: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Bool` 
        
        compare *this* with *other*, starting at *start*. The count of compared
        characters is determined by *other*'s length. 
        
    .. memberfunction:: compare~whole (other: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        compare *this* with *other*, starting at 0. Compare ``other length()`` characters.
        
    .. memberfunction:: length -> :cover:`~lang/types SizeT` 
        
        return the string's length, excluding the null byte.
        
    .. memberfunction:: equals (other: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        return true if *other* and *this* are equal. This also returns false if either
        of these two is ``null``. 
        
    .. memberfunction:: toInt -> :cover:`~lang/types Int` 
        
        convert the string's contents to Int.
        
    .. memberfunction:: toInt~withBase (base: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. memberfunction:: toLong -> :cover:`~lang/types Long` 
        
        convert the string's contents to Long.
        
    .. memberfunction:: toLong~withBase (base: :cover:`~lang/types Long` ) -> :cover:`~lang/types Long` 
        
    .. memberfunction:: toLLong -> :cover:`~lang/types LLong` 
        
        convert the string's contents to Long Long.
        
    .. memberfunction:: toLLong~withBase (base: :cover:`~lang/types LLong` ) -> :cover:`~lang/types LLong` 
        
    .. memberfunction:: toULong -> :cover:`~lang/types ULong` 
        
        convert the string's contents to Unsigned Long.
        
    .. memberfunction:: toULong~withBase (base: :cover:`~lang/types ULong` ) -> :cover:`~lang/types ULong` 
        
    .. memberfunction:: toFloat -> :cover:`~lang/types Float` 
        
        convert the string's contents to Float.
        
    .. memberfunction:: toDouble -> :cover:`~lang/types Double` 
        
        convert the string's contents to Double.
        
    .. memberfunction:: toLDouble -> :cover:`~lang/types LDouble` 
        
        convert the string's contents to Long Double.
        
    .. memberfunction:: isEmpty -> :cover:`~lang/types Bool` 
        
        return true if the string is empty or ``null``.
        
    .. memberfunction:: startsWith (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        return true if the first characters of *this* are equal to *s*.
        
    .. memberfunction:: startsWith~withChar (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Bool` 
        
        return true if the first character of *this* is equal to *c*.
        
    .. memberfunction:: endsWith (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        return true if the last characters of *this* are equal to *s*.
        
    .. memberfunction:: indexOf~charZero (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Int` 
        
        return the index of *c*, starting at 0. If *this* does not contain
        c*, return -1. 
        
    .. memberfunction:: indexOf~char (c: :cover:`~lang/types Char` , start: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
        return the index of *c*, but only check characters ``start..length``.
        However, the return value is the index of the *c* relative to the
        string's beginning. If *this* does not contain *c*, return -1. 
        
    .. memberfunction:: indexOf~stringZero (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
        return the index of *s*, starting at 0. If *this* does not contain *s*,
        return -1. 
        
    .. memberfunction:: indexOf~string (s: :cover:`~lang/types String` , start: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
        return the index of *s*, but only check characters ``start..length``.
        However, the return value is relative to the *this*' first character.
        If *this* does not contain *c*, return -1. 
        
    .. memberfunction:: contains~char (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Bool` 
        
        return *true* if *this* contains the character *c
        
    .. memberfunction:: contains~string (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        return *true* if *this* contains the string *s
        
    .. memberfunction:: trim~space -> :cover:`~lang/types String` 
        
        return a copy of *this* with space characters (ASCII 32) stripped at both ends.
        
    .. memberfunction:: trim (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        return a copy of *this* with *c* characters stripped at both ends.
        
    .. memberfunction:: trim~string (s: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        return a copy of *this* with all characters contained by *s* stripped
        at both ends. 
        
    .. memberfunction:: first -> :cover:`~lang/types Char` 
        
        return the first character of *this*. If *this* is empty, 0 is returned.
        
    .. memberfunction:: lastIndex -> :cover:`~lang/types SizeT` 
        
        return the index of the last character of *this*. If *this* is empty,
        -1 is returned. 
        
    .. memberfunction:: last -> :cover:`~lang/types Char` 
        
        return the last character of *this*.
        
    .. memberfunction:: lastIndexOf (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Int` 
        
        return the index of the last occurence of *c* in *this*.
        If *this* does not contain *c*, return -1. 
        
    .. memberfunction:: substring~tillEnd (start: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types String` 
        
        return a substring of *this* only containing the characters
        in the range ``start..length``.  
        
    .. memberfunction:: substring (start, end: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types String` 
        
        return a substring of *this* only containing the characters in the
        range ``start..end``. 
        
    .. memberfunction:: reverse -> :cover:`~lang/types String` 
        
        return a reversed copy of *this*.
        
    .. memberfunction:: print
        
        print *this* to stdout without a following newline. Flush stdout.
        
    .. memberfunction:: println
        
        print *this* followed by a newline.
        
    .. memberfunction:: times (count: :cover:`~lang/types Int` ) -> :cover:`~lang/types String` 
        
        return a string that contains *this*, repeated *count* times.
        
    .. memberfunction:: clone -> :cover:`~lang/types String` 
        
        return a copy of *this*.
        
    .. memberfunction:: append (other: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        return a string that contains *this* followed by *other*.
        
    .. memberfunction:: append~char (other: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        return a string containing *this* followed by *other*.
        
    .. memberfunction:: count~char (what: :cover:`~lang/types Char` ) -> :cover:`~lang/types SizeT` 
        
        return the number of *what*'s occurences in *this*.
        
    .. memberfunction:: count~string (what: :cover:`~lang/types String` ) -> :cover:`~lang/types SizeT` 
        
        return the number of *what*'s non-overlapping occurences in *this*.
        
    .. memberfunction:: replace (oldie, kiddo: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        clone myself, return all occurences of *oldie* with *kiddo* and return it.
        
    .. memberfunction:: replace~string (oldie, kiddo: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        clone myself, return all occurences of *oldie* with *kiddo* and return it.
        
    .. memberfunction:: prepend (other: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        return a new string containg *other* followed by *this*.
        
    .. memberfunction:: prepend~char (other: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        return a new string containing *other* followed by *this*.
        
    .. memberfunction:: toLower -> :cover:`~lang/types String` 
        
        return a new string with all characters lowercased (if possible).
        
    .. memberfunction:: toUpper -> :cover:`~lang/types String` 
        
        return a new string with all characters uppercased (if possible).
        
    .. memberfunction:: charAt (index: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Char` 
        
        return the character at position #*index* (starting at 0)
        
    .. memberfunction:: format (...) -> :cover:`~lang/types String` 
        
        return a string formatted using *this* as template.
        
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
        
        create a new instance of the object of type defined by this class
        
    .. memberfunction:: inheritsFrom (T: :class:`~lang/types Class` ) -> :cover:`~lang/types Bool` 
        
        return true if `this` is a subclass of *T* .
        
    .. field:: instanceSize -> :cover:`~lang/types SizeT` 
    
    .. field:: size -> :cover:`~lang/types SizeT` 
    
    .. field:: name -> :cover:`~lang/types String` 
    
    .. field:: super -> :class:`~lang/types Class` 
    
    .. field:: __defaults__ -> Func 
    
    .. field:: __destroy__ -> Func 
    
    .. field:: __load__ -> Func 
    
.. class:: Object
    
    .. memberfunction:: instanceOf (T: :class:`~lang/types Class` ) -> :cover:`~lang/types Bool` 
        
        return true if *class* is a subclass of *T*.
        
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
        
        return the contents of the iterable as ArrayList.
        
    .. field:: T -> :class:`~lang/types Class` 
    
.. class:: Exception
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new~origin (origin: :class:`~lang/types Class` , msg: :cover:`~lang/types String` ) -> :class:`~lang/types Exception` 
        
    .. memberfunction:: init~origin (origin: :class:`~lang/types Class` , msg: :cover:`~lang/types String` )
        
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

