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
    
    .. staticmemberfunction:: new -> Time
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: microtime -> LLong
        
    .. staticmemberfunction:: microsec -> UInt
        
    .. staticmemberfunction:: sec -> UInt
        
    .. staticmemberfunction:: min -> UInt
        
    .. staticmemberfunction:: hour -> UInt
        
    .. staticmemberfunction:: sleepSec (duration: Float)
        
    .. staticmemberfunction:: sleepMilli (duration: UInt)
        
    .. staticmemberfunction:: sleepMicro (duration: UInt)
        
.. data:: st

.. data:: tv

.. data:: tt

.. data:: val

