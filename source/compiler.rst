Compiler options
================

Blah blah, read "ooc -help" already.

driver=combine
--------------

The Combine driver outputs .c/.h files at every compilation, and launches
the C compiler on all of them at once.

driver=sequence
---------------

The Sequence driver only outputs .c/.h files if they have changed since
last written to disk, only compiles them to .o if the date of the
.c/.h and .o are different. In the best case, only the executable
is rebuilt.

In fact, .c/.h files aren't really compiled in sequence. Several gcc
processes are launched in parallel, to speed up the compilation process.

