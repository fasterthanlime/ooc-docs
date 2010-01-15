Compiler options
================

Blah blah, read "ooc -help" already.

.. program:: ooc

.. cmdoption:: -g, -debug

    These options include debugging information in produced executables.
    (E.g. symbol names when debugging, to give you a sweet stack trace)

.. cmdoption:: -noclean

    By default, the ooc compiler erases the produced .c/.h files after successful
    compilation. -noclean instructs it to leave the .c/.h files. Useful if you
    want to read/study them or redistribute them.

    .. note::

	-g implies -noclean, cause having .c/.h files around is useful when
	debugging

.. cmdoption:: -driver=combine, -driver=sequence

    The Combine driver outputs .c/.h files at every compilation, and launches
    the C compiler on all of them at once.

    The Sequence driver only outputs .c/.h files if they have changed since
    last written to disk, only compiles them to .o if the date of the
    .c/.h and .o are different. In the best case, only the executable
    is rebuilt.

    In fact, .c/.h files aren't really compiled in sequence. Several gcc
    processes are launched in parallel, to speed up the compilation process.

.. cmdoption:: +...

    The ooc will pass options prepended with ``+`` to the compiler. So, if you
    want to pass the ``-pedantic`` flag to the compiler, invoke ooc like
    ``ooc +-pedantic test.ooc``.

    Even options with values work this way. If you want to pass ``-L ~/libs`` to the compiler, do
    ``ooc +-L +~/libs test.ooc``.

.. envvar:: OOC_SDK

    To use a custom SDK, use this environment variable to make the location known to ooc.

.. envvar:: OOC_LIBS

    This environment variable points to the :ref:`libraries <libs>` directory. If not given, the
    default is :file:`/usr/lib/ooc` on linux.

.. envvar:: OOC_DIST

    This environment variable may contain the path of your ooc distribution. Don't worry, in the
    most cases, ooc will find itself.
