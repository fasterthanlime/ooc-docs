structs/HashMap
===============

.. module:: structs/HashMap

.. class:: HashEntry<T>
    
    .. staticmemberfunction:: new (key: String, value: T) -> HashEntry<T>
        
    .. memberfunction:: init (key: String, value: T)
        
    .. field:: T -> Class
    
    .. field:: key -> String
    
    .. field:: value -> T
    
.. class:: HashMap<T>
    
    .. staticmemberfunction:: new -> HashMap<T>
        
    .. memberfunction:: init
        
        Returns a hash table with 100 buckets
        @return HashTable
        
        
    .. staticmemberfunction:: new~withCapacity (capacity: UInt) -> HashMap<T>
        
    .. memberfunction:: init~withCapacity (capacity: UInt)
        
        Returns a hash table of a specified bucket capacity.
        @param UInt capacity The number of buckets to use
        @return HashTable
        
        
    .. memberfunction:: murmurHash (keyTagazok: T, seed: UInt) -> UInt
        
        Port of Austin Appleby's Murmur Hash implementation
        http://murmurhash.googlepages.com/
        TODO: Use this to hash not just strings, but any type of object
        @param Object key The key to hash
        @param Int len The size of the key (in bytes)
        @param UInt seed The seed value
        
        
    .. memberfunction:: ac_X31_hash (s: String) -> UInt
        
        khash's ac_X31_hash_string
        http://attractivechaos.awardspace.com/khash.h.html
        @access private
        @param String s The string to hash
        @return UInt
        
        
    .. memberfunction:: getEntry (key: String) -> HashEntry<T>
        
        Returns the HashEntry associated with a key.
        @access private
        @param String key The key associated with the HashEntry
        @return HashEntry
        
        
    .. memberfunction:: put (key: String, value: T) -> Bool
        
        Puts a key/value pair in the hash table. If the pair already exists,
        it is overwritten.
        @param String key The key to be hashed
        @param Object value The value associated with the key
        @return Bool
        
        
    .. memberfunction:: add (key: String, value: T) -> Bool
        
        Alias of put
        
        
    .. memberfunction:: get (key: String) -> T
        
        Returns the value associated with the key. Returns null if the key
        does not exist.
        @param String key The key associated with the value
        @return Object
        
        
    .. memberfunction:: isEmpty -> Bool
        
        @return true if this map is empty, false if not
        
        
    .. memberfunction:: contains (key: String) -> Bool
        
        Returns whether or not the key exists in the hash table.
        @param String key The key to check
        @return Bool
        
        
    .. memberfunction:: remove (key: String) -> Bool
        
        Removes the entry associated with the key
        @param String key The key to remove
        @return Bool
        
        
    .. memberfunction:: resize (_capacity: UInt) -> Bool
        
        Resizes the hash table to a new capacity
        @param UInt _capacity The new table capacity
        @return Bool
        
        
    .. memberfunction:: iterator -> Iterator<T>
        
    .. memberfunction:: clear
        
    .. field:: size -> UInt
    
    .. field:: capacity -> UInt
    
    .. field:: buckets -> ArrayList<T>*
    
    .. field:: keys -> ArrayList<T>
    
.. class:: HashMapValueIterator<T>
    
    .. staticmemberfunction:: new (map: HashMap<T>) -> HashMapValueIterator<T>
        
    .. memberfunction:: init (map: HashMap<T>)
        
    .. memberfunction:: hasNext -> Bool
        
    .. memberfunction:: next -> T
        
    .. memberfunction:: hasPrev -> Bool
        
    .. memberfunction:: prev -> T
        
    .. memberfunction:: remove -> Bool
        
    .. field:: map -> HashMap<T>
    
    .. field:: index -> Int
    
