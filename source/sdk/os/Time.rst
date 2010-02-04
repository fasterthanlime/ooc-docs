os/Time
=======

.. module:: os/Time

.. function:: GetLocalTime (SystemTime*)
    

.. function:: Sleep (UInt)
    

.. function:: time (TimeT*) -> TimeT
    

.. function:: localtime (TimeT*) -> TMStruct*
    

.. function:: gettimeofday (TimeVal*, TimeZone*) -> Int
    

.. function:: usleep (UInt)
    

.. cover:: SystemTime
    

.. cover:: TimeT
    

.. cover:: TimeZone
    

.. cover:: TMStruct
    

.. cover:: TimeVal
    

.. class:: Time
    
    .. memberfunction:: new -> Time
        
    
    .. memberfunction:: init
        
    
    .. memberfunction:: microtime -> LLong
        
    
    .. memberfunction:: microsec -> UInt
        
    
    .. memberfunction:: sec -> UInt
        
    
    .. memberfunction:: min -> UInt
        
    
    .. memberfunction:: hour -> UInt
        
    
    .. memberfunction:: sleepSec (duration: Float)
        
    
    .. memberfunction:: sleepMilli (duration: UInt)
        
    
    .. memberfunction:: sleepMicro (duration: UInt)
        
    

.. globalVariable:: st

.. globalVariable:: tv

.. globalVariable:: tt

.. globalVariable:: val

