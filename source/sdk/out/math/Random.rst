math/Random
===========

.. module:: math/Random

.. class:: Random
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~math/Random Random` 
        
    .. method:: init
        
    .. staticmethod:: random -> :cover:`~lang/types Int` 
        
    .. staticmethod:: randInt (start, end: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. staticmethod:: randInt~exclude (start, end: :cover:`~lang/types Int` , ex: :class:`~structs/List List<T>` ) -> :cover:`~lang/types Int` 
        
    .. staticmethod:: randRange (start, end: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. staticmethod:: randRange~exclude (start, end: :cover:`~lang/types Int` , ex: :class:`~structs/List List<T>` ) -> :cover:`~lang/types Int` 
        
    .. staticmethod:: choice (l: :class:`~structs/List List<T>` ) -> T 
        
    .. staticmethod:: exclude (start, end: :cover:`~lang/types Int` , ex: :class:`~structs/List List<T>` , f: Func ) -> :cover:`~lang/types Int` 
        
    .. staticmethod:: fastRandom -> :cover:`~lang/types Int` 
        
    .. staticmethod:: fastRandInt (start, end: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. staticmethod:: fastRandInt~exclude (start, end: :cover:`~lang/types Int` , ex: :class:`~structs/List List<T>` ) -> :cover:`~lang/types Int` 
        
    .. staticmethod:: fastRandRange (start, end: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
        
    .. staticmethod:: fastRandRange~exclude (start, end: :cover:`~lang/types Int` , ex: :class:`~structs/List List<T>` ) -> :cover:`~lang/types Int` 
        
    .. field:: state -> :cover:`~lang/types Long` 
    
.. var:: __STATE -> :cover:`~lang/types LLong` 

