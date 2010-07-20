net/Address
===========

.. module:: net/Address

.. class:: IPAddress
    
    :extends: :class:`~lang/types Object` 
    .. method:: isBroadcast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a broadcast address.
        
        Only IPv4 addresses can be broadcast addresses. All bits are one.
        IPv6 addresses always return false.
        
        
    .. method:: isWildcard -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a wildcard (all zeros) address.
        
        
    .. method:: isGlobalMulticast -> :cover:`~lang/types Bool` 
        
        Return true if the address is a global multicast address.
        
        IPv4 most be in the 224.0.1.0 to 238.255.255.255 range.
        IPv6 most be in the FFxF:x:x:x:x:x:x:x range.
        
        
    .. method:: isIP4Compatible -> :cover:`~lang/types Bool` 
        
        Returns true if the address is IPv4 compatible.
        
        IPv4 addresses always return true.
        IPv6 address must be in the ::x:x range (first 96 bits are zero).
        
        
    .. method:: isIP4Mapped -> :cover:`~lang/types Bool` 
        
        Returns true if the address is an IPv4 mapped IPv6 address.
        
        IPv4 addresses always return true.
        IPv6 addresses must be in the ::FFFF:x:x range.
        
        
    .. method:: isLinkLocal -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a link local unicast address.
        
        IPv4 addresses are in the 169.254.0.0/16 range (RFC 3927).
        IPv6 addresses have 1111 1110 10 as the first 10 bits, followed by 54 zeros. 
        
        
    .. method:: isLinkLocalMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a link local multicast address.
        
        IPv4 addresses are in the 224.0.0.0/24 range. Note that this overlaps with the range for
        well-known multicast addresses.
        
        
    .. method:: isLoopback -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a loopback address.
        
        IPv4 address must be 127.0.0.1
        IPv6 address must be ::1
        
        
    .. method:: isMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a multicast address.
        
        IPv4 addresses must be in the 224.0.0.0 to 239.255.255.255 range
        (the first four bits have the value 1110).
        IPv6 addresses are in the FFxx:x:x:x:x:x:x:x range.
        
        
    .. method:: isNodeLocalMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a node-local multicast address.
        
        IPv4 does not support node-local multicast and will always return false.
        IPv6 addresses must be in the FFx1:x:x:x:x:x:x:x range.
        
        
    .. method:: isOrgLocalMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is an organization-local multicast address.
        
        IPv4 addresses must be in the 239.192.0.0/16 range.
        IPv6 addresses must be in the FFx8:x:x:x:x:x:x:x range.
        
        
    .. method:: isSiteLocal -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a site-local unicast address.
        
        IPv4 addresses are in on of the 10.0.0.0/24, 192.168.0.0/16 or 172.16.0.0 to 172.31.255.255 ranges.
        IPv6 addresses have 1111 1110 11 as the first 10 bits, followed by 38 zeros.
        
        
    .. method:: isSiteLocalMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a site-local multicast address.
        
        IPv4 addresses are in the 239.255.0.0/16 range.
        IPv6 addresses are in the FFx5:x:x:x:x:x:x:x range.
        
        
    .. method:: isUnicast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is an unicast address.
        
        An address is unicast if it is neither a wildcard, broadcast, or multicast.
        
        
    .. method:: isWellKnownMulticast -> :cover:`~lang/types Bool` 
        
        Returns true if the address is a well-known multicast address.
        
        IPv4 addresses are in the 224.0.0.0/8 range.
        IPv6 addresses are in the FF0x:x:x:x:x:x:x:x range.
        
        
    .. method:: mask (mask: :class:`~net/Address IPAddress` )
        
        Masks the IP address using the given netmask, which is usually a IPv4 subnet mask.
        Only supported for IPv4 addresses.
        The new address is (address & mask).
        
        
    .. method:: mask~withSet (mask, set: :class:`~net/Address IPAddress` )
        
        Masks the IP address using the given netmask, which is usually a IPv4 subnet mask.
        Only supported for IPv4 addresses.
        
        The new address is (address & mask) | (set & mask).
        
        
    .. method:: toString -> :cover:`~lang/types String` 
        
        Returns a string representation of the address in presentation format.
        
        
    .. field:: family -> :cover:`~lang/types Int` 
    
.. class:: IP4Address
    
    :extends: :class:`~net/Address IPAddress` 
    .. staticmethod:: new (ipAddress: :cover:`~lang/types String` ) -> :class:`~net/Address IP4Address` 
        
    .. method:: init (ipAddress: :cover:`~lang/types String` )
        
    .. staticmethod:: new~wildcard -> :class:`~net/Address IP4Address` 
        
    .. method:: init~wildcard
        
    .. staticmethod:: new~withAddr (addr: :cover:`~net/berkeley InAddr` ) -> :class:`~net/Address IP4Address` 
        
    .. method:: init~withAddr (addr: :cover:`~net/berkeley InAddr` )
        
    .. method:: isBroadcast -> :cover:`~lang/types Bool` 
        
    .. method:: isWildcard -> :cover:`~lang/types Bool` 
        
    .. method:: isGlobalMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isIP4Compatible -> :cover:`~lang/types Bool` 
        
    .. method:: isIP4Mapped -> :cover:`~lang/types Bool` 
        
    .. method:: isLinkLocal -> :cover:`~lang/types Bool` 
        
    .. method:: isLinkLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isLoopback -> :cover:`~lang/types Bool` 
        
    .. method:: isMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isNodeLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isOrgLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isSiteLocal -> :cover:`~lang/types Bool` 
        
    .. method:: isSiteLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isWellKnownMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: mask (mask: :class:`~net/Address IPAddress` )
        
    .. method:: mask~withSet (mask, set: :class:`~net/Address IPAddress` )
        
    .. method:: toString -> :cover:`~lang/types String` 
        
    .. field:: ai -> :cover:`~net/berkeley InAddr` 
    
