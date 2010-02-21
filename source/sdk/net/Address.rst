net/Address
===========

.. module:: net/Address

.. class:: IPAddress
    
    :extends: :class:`~lang/types Object` 
    .. memberfunction:: isBroadcast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a broadcast address.
        
        Only IPv4 addresses can be broadcast addresses. All bits are one.
        IPv6 addresses always return false.
        
        
    .. memberfunction:: isWildcard -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a wildcard (all zeros) address.
        
        
    .. memberfunction:: isGlobalMulticast -> :cover:`~lang/types Bool` 
        
        Return true if the address is a global multicast address.
        
        IPv4 most be in the 224.0.1.0 to 238.255.255.255 range.
        IPv6 most be in the FFxF:x:x:x:x:x:x:x range.
        
        
    .. memberfunction:: isIP4Compatible -> :cover:`~lang/types Bool` 
        
        Returns true if the address is IPv4 compatible.
        
        IPv4 addresses always return true.
        IPv6 address must be in the ::x:x range (first 96 bits are zero).
        
        
    .. memberfunction:: isIP4Mapped -> :cover:`~lang/types Bool` 
        
        Returns true if the address is an IPv4 mapped IPv6 address.
        
        IPv4 addresses always return true.
        IPv6 addresses must be in the ::FFFF:x:x range.
        
        
    .. memberfunction:: isLinkLocal -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a link local unicast address.
        
        IPv4 addresses are in the 169.254.0.0/16 range (RFC 3927).
        IPv6 addresses have 1111 1110 10 as the first 10 bits, followed by 54 zeros. 
        
        
    .. memberfunction:: isLinkLocalMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a link local multicast address.
        
        IPv4 addresses are in the 224.0.0.0/24 range. Note that this overlaps with the range for
        well-known multicast addresses.
        
        
    .. memberfunction:: isLoopback -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a loopback address.
        
        IPv4 address must be 127.0.0.1
        IPv6 address must be ::1
        
        
    .. memberfunction:: isMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a multicast address.
        
        IPv4 addresses must be in the 224.0.0.0 to 239.255.255.255 range
        (the first four bits have the value 1110).
        IPv6 addresses are in the FFxx:x:x:x:x:x:x:x range.
        
        
    .. memberfunction:: isNodeLocalMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a node-local multicast address.
        
        IPv4 does not support node-local multicast and will always return false.
        IPv6 addresses must be in the FFx1:x:x:x:x:x:x:x range.
        
        
    .. memberfunction:: isOrgLocalMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is an organization-local multicast address.
        
        IPv4 addresses must be in the 239.192.0.0/16 range.
        IPv6 addresses must be in the FFx8:x:x:x:x:x:x:x range.
        
        
    .. memberfunction:: isSiteLocal -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a site-local unicast address.
        
        IPv4 addresses are in on of the 10.0.0.0/24, 192.168.0.0/16 or 172.16.0.0 to 172.31.255.255 ranges.
        IPv6 addresses have 1111 1110 11 as the first 10 bits, followed by 38 zeros.
        
        
    .. memberfunction:: isSiteLocalMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a site-local multicast address.
        
        IPv4 addresses are in the 239.255.0.0/16 range.
        IPv6 addresses are in the FFx5:x:x:x:x:x:x:x range.
        
        
    .. memberfunction:: isUnicast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is an unicast address.
        
        An address is unicast if it is neither a wildcard, broadcast, or multicast.
        
        
    .. memberfunction:: isWellKnownMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a well-known multicast address.
        
        IPv4 addresses are in the 224.0.0.0/8 range.
        IPv6 addresses are in the FF0x:x:x:x:x:x:x:x range.
        
        
    .. memberfunction:: mask (mask: :class:`~net/Address IPAddress` )
        
        Masks the IP address using the given netmask, which is usually a IPv4 subnet mask.
        Only supported for IPv4 addresses.
        The new address is (address & mask).
        
        
    .. memberfunction:: mask~withSet (mask, set: :class:`~net/Address IPAddress` )
        
        Masks the IP address using the given netmask, which is usually a IPv4 subnet mask.
        Only supported for IPv4 addresses.
        
        The new address is (address & mask) | (set & mask).
        
        
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
        Returns a string representation of the address in presentation format.
        
        
    .. field:: family -> :cover:`~lang/types Int` 
    
