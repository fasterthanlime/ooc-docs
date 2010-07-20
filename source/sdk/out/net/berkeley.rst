net/berkeley
============

.. module:: net/berkeley

.. function:: socket (family, type, protocol: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: accept (s: :cover:`~lang/types Int` , addr: :cover:`~net/berkeley SockAddr` *, addrlen: :cover:`~lang/types UInt` ) -> :cover:`~lang/types Int` 
    
.. function:: bind (sockfd: :cover:`~lang/types Int` , my_addr: :cover:`~net/berkeley SockAddr` *, addrlen: :cover:`~lang/types UInt` ) -> :cover:`~lang/types Int` 
    
.. function:: connect (sockfd: :cover:`~lang/types Int` , serv_addr: :cover:`~net/berkeley SockAddr` *, addrlen: :cover:`~lang/types UInt` ) -> :cover:`~lang/types Int` 
    
.. function:: close (descriptor: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: shutdown (s, how: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: listen (s, backlog: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: poll (ufds: :cover:`~net/berkeley PollFd` *, nfds: :cover:`~lang/types UInt` , timeout: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: recv (s: :cover:`~lang/types Int` , buf: :cover:`~lang/types Pointer` , len: :cover:`~lang/types SizeT` , flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: recvFrom (s: :cover:`~lang/types Int` , buf: :cover:`~lang/types Pointer` , len: :cover:`~lang/types SizeT` , flags: :cover:`~lang/types Int` , s_from: :cover:`~net/berkeley SockAddr` *, fromlen: :cover:`~lang/types UInt` ) -> :cover:`~lang/types Int` 
    
.. function:: send (s: :cover:`~lang/types Int` , buf: :cover:`~lang/types Pointer` , len: :cover:`~lang/types SizeT` , flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: sendTo (s: :cover:`~lang/types Int` , buf: :cover:`~lang/types Pointer` , len: :cover:`~lang/types SizeT` , flags: :cover:`~lang/types Int` , s_to: :cover:`~net/berkeley SockAddr` *, tolen: :cover:`~lang/types UInt` ) -> :cover:`~lang/types Int` 
    
.. function:: select (n: :cover:`~lang/types Int` , readfds: :cover:`~net/berkeley FdSet` *, writefds: :cover:`~net/berkeley FdSet` , exceptfds: :cover:`~net/berkeley FdSet` *, timeout: :cover:`~net/berkeley TimeVal` *) -> :cover:`~lang/types Int` 
    
.. function:: getsockopt (s, level, optname: :cover:`~lang/types Int` , optval: :cover:`~lang/types Pointer` , optlen: :cover:`~lang/types UInt` ) -> :cover:`~lang/types Int` 
    
.. function:: setsockopt (s, level, optname: :cover:`~lang/types Int` , optval: :cover:`~lang/types Pointer` , optlen: :cover:`~lang/types UInt` ) -> :cover:`~lang/types Int` 
    
.. function:: getaddrinfo (nodename, servname: :cover:`~lang/types String` , hints: :cover:`~net/berkeley AddrInfo` *, servinfo: :cover:`~net/berkeley AddrInfo` **) -> :cover:`~lang/types Int` 
    
.. function:: getnameinfo (sa: :cover:`~net/berkeley SockAddr` *, salen: :cover:`~lang/types UInt32` , host: :cover:`~lang/types String` , hostlen: :cover:`~lang/types SizeT` , serv: :cover:`~lang/types String` , servlen: :cover:`~lang/types UInt32` , flags: :cover:`~lang/types Int` ) -> :cover:`~lang/types Int` 
    
.. function:: freeaddrinfo (ai: :cover:`~net/berkeley AddrInfo` *)
    
.. function:: gai_strerror (ecode: :cover:`~lang/types Int` ) -> :cover:`~lang/types Char` *
    
.. function:: gethostname (name: :cover:`~lang/types String` , len: :cover:`~lang/types SizeT` ) -> :cover:`~lang/types Int` 
    
.. function:: gethostbyname (name: :cover:`~lang/types String` ) -> :cover:`~net/berkeley HostEntry` *
    
.. function:: gethostbyaddr (addr: :cover:`~lang/types String` , len, type: :cover:`~lang/types Int` ) -> :cover:`~net/berkeley HostEntry` *
    
.. function:: getpeername (s: :cover:`~lang/types Int` , addr: :cover:`~net/berkeley SockAddr` *, len: :cover:`~lang/types UInt` ) -> :cover:`~lang/types Int` 
    
.. function:: htonl (hostlong: :cover:`~lang/types UInt32` ) -> :cover:`~lang/types UInt32` 
    
.. function:: htons (hostshort: :cover:`~lang/types UInt16` ) -> :cover:`~lang/types UInt16` 
    
.. function:: ntohl (netlong: :cover:`~lang/types UInt32` ) -> :cover:`~lang/types UInt32` 
    
.. function:: ntohs (netshort: :cover:`~lang/types UInt16` ) -> :cover:`~lang/types UInt16` 
    
.. function:: inet_ntoa (inaddr: :cover:`~net/berkeley InAddr` ) -> :cover:`~lang/types String` 
    
.. function:: inet_aton (cp: :cover:`~lang/types String` , inp: :cover:`~net/berkeley InAddr` *) -> :cover:`~lang/types Int` 
    
.. function:: inet_addr (cp: :cover:`~lang/types String` ) -> :cover:`~lang/types ULong` 
    
.. function:: inet_ntop (af: :cover:`~lang/types Int` , src: :cover:`~lang/types Pointer` , dst: :cover:`~lang/types String` , size: :cover:`~lang/types UInt` ) -> :cover:`~lang/types String` 
    
.. function:: inet_pton (af: :cover:`~lang/types Int` , src: :cover:`~lang/types String` , dst: :cover:`~lang/types Pointer` ) -> :cover:`~lang/types Int` 
    
.. function:: ioctl (d, request: :cover:`~lang/types Int` , arg: :cover:`~lang/types Pointer` ) -> :cover:`~lang/types Int` 
    
.. cover:: SockAddr
    
    :from: ``struct sockaddr``
.. cover:: SockAddrIn
    
    :from: ``struct sockaddr_in``
.. cover:: InAddr
    
    :from: ``struct in_addr``
.. cover:: SockAddrIn6
    
    :from: ``struct sockaddr_in6``
.. cover:: In6Addr
    
    :from: ``struct in6_addr``
.. cover:: AddrInfo
    
    :from: ``struct addrinfo``
.. cover:: HostEntry
    
    :from: ``struct hostent``
.. cover:: PollFd
    
    :from: ``struct pollfd``
.. cover:: FdSet
    
    :from: ``fd_set``
    .. method:: _set (fd: :cover:`~lang/types Int` , fdset: :cover:`~net/berkeley FdSet` *)
        
    .. method:: _isSet (fd: :cover:`~lang/types Int` , fdset: :cover:`~net/berkeley FdSet` *) -> :cover:`~lang/types Bool` 
        
    .. method:: _clr (fd: :cover:`~lang/types Int` , fdset: :cover:`~net/berkeley FdSet` *)
        
    .. method:: _zero (fdset: :cover:`~net/berkeley FdSet` *)
        
    .. method:: set (fd: :cover:`~lang/types Int` )
        
    .. method:: isSet (fd: :cover:`~lang/types Int` ) -> :cover:`~lang/types Bool` 
        
    .. method:: clr (fd: :cover:`~lang/types Int` )
        
    .. method:: zero
        
.. cover:: TimeVal
    
    :from: ``struct timeval``
.. var:: INADDR_ANY -> :cover:`~lang/types ULong` 

.. var:: INADDR_NONE -> :cover:`~lang/types ULong` 

.. var:: AI_CANONNAME -> :cover:`~lang/types Int` 

.. var:: FIONREAD -> :cover:`~lang/types Int` 