.. class:: IP6Address
    
    :extends: :class:`~net/Address IPAddress` 
    .. staticmethod:: new (ipAddress: :cover:`~lang/types String` ) -> :class:`~net/Address IP6Address` 
        
    .. method:: init (ipAddress: :cover:`~lang/types String` )
        
    .. staticmethod:: new~withAddr (addr: :cover:`~net/berkeley In6Addr` ) -> :class:`~net/Address IP6Address` 
        
    .. method:: init~withAddr (addr: :cover:`~net/berkeley In6Addr` )
        
    .. method:: toWords -> :cover:`~lang/types UInt16` *
        
    .. method:: isBroadcast -> :cover:`~lang/types Bool` 
        
    .. method:: isWildcard -> :cover:`~lang/types Bool` 
        
    .. method:: isGlobalMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isIP4Compatible -> :cover:`~lang/types Bool` 
        
    .. method:: isIP4Mapped -> :cover:`~lang/types Bool` 
        
    .. method:: isLinkLocal -> :cover:`~lang/types Bool` 
        
    .. method:: isLinkLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isLoopback -> :cover:`~lang/types Bool` 
        
    .. method:: isMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isNodeLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isOrgLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isSiteLocal -> :cover:`~lang/types Bool` 
        
    .. method:: isSiteLocalMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: isWellKnownMulticast -> :cover:`~lang/types Bool` 
        
    .. method:: mask (mask: :class:`~net/Address IPAddress` )
        
    .. method:: mask~withSet (mask, set: :class:`~net/Address IPAddress` )
        
    .. method:: toString -> :cover:`~lang/types String` 
        
    .. field:: ai -> :cover:`~net/berkeley In6Addr` 
    
.. class:: SocketAddress
    
    :extends: :class:`~lang/types Object` 
    .. staticmethod:: new (host: :class:`~net/Address IPAddress` , port: :cover:`~lang/types Int` ) -> :class:`~net/Address SocketAddress` 
        
    .. staticmethod:: newFromSock (addr: :cover:`~net/berkeley SockAddr` *, len: :cover:`~lang/types UInt` ) -> :class:`~net/Address SocketAddress` 
        
    .. method:: family -> :cover:`~lang/types Int` 
        
    .. method:: host -> :class:`~net/Address IPAddress` 
        
    .. method:: port -> :cover:`~lang/types Int` 
        
    .. method:: addr -> :cover:`~net/berkeley SockAddr` *
        
    .. method:: length -> :cover:`~lang/types UInt32` 
        
    .. method:: toString -> :cover:`~lang/types String` 
        
.. class:: SocketAddressIP4
    
    :extends: :class:`~net/Address SocketAddress` 
    .. staticmethod:: new (addr: :cover:`~net/berkeley InAddr` , port: :cover:`~lang/types Int` ) -> :class:`~net/Address SocketAddressIP4` 
        
    .. method:: init (addr: :cover:`~net/berkeley InAddr` , port: :cover:`~lang/types Int` )
        
    .. staticmethod:: new~sock (sockAddr: :cover:`~net/berkeley SockAddrIn` *) -> :class:`~net/Address SocketAddressIP4` 
        
    .. method:: init~sock (sockAddr: :cover:`~net/berkeley SockAddrIn` *)
        
    .. method:: family -> :cover:`~lang/types Int` 
        
    .. method:: host -> :class:`~net/Address IPAddress` 
        
    .. method:: port -> :cover:`~lang/types Int` 
        
    .. method:: addr -> :cover:`~net/berkeley SockAddr` *
        
    .. method:: length -> :cover:`~lang/types UInt32` 
        
    .. field:: sa -> :cover:`~net/berkeley SockAddrIn` 
    
.. class:: SocketAddressIP6
    
    :extends: :class:`~net/Address SocketAddress` 
    .. staticmethod:: new (addr: :cover:`~net/berkeley In6Addr` , port: :cover:`~lang/types Int` ) -> :class:`~net/Address SocketAddressIP6` 
        
    .. method:: init (addr: :cover:`~net/berkeley In6Addr` , port: :cover:`~lang/types Int` )
        
    .. staticmethod:: new~sock6 (sockAddr: :cover:`~net/berkeley SockAddrIn6` *) -> :class:`~net/Address SocketAddressIP6` 
        
    .. method:: init~sock6 (sockAddr: :cover:`~net/berkeley SockAddrIn6` *)
        
    .. method:: family -> :cover:`~lang/types Int` 
        
    .. method:: host -> :class:`~net/Address IPAddress` 
        
    .. method:: port -> :cover:`~lang/types Int` 
        
    .. method:: addr -> :cover:`~net/berkeley SockAddr` *
        
    .. method:: length -> :cover:`~lang/types UInt32` 
        
    .. field:: sa -> :cover:`~net/berkeley SockAddrIn6` 
    
