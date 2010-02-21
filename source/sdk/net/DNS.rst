net/DNS
=======

.. module:: net/DNS

.. class:: DNS
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new -> :class:`~net/DNS DNS` 
        
    .. memberfunction:: init
        
    .. staticmemberfunction:: resolve (hostname: :cover:`~lang/types String` ) -> :class:`~net/DNS HostInfo` 
        
        Perform DNS lookup using the hostname.
        Returns information about the host that was found.
        
        
    .. staticmemberfunction:: resolve~filter (hostname: :cover:`~lang/types String` , socketType, socketFamily: :cover:`~lang/types Int` ) -> :class:`~net/DNS HostInfo` 
        
    .. staticmemberfunction:: resolveOne (host: :cover:`~lang/types String` ) -> :class:`~net/Address IPAddress` 
        
        Perform DNS lookup using the hostname.
        Returns the first IPAddress found for the host.
        
        
    .. staticmemberfunction:: resolveOne~filter (host: :cover:`~lang/types String` , socketType, socketFamily: :cover:`~lang/types Int` ) -> :class:`~net/Address IPAddress` 
        
    .. staticmemberfunction:: reverse (ip: :class:`~net/Address IPAddress` ) -> :cover:`~lang/types String` 
        
        Perform a reverse DNS lookup by using the host's address.
        Returns the hostname of the specified address.
        
        
    .. staticmemberfunction:: reverse~withSockAddr (sockaddr: :class:`~net/Address SocketAddress` ) -> :cover:`~lang/types String` 
        
    .. staticmemberfunction:: hostname -> :cover:`~lang/types String` 
        
        Returns the hostname of this system.
        
        
    .. staticmemberfunction:: localhost -> :class:`~net/DNS HostInfo` 
        
        Retreive host information about this system.
        
        
.. class:: HostInfo
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new (addrinfo: :cover:`~net/berkeley AddrInfo` *) -> :class:`~net/DNS HostInfo` 
        
    .. memberfunction:: init (addrinfo: :cover:`~net/berkeley AddrInfo` *)
        
    .. memberfunction:: addresses -> :class:`~structs/LinkedList LinkedList<T>` 
        
    .. field:: name -> :cover:`~lang/types String` 
    
    .. field:: addresses -> :class:`~structs/LinkedList LinkedList<T>` 
    
