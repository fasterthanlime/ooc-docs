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
    
.. cover:: TimeT
    
.. cover:: TimeZone
    
.. cover:: TMStruct
    
.. cover:: TimeVal
    
.. class:: Time
    
    .. staticmemberfunction:: new -> :class:`~os/Time Time` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: microtime -> :cover:`~lang/types LLong` 
        
    .. staticmemberfunction:: microsec -> :cover:`~lang/types UInt` 
        
    .. staticmemberfunction:: sec -> :cover:`~lang/types UInt` 
        
    .. staticmemberfunction:: min -> :cover:`~lang/types UInt` 
        
    .. staticmemberfunction:: hour -> :cover:`~lang/types UInt` 
        
    .. staticmemberfunction:: sleepSec (duration: :cover:`~lang/types Float` )
        
    .. staticmemberfunction:: sleepMilli (duration: :cover:`~lang/types UInt` )
        
    .. staticmemberfunction:: sleepMicro (duration: :cover:`~lang/types UInt` )
        
.. var:: st -> :cover:`~os/Time SystemTime` 

.. var:: tv -> :cover:`~os/Time TimeVal` 

.. var:: tt -> :cover:`~os/Time TimeT` 

.. var:: val -> :cover:`~os/Time TMStruct` *

