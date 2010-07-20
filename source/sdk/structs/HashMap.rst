structs/HashMap
===============

.. module:: structs/HashMap

.. function:: stringKeyEquals (k1, k2: K ) -> :cover:`~lang/types Bool` 
    
.. function:: genericKeyEquals (k1, k2: K ) -> :cover:`~lang/types Bool` 
    
.. function:: murmurHash (keyTagazok: K ) -> :cover:`~lang/types UInt` 
    
.. function:: ac_X31_hash (key: K ) -> :cover:`~lang/types UInt` 
    
.. class:: HashEntry<K,V>
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new~keyVal (key: K , value: V ) -> :class:`~structs/HashMap HashEntry<K,V>` 
        
    .. method:: init~keyVal (key: K , value: V )
        
    .. field:: V -> :class:`~lang/types Class` 
    
    .. field:: K -> :class:`~lang/types Class` 
    
    .. field:: key -> K 
    
    .. field:: value -> V 
    
.. class:: HashMap<K,V>
    
    :extends: :class:`~lang/types Iterable<T>` 
    .. staticmethod:: new -> :class:`~structs/HashMap HashMap<K,V>` 
        
    .. method:: init
        
        Returns a hash table with 100 buckets
        @return HashTable
        
        
    .. staticmethod:: new~withCapacity (capacity: :cover:`~lang/types UInt` ) -> :class:`~structs/HashMap HashMap<K,V>` 
        
    .. method:: init~withCapacity (capacity: :cover:`~lang/types UInt` )
        
        Returns a hash table of a specified bucket capacity.
        @param UInt capacity The number of buckets to use
        @return HashTable
        
        
    .. method:: getEntry (key: K ) -> :class:`~structs/HashMap HashEntry<K,V>` 
        
        Returns the HashEntry associated with a key.
        @access private
        @param key The key associated with the HashEntry
        @return HashEntry
        
        
    .. method:: put (key: K , value: V ) -> :cover:`~lang/types Bool` 
        
        Puts a key/value pair in the hash table. If the pair already exists,
        it is overwritten.
        @param key The key to be hashed
        @param value The value associated with the key
        @return Bool
        
        
    .. method:: add (key: K , value: V ) -> :cover:`~lang/types Bool` 
        
        Alias of put
        
        
    .. method:: get (key: K ) -> V 
        
        Returns the value associated with the key. Returns null if the key
        does not exist.
        @param key The key associated with the value
        @return Object
        
        
    .. method:: isEmpty -> :cover:`~lang/types Bool` 
        
        @return true if this map is empty, false if not
        
        
    .. method:: contains (key: K ) -> :cover:`~lang/types Bool` 
        
        Returns whether or not the key exists in the hash table.
        @param key The key to check
        @return Bool
        
        
    .. method:: remove (key: K ) -> :cover:`~lang/types Bool` 
        
        Removes the entry associated with the key
        @param key The key to remove
        @return Bool
        
        
    .. method:: resize (_capacity: :cover:`~lang/types UInt` ) -> :cover:`~lang/types Bool` 
        
        Resizes the hash table to a new capacity
        @param UInt _capacity The new table capacity
        @return Bool
        
        
    .. method:: iterator -> :class:`~lang/types Iterator<T>` 
        
    .. method:: clear
        
    .. method:: size -> :cover:`~lang/types UInt` 
        
    .. method:: getKeys -> :class:`~structs/ArrayList ArrayList<T>` 
        
    .. field:: V -> :class:`~lang/types Class` 
    
    .. field:: K -> :class:`~lang/types Class` 
    
    .. field:: size -> :cover:`~lang/types UInt` 
    
    .. field:: capacity -> :cover:`~lang/types UInt` 
    
    .. field:: keyEquals -> Func 
    
    .. field:: hashKey -> Func 
    
    .. field:: buckets -> :class:`~structs/ArrayList ArrayList<T>` *
    
    .. field:: keys -> :class:`~structs/ArrayList ArrayList<T>` 
    
.. class:: HashMapValueIterator<K,T>
    
    :extends: :class:`~lang/types Iterator<T>` 
    .. staticmethod:: new~withMap (map: :class:`~structs/HashMap HashMap<K,V>` ) -> :class:`~structs/HashMap HashMapValueIterator<K,T>` 
        
    .. method:: init~withMap (map: :class:`~structs/HashMap HashMap<K,V>` )
        
    .. method:: hasNext -> :cover:`~lang/types Bool` 
        
    .. method:: next -> T 
        
    .. method:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. method:: prev -> T 
        
    .. method:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: K -> :class:`~lang/types Class` 
    
    .. field:: map -> :class:`~structs/HashMap HashMap<K,V>` 
    
    .. field:: index -> :cover:`~lang/types Int` 
    