.. class:: IP4Address
    
    :extends: :class:`~net/Address IPAddress` 
    .. staticmemberfunction:: new (ipAddress: :cover:`~lang/types String` ) -> :class:`~net/Address IP4Address` 
        
    .. memberfunction:: init (ipAddress: :cover:`~lang/types String` )
        
    .. staticmemberfunction:: new~withAddr (addr: :cover:`~net/berkeley InAddr` ) -> :class:`~net/Address IP4Address` 
        
    .. memberfunction:: init~withAddr (addr: :cover:`~net/berkeley InAddr` )
        
    .. memberfunction:: isBroadcast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isWildcard -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isGlobalMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isIP4Compatible -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isIP4Mapped -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isLinkLocal -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isLinkLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isLoopback -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isNodeLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isOrgLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isSiteLocal -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isSiteLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isWellKnownMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: mask (mask: :class:`~net/Address IPAddress` )
        
    .. memberfunction:: mask~withSet (mask, set: :class:`~net/Address IPAddress` )
        
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. field:: ai -> :cover:`~net/berkeley InAddr` 
    
.. class:: IP6Address
    
    :extends: :class:`~net/Address IPAddress` 
    .. staticmemberfunction:: new (ipAddress: :cover:`~lang/types String` ) -> :class:`~net/Address IP6Address` 
        
    .. memberfunction:: init (ipAddress: :cover:`~lang/types String` )
        
    .. staticmemberfunction:: new~withAddr (addr: :cover:`~net/berkeley In6Addr` ) -> :class:`~net/Address IP6Address` 
        
    .. memberfunction:: init~withAddr (addr: :cover:`~net/berkeley In6Addr` )
        
    .. memberfunction:: toWords -> :cover:`~lang/types UInt16` *
        
    .. memberfunction:: isBroadcast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isWildcard -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isGlobalMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isIP4Compatible -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isIP4Mapped -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isLinkLocal -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isLinkLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isLoopback -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isNodeLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isOrgLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isSiteLocal -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isSiteLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: isWellKnownMulticast -> :cover:`~lang/types Bool` 
        
    .. memberfunction:: mask (mask: :class:`~net/Address IPAddress` )
        
    .. memberfunction:: mask~withSet (mask, set: :class:`~net/Address IPAddress` )
        
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
    .. field:: ai -> :cover:`~net/berkeley In6Addr` 
    
.. class:: SocketAddress
    
    :extends: :class:`~lang/types Object` 
    .. staticmemberfunction:: new (host: :class:`~net/Address IPAddress` , port: :cover:`~lang/types Int` ) -> :class:`~net/Address SocketAddress` 
        
    .. memberfunction:: family -> :cover:`~lang/types Int` 
        
    .. memberfunction:: host -> :class:`~net/Address IPAddress` 
        
    .. memberfunction:: port -> :cover:`~lang/types Int` 
        
    .. memberfunction:: addr -> :cover:`~net/berkeley SockAddr` *
        
    .. memberfunction:: length -> :cover:`~lang/types UInt32` 
        
    .. memberfunction:: toString -> :cover:`~lang/types String` 
        
.. class:: SocketAddressIP4
    
    :extends: :class:`~net/Address SocketAddress` 
    .. staticmemberfunction:: new (addr: :cover:`~net/berkeley InAddr` , port: :cover:`~lang/types Int` ) -> :class:`~net/Address SocketAddressIP4` 
        
    .. memberfunction:: init (addr: :cover:`~net/berkeley InAddr` , port: :cover:`~lang/types Int` )
        
    .. memberfunction:: family -> :cover:`~lang/types Int` 
        
    .. memberfunction:: host -> :class:`~net/Address IPAddress` 
        
    .. memberfunction:: port -> :cover:`~lang/types Int` 
        
    .. memberfunction:: addr -> :cover:`~net/berkeley SockAddr` *
        
    .. memberfunction:: length -> :cover:`~lang/types UInt32` 
        
    .. field:: sa -> :cover:`~net/berkeley SockAddrIn` 
    
.. class:: SocketAddressIP6
    
    :extends: :class:`~net/Address SocketAddress` 
    .. staticmemberfunction:: new (addr: :cover:`~net/berkeley In6Addr` , port: :cover:`~lang/types Int` ) -> :class:`~net/Address SocketAddressIP6` 
        
    .. memberfunction:: init (addr: :cover:`~net/berkeley In6Addr` , port: :cover:`~lang/types Int` )
        
    .. memberfunction:: family -> :cover:`~lang/types Int` 
        
    .. memberfunction:: host -> :class:`~net/Address IPAddress` 
        
    .. memberfunction:: port -> :cover:`~lang/types Int` 
        
    .. memberfunction:: addr -> :cover:`~net/berkeley SockAddr` *
        
    .. memberfunction:: length -> :cover:`~lang/types UInt32` 
        
    .. field:: sa -> :cover:`~net/berkeley SockAddrIn6` 
    
