lang/types
==========

.. module:: lang/types

.. function:: strtol (:cover:`~lang/types Char` *, :cover:`~lang/types Pointer` , :cover:`~lang/types Int` ) -> :cover:`~lang/types Long` 
    
.. function:: strtoll (:cover:`~lang/types Char` *, :cover:`~lang/types Pointer` , :cover:`~lang/types Int` ) -> :cover:`~lang/types LLong` 
    
.. function:: strtoul (:cover:`~lang/types Char` *, :cover:`~lang/types Pointer` , :cover:`~lang/types Int` ) -> :cover:`~lang/types ULong` 
    
.. function:: strtof (:cover:`~lang/types Char` *, :cover:`~lang/types Pointer` ) -> :cover:`~lang/types Float` 
    
.. function:: strtod (:cover:`~lang/types Char` *, :cover:`~lang/types Pointer` ) -> :cover:`~lang/types Double` 
    
.. function:: strtold (:cover:`~lang/types Char` *, :cover:`~lang/types Pointer` ) -> :cover:`~lang/types LDouble` 
    
.. function:: strlen (:cover:`~lang/types Char` *) -> :cover:`~lang/types Int` 
    
.. cover:: Void
    
    :from: ``void``
.. cover:: Pointer
    
    :from: ``void*``
    .. method:: toString -> :cover:`~lang/types String` 
        
