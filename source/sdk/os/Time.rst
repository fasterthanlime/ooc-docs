os/Time
=======

.. module:: os/Time

.. function:: GetLocalTime (:cover:`~os/Time SystemTime` *)
    
.. function:: Sleep (:cover:`~lang/types UInt` )
    
.. function:: time (:cover:`~os/Time TimeT` *) -> :cover:`~os/Time TimeT` 
    
.. function:: localtime (:cover:`~os/Time TimeT` *) -> :cover:`~os/Time TMStruct` *
    
.. function:: gettimeofday (:cover:`~os/Time TimeVal` *, :cover:`~os/Time TimeZone` *) -> :cover:`~lang/types Int` 
    
.. function:: usleep (:cover:`~lang/types UInt` )
    
.. cover:: SystemTime
    
    :from: ``SYSTEMTIME``
.. cover:: TimeT
    
    :from: ``time_t``
.. cover:: TimeZone
    
    :from: ``struct timezone``
.. cover:: TMStruct
    
    :from: ``struct tm``
.. cover:: TimeVal
    
    :from: ``struct timeval``
.. class:: Time
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~os/Time Time` 
        
    .. method:: init
        
    .. staticmethod:: microtime -> :cover:`~lang/types LLong` 
        
    .. staticmethod:: microsec -> :cover:`~lang/types UInt` 
        
    .. staticmethod:: sec -> :cover:`~lang/types UInt` 
        
    .. staticmethod:: min -> :cover:`~lang/types UInt` 
        
    .. staticmethod:: hour -> :cover:`~lang/types UInt` 
        
    .. staticmethod:: sleepSec (duration: :cover:`~lang/types Float` )
        
    .. staticmethod:: sleepMilli (duration: :cover:`~lang/types UInt` )
        
    .. staticmethod:: sleepMicro (duration: :cover:`~lang/types UInt` )
        
.. var:: st -> :cover:`~os/Time SystemTime` 

.. var:: tv -> :cover:`~os/Time TimeVal` 

.. var:: tt -> :cover:`~os/Time TimeT` 

.. var:: val -> :cover:`~os/Time TMStruct` *

