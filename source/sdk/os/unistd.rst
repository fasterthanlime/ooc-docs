os/unistd
=========

.. module:: os/unistd

.. function:: chdir (:cover:`~lang/types String`) -> :cover:`~lang/types Int`
    
.. function:: dup2 (:cover:`~lang/types Int`, :cover:`~lang/types Int`) -> :cover:`~lang/types Int`
    
.. function:: execv (:cover:`~lang/types String`, :cover:`~lang/types String`*) -> :cover:`~lang/types Int`
    
.. function:: execvp (:cover:`~lang/types String`, :cover:`~lang/types String`*) -> :cover:`~lang/types Int`
    
.. function:: execve (:cover:`~lang/types String`, :cover:`~lang/types String`*, :cover:`~lang/types String`*) -> :cover:`~lang/types Int`
    
.. function:: fileno (:cover:`~lang/stdio FILE`*) -> :cover:`~lang/types Int`
    
.. function:: fork -> :cover:`~lang/types Int`
    
.. function:: pipe (arg: :cover:`~lang/types Int`*) -> :cover:`~lang/types Int`
    
.. var:: PIPE_BUF -> :cover:`~lang/types Int`

.. var:: STDOUT_FILENO -> :cover:`~lang/types Int`

.. var:: STDERR_FILENO -> :cover:`~lang/types Int`