.. cover:: Char
    
    :from: ``char``
    .. method:: isAlphaNumeric -> :cover:`~lang/types Bool` 
        
        check for an alphanumeric character
        
    .. method:: isAlpha -> :cover:`~lang/types Bool` 
        
        check for an alphabetic character
        
    .. method:: isLower -> :cover:`~lang/types Bool` 
        
        check for a lowercase alphabetic character
        
    .. method:: isUpper -> :cover:`~lang/types Bool` 
        
        check for an uppercase alphabetic character
        
    .. method:: isDigit -> :cover:`~lang/types Bool` 
        
        check for a decimal digit (0 through 9)
        
    .. method:: isHexDigit -> :cover:`~lang/types Bool` 
        
        check for a hexadecimal digit (0 1 2 3 4 5 6 7 8 9 a b c d e f A B C D E F)
        
    .. method:: isControl -> :cover:`~lang/types Bool` 
        
        check for a control character
        
    .. method:: isGraph -> :cover:`~lang/types Bool` 
        
        check for any printable character except space
        
    .. method:: isPrintable -> :cover:`~lang/types Bool` 
        
        check for any printable character including space
        
    .. method:: isPunctuation -> :cover:`~lang/types Bool` 
        
        check for any printable character which is not a space or an alphanumeric character
        
    .. method:: isWhitespace -> :cover:`~lang/types Bool` 
        
        check for white-space characters: space, form-feed ('\\f'), newline ('\\n'),
        carriage return ('\\r'), horizontal tab ('\\t'), and vertical tab ('\\v') 
        
    .. method:: isBlank -> :cover:`~lang/types Bool` 
        
        check for a blank character; that is, a space or a tab
        
    .. method:: toInt -> :cover:`~lang/types Int` 
        
        convert to an integer. This only works for digits, otherwise -1 is returned
        
    .. method:: toLower -> :cover:`~lang/types Char` 
        
        return the lowered character
        
    .. method:: toUpper -> :cover:`~lang/types Char` 
        
        return the capitalized character
        
    .. method:: toString -> :cover:`~lang/types String` 
        
        return a one-character string containing this character.
        
    .. method:: print
        
        write this character to stdout without a following newline.
        
    .. method:: println
        
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
    .. method:: new~withLength (length: :cover:`~lang/types Int` ) -> :cover:`~lang/types String` 
        
        Create a new string exactly *length* characters long (without the nullbyte).
        The contents of the string are undefined. 
        
    .. method:: new~withChar (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        Create a new string of the length 1 containing only the character *c
        
    .. method:: compare (other: :cover:`~lang/types String` , start, length: :cover:`~lang/types Int` ) -> :cover:`~lang/types Bool` 
        
        compare *length* characters of *this* with *other*, starting at *start*.
        Return true if the two strings are equal, return false if they are not. 
        
    .. method:: compare~implicitLength (other: :cover:`~lang/types String` , start: :cover:`~lang/types Int` ) -> :cover:`~lang/types Bool` 
        
        compare *this* with *other*, starting at *start*. The count of compared
        characters is determined by *other*'s length. 
        
    .. method:: compare~whole (other: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        compare *this* with *other*, starting at 0. Compare ``other length()`` characters.
        
    .. method:: length -> :cover:`~lang/types Int` 
        
        return the string's length, excluding the null byte.
        
    .. method:: equals (other: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        return true if *other* and *this* are equal. This also returns false if either
        of these two is ``null``. 
        
    .. method:: toInt -> :cover:`~lang/types Int` 
        
        convert the string's contents to Int.
        
    .. method:: toInt~withBase (base: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. method:: toLong -> :cover:`~lang/types Long` 
        
        convert the string's contents to Long.
        
    .. method:: toLong~withBase (base: :cover:`~lang/types Long` ) -> :cover:`~lang/types Long` 
        
    .. method:: toLLong -> :cover:`~lang/types LLong` 
        
        convert the string's contents to Long Long.
        
    .. method:: toLLong~withBase (base: :cover:`~lang/types LLong` ) -> :cover:`~lang/types LLong` 
        
    .. method:: toULong -> :cover:`~lang/types ULong` 
        
        convert the string's contents to Unsigned Long.
        
    .. method:: toULong~withBase (base: :cover:`~lang/types ULong` ) -> :cover:`~lang/types ULong` 
        
    .. method:: toFloat -> :cover:`~lang/types Float` 
        
        convert the string's contents to Float.
        
    .. method:: toDouble -> :cover:`~lang/types Double` 
        
        convert the string's contents to Double.
        
    .. method:: toLDouble -> :cover:`~lang/types LDouble` 
        
        convert the string's contents to Long Double.
        
    .. method:: isEmpty -> :cover:`~lang/types Bool` 
        
        return true if the string is empty or ``null``.
        
    .. method:: startsWith (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        return true if the first characters of *this* are equal to *s*.
        
    .. method:: startsWith~withChar (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Bool` 
        
        return true if the first character of *this* is equal to *c*.
        
    .. method:: endsWith (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        return true if the last characters of *this* are equal to *s*.
        
    .. method:: indexOf~charZero (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Int` 
        
        return the index of *c*, starting at 0. If *this* does not contain
        c*, return -1. 
        
    .. method:: indexOf~char (c: :cover:`~lang/types Char` , start: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
        return the index of *c*, but only check characters ``start..length``.
        However, the return value is the index of the *c* relative to the
        string's beginning. If *this* does not contain *c*, return -1. 
        
    .. method:: indexOf~stringZero (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
        return the index of *s*, starting at 0. If *this* does not contain *s*,
        return -1. 
        
    .. method:: indexOf~string (s: :cover:`~lang/types String` , start: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
        return the index of *s*, but only check characters ``start..length``.
        However, the return value is relative to the *this*' first character.
        If *this* does not contain *c*, return -1. 
        
    .. method:: contains~char (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Bool` 
        
        return *true* if *this* contains the character *c
        
    .. method:: contains~string (s: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        return *true* if *this* contains the string *s
        
    .. method:: trim~space -> :cover:`~lang/types String` 
        
        return a copy of *this* with space characters (ASCII 32) stripped at both ends.
        
    .. method:: trim (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        return a copy of *this* with *c* characters stripped at both ends.
        
    .. method:: trim~string (s: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        return a copy of *this* with all characters contained by *s* stripped
        at both ends. 
        
    .. method:: trimLeft~space -> :cover:`~lang/types String` 
        
        return a copy of *this* with space characters (ASCII 32) stripped from the left side.
        
    .. method:: trimLeft (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        return a copy of *this* with *c* characters stripped from the left side.
        
    .. method:: trimLeft~string (s: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        return a copy of *this* with all characters contained by *s* stripped
        from the left side. 
        
    .. method:: trimRight~space -> :cover:`~lang/types String` 
        
        return a copy of *this* with space characters (ASCII 32) stripped from the right side.
        
    .. method:: trimRight (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        return a copy of *this* with *c* characters stripped from the right side.
        
    .. method:: trimRight~string (s: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        return a copy of *this* with all characters contained by *s* stripped
        from the right side. 
        
    .. method:: first -> :cover:`~lang/types Char` 
        
        return the first character of *this*. If *this* is empty, 0 is returned.
        
    .. method:: lastIndex -> :cover:`~lang/types Int` 
        
        return the index of the last character of *this*. If *this* is empty,
        -1 is returned. 
        
    .. method:: last -> :cover:`~lang/types Char` 
        
        return the last character of *this*.
        
    .. method:: lastIndexOf (c: :cover:`~lang/types Char` ) -> :cover:`~lang/types Int` 
        
        return the index of the last occurence of *c* in *this*.
        If *this* does not contain *c*, return -1. 
        
    .. method:: substring~tillEnd (start: :cover:`~lang/types Int` ) -> :cover:`~lang/types String` 
        
        return a substring of *this* only containing the characters
        in the range ``start..length``.  
        
    .. method:: substring (start, end: :cover:`~lang/types Int` ) -> :cover:`~lang/types String` 
        
        return a substring of *this* only containing the characters in the
        range ``start..end``. 
        
    .. method:: reverse -> :cover:`~lang/types String` 
        
        return a reversed copy of *this*.
        
    .. method:: print
        
        print *this* to stdout without a following newline. Flush stdout.
        
    .. method:: println
        
        print *this* followed by a newline.
        
    .. method:: times (count: :cover:`~lang/types Int` ) -> :cover:`~lang/types String` 
        
        return a string that contains *this*, repeated *count* times.
        
    .. method:: clone -> :cover:`~lang/types String` 
        
        return a copy of *this*.
        
    .. method:: append (other: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        return a string that contains *this* followed by *other*.
        
    .. method:: append~char (other: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        return a string containing *this* followed by *other*.
        
    .. method:: count~char (what: :cover:`~lang/types Char` ) -> :cover:`~lang/types Int` 
        
        return the number of *what*'s occurences in *this*.
        
    .. method:: count~string (what: :cover:`~lang/types String` ) -> :cover:`~lang/types Int` 
        
        return the number of *what*'s non-overlapping occurences in *this*.
        
    .. method:: replace (oldie, kiddo: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        clone myself, return all occurences of *oldie* with *kiddo* and return it.
        
    .. method:: replace~string (oldie, kiddo: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        clone myself, return all occurences of *oldie* with *kiddo* and return it.
        
    .. method:: prepend (other: :cover:`~lang/types String` ) -> :cover:`~lang/types String` 
        
        return a new string containg *other* followed by *this*.
        
    .. method:: prepend~char (other: :cover:`~lang/types Char` ) -> :cover:`~lang/types String` 
        
        return a new string containing *other* followed by *this*.
        
    .. method:: toLower -> :cover:`~lang/types String` 
        
        return a new string with all characters lowercased (if possible).
        
    .. method:: toUpper -> :cover:`~lang/types String` 
        
        return a new string with all characters uppercased (if possible).
        
    .. method:: charAt (index: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Char` 
        
        return the character at position #*index* (starting at 0)
        
    .. method:: format (...) -> :cover:`~lang/types String` 
        
        return a string formatted using *this* as template.
        
    .. method:: scanf (format: :cover:`~lang/types String` , ...) -> :cover:`~lang/types Int` 
        
    .. method:: iterator -> :class:`~lang/types StringIterator<T>` 
        
.. cover:: LLong
    
    :from: ``signed long long``
    .. method:: toString -> :cover:`~lang/types String` 
        
    .. method:: toHexString -> :cover:`~lang/types String` 
        
    .. method:: isOdd -> :cover:`~lang/types Bool` 
        
    .. method:: isEven -> :cover:`~lang/types Bool` 
        
    .. method:: in (range: :cover:`~lang/types Range` ) -> :cover:`~lang/types Bool` 
        
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
    .. method:: toString -> :cover:`~lang/types String` 
        
    .. method:: in (range: :cover:`~lang/types Range` ) -> :cover:`~lang/types Bool` 
        
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
    .. method:: toString -> :cover:`~lang/types String` 
        
.. cover:: LDouble
    
    :from: ``long double``
    .. method:: toString -> :cover:`~lang/types String` 
        
    .. method:: abs -> :cover:`~lang/types LDouble` 
        
.. cover:: Float
    
    :extends: :cover:`~lang/types LDouble` 
    :from: ``float``
.. cover:: Double
    
    :extends: :cover:`~lang/types LDouble` 
    :from: ``double``
.. cover:: Range
    
    .. method:: new (min, max: :cover:`~lang/types Int` ) -> :cover:`~lang/types Range` 
        
.. class:: Class
    
    :extends: :class:`~lang/types Object` 
    .. method:: alloc -> :class:`~lang/types Object` 
        
        create a new instance of the object of type defined by this class
        
    .. method:: inheritsFrom (T: :class:`~lang/types Class` ) -> :cover:`~lang/types Bool` 
        
        return true if `this` is a subclass of *T* .
        
    .. field:: instanceSize -> :cover:`~lang/types SizeT` 
    
    .. field:: size -> :cover:`~lang/types SizeT` 
    
    .. field:: name -> :cover:`~lang/types String` 
    
    .. field:: super -> :class:`~lang/types Class` 
    
    .. field:: __defaults__ -> Func 
    
    .. field:: __destroy__ -> Func 
    
    .. field:: __load__ -> Func 
    
.. class:: Object
    
    .. method:: instanceOf (T: :class:`~lang/types Class` ) -> :cover:`~lang/types Bool` 
        
        return true if *class* is a subclass of *T*.
        
    .. field:: class -> :class:`~lang/types Class` 
    
.. class:: Iterator<T>
    
    :extends: :class:`~lang/types Object` 
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: next -> T 
        
    .. method:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. method:: prev -> T 
        
    .. method:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: T -> :class:`~lang/types Class` 
    
.. class:: Iterable<T>
    
    :extends: :class:`~lang/types Object` 
    .. method:: iterator -> :class:`~lang/types Iterator<T>` 
        
    .. method:: toArrayList -> :class:`~structs/ArrayList ArrayList<T>` 
        
        return the contents of the iterable as ArrayList.
        
    .. field:: T -> :class:`~lang/types Class` 
    
.. class:: Exception
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new~origin (origin: :class:`~lang/types Class` , msg: :cover:`~lang/types String` ) -> :class:`~lang/types Exception` 
        
    .. method:: init~origin (origin: :class:`~lang/types Class` , msg: :cover:`~lang/types String` )
        
    .. staticmethod:: new~noOrigin (msg: :cover:`~lang/types String` ) -> :class:`~lang/types Exception` 
        
    .. method:: init~noOrigin (msg: :cover:`~lang/types String` )
        
    .. method:: crash
        
    .. method:: getMessage -> :cover:`~lang/types String` 
        
    .. method:: print
        
    .. method:: throw
        
    .. field:: origin -> :class:`~lang/types Class` 
    
    .. field:: msg -> :cover:`~lang/types String` 
    
.. class:: StringIterator<T>
    
    :extends: :class:`~lang/types Iterator<T>` 
    .. staticmethod:: new~withStr (str: :cover:`~lang/types String` ) -> :class:`~lang/types StringIterator<T>` 
        
    .. method:: init~withStr (str: :cover:`~lang/types String` )
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: next -> T 
        
    .. method:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. method:: prev -> T 
        
    .. method:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: i -> :cover:`~lang/types Int` 
    
    .. field:: str -> :cover:`~lang/types String` 
    
.. class:: None
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~lang/types None` 
        
    .. method:: init
        
.. class:: Cell<T>
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new (val: T ) -> :class:`~lang/types Cell<T>` 
        
    .. method:: init (val: T )
        
    .. field:: T -> :class:`~lang/types Class` 
    
    .. field:: val -> T 
    
.. var:: INT_MIN -> :cover:`~lang/types Int` 

.. var:: INT_MAX -> :cover:`~lang/types Int` 

.. var:: UINT_MAX -> :cover:`~lang/types UInt` 

.. var:: LONG_MIN -> :cover:`~lang/types Long` 

.. var:: LONG_MAX -> :cover:`~lang/types Long` 

.. var:: ULONG_MAX -> :cover:`~lang/types ULong` 

.. var:: LLONG_MIN -> :cover:`~lang/types LLong` 

.. var:: LLONG_MAX -> :cover:`~lang/types LLong` 

.. var:: ULLONG_MAX -> :cover:`~lang/types ULLong` 

.. var:: DBL_MIN -> :cover:`~lang/types Double` 

.. var:: DBL_MAX -> :cover:`~lang/types Double` 

.. var:: FLT_MIN -> :cover:`~lang/types Float` 

.. var:: FLT_MAX -> :cover:`~lang/types Float` 

.. var:: LDBL_MIN -> :cover:`~lang/types LDouble` 

.. var:: LDBL_MAX -> :cover:`~lang/types LDouble` 

