net/DNS
=======

.. module:: net/DNS

.. class:: DNS
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new -> :class:`~net/DNS DNS` 
        
    .. method:: init
        
    .. staticmethod:: resolve (hostname: :cover:`~lang/types String` ) -> :class:`~net/DNS HostInfo` 
        
        Perform DNS lookup using the hostname.
        Returns information about the host that was found.
        
        
    .. staticmethod:: resolve~filter (hostname: :cover:`~lang/types String` , socketType, socketFamily: :cover:`~lang/types Int` ) -> :class:`~net/DNS HostInfo` 
        
    .. staticmethod:: resolveOne (host: :cover:`~lang/types String` ) -> :class:`~net/Address IPAddress` 
        
        Perform DNS lookup using the hostname.
        Returns the first IPAddress found for the host.
        
        
    .. staticmethod:: resolveOne~filter (host: :cover:`~lang/types String` , socketType, socketFamily: :cover:`~lang/types Int` ) -> :class:`~net/Address IPAddress` 
        
    .. staticmethod:: reverse (ip: :class:`~net/Address IPAddress` ) -> :cover:`~lang/types String` 
        
        Perform a reverse DNS lookup by using the host's address.
        Returns the hostname of the specified address.
        
        
    .. staticmethod:: reverse~withSockAddr (sockaddr: :class:`~net/Address SocketAddress` ) -> :cover:`~lang/types String` 
        
    .. staticmethod:: hostname -> :cover:`~lang/types String` 
        
        Returns the hostname of this system.
        
        
    .. staticmethod:: localhost -> :class:`~net/DNS HostInfo` 
        
        Retreive host information about this system.
        
        
.. class:: HostInfo
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new (addrinfo: :cover:`~net/berkeley AddrInfo` *) -> :class:`~net/DNS HostInfo` 
        
    .. method:: init (addrinfo: :cover:`~net/berkeley AddrInfo` *)
        
    .. method:: addresses -> :class:`~structs/LinkedList LinkedList<T>` 
        
        Returns a list of IPAddress associated with this host.
        
        
    .. field:: name -> :cover:`~lang/types String` 
    
    .. field:: addresses -> :class:`~structs/LinkedList LinkedList<T>` 
    
