structs/HashMap
===============

.. module:: structs/HashMap

.. class:: HashEntry<T>
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new (key: :cover:`~lang/types String` , value: T ) -> :class:`~structs/HashMap HashEntry<T>` 
        
    .. memberfunction:: init (key: :cover:`~lang/types String` , value: T )
        
    .. field:: T -> :class:`~lang/types Class` 
    
    .. field:: key -> :cover:`~lang/types String` 
    
    .. field:: value -> T 
    
.. class:: HashMap<T>
    
    :extends: :class:`~lang/types Iterable<T>` 
    .. staticmemberfunction:: new -> :class:`~structs/HashMap HashMap<T>` 
        
    .. memberfunction:: init
        
        Returns a hash table with 100 buckets
        @return HashTable
        
        
    .. staticmemberfunction:: new~withCapacity (capacity: :cover:`~lang/types UInt` ) -> :class:`~structs/HashMap HashMap<T>` 
        
    .. memberfunction:: init~withCapacity (capacity: :cover:`~lang/types UInt` )
        
        Returns a hash table of a specified bucket capacity.
        @param UInt capacity The number of buckets to use
        @return HashTable
        
        
    .. memberfunction:: murmurHash (keyTagazok: T , seed: :cover:`~lang/types UInt` ) -> :cover:`~lang/types UInt` 
        
        Port of Austin Appleby's Murmur Hash implementation
        http://murmurhash.googlepages.com/
        TODO: Use this to hash not just strings, but any type of object
        @param Object key The key to hash
        @param Int len The size of the key (in bytes)
        @param UInt seed The seed value
        
        
    .. memberfunction:: ac_X31_hash (s: :cover:`~lang/types String` ) -> :cover:`~lang/types UInt` 
        
        khash's ac_X31_hash_string
        http://attractivechaos.awardspace.com/khash.h.html
        @access private
        @param String s The string to hash
        @return UInt
        
        
    .. memberfunction:: getEntry (key: :cover:`~lang/types String` ) -> :class:`~structs/HashMap HashEntry<T>` 
        
        Returns the HashEntry associated with a key.
        @access private
        @param String key The key associated with the HashEntry
        @return HashEntry
        
        
    .. memberfunction:: put (key: :cover:`~lang/types String` , value: T ) -> :cover:`~lang/types Bool` 
        
        Puts a key/value pair in the hash table. If the pair already exists,
        it is overwritten.
        @param String key The key to be hashed
        @param Object value The value associated with the key
        @return Bool
        
        
    .. memberfunction:: add (key: :cover:`~lang/types String` , value: T ) -> :cover:`~lang/types Bool` 
        
        Alias of put
        
        
    .. memberfunction:: get (key: :cover:`~lang/types String` ) -> T 
        
        Returns the value associated with the key. Returns null if the key
        does not exist.
        @param String key The key associated with the value
        @return Object
        
        
    .. memberfunction:: isEmpty -> :cover:`~lang/types Bool` 
        
        @return true if this map is empty, false if not
        
        
    .. memberfunction:: contains (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        Returns whether or not the key exists in the hash table.
        @param String key The key to check
        @return Bool
        
        
    .. memberfunction:: remove (key: :cover:`~lang/types String` ) -> :cover:`~lang/types Bool` 
        
        Removes the entry associated with the key
        @param String key The key to remove
        @return Bool
        
        
    .. memberfunction:: resize (_capacity: :cover:`~lang/types UInt` ) -> :cover:`~lang/types Bool` 
        
        Resizes the hash table to a new capacity
        @param UInt _capacity The new table capacity
        @return Bool
        
        
    .. memberfunction:: iterator -> :class:`~lang/types Iterator<T>` 
        
    .. memberfunction:: clear
        
    .. field:: size -> :cover:`~lang/types UInt` 
    
    .. field:: capacity -> :cover:`~lang/types UInt` 
    
    .. field:: buckets -> :class:`~structs/ArrayList ArrayList<T>` *
    
    .. field:: keys -> :class:`~structs/ArrayList ArrayList<T>` 
    
.. class:: HashMapValueIterator<T>
    
    :extends: :class:`~lang/types Iterator<T>` 
    .. staticmemberfunction:: new (map: :class:`~structs/HashMap HashMap<T>` ) -> :class:`~structs/HashMap HashMapValueIterator<T>` 
        
    .. memberfunction:: init (map: :class:`~structs/HashMap HashMap<T>` )
        
    .. memberfunction:: hasNext -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: next -> T 
        
    .. memberfunction:: hasPrev -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: prev -> T 
        
    .. memberfunction:: remove -> :cover:`~lang/types Bool` 
        
    .. field:: map -> :class:`~structs/HashMap HashMap<T>` 
    
    .. field:: index -> :cover:`~lang/types Int` 
    
