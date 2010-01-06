.. _libs:

Using and creating ooc libraries, or the magic of .use files
============================================================

Installing ooc libs
-------------------

Let's say you want to install ooc-cairo:

There are several ways
  - Either: copy the ooc-cairo directory to /usr/lib/ooc/ and you're all set.
  - Or: ln -s /path/to/ooc-cairo  /usr/lib/ooc/ and you're good.
  - If you don't want to put your libs in /usr/lib/ooc/, adjust the OOC_LIBS
    environment variable (in the /usr/bin/ooc launcher script, for example,
    or in /etc/environment, or in your Makefile, or..)
  

Example - gtk hello world
-------------------------

Let's take a simple GTK hello world::

    use gtk

    import gtk/[Gtk, Window, Button]

    main: func {
        Window new("Hi, world =)") setUSize(400, 200).
               connect("delete_event", exit).
               showAll()
        Gtk main()
    }

    exit: extern func

'use gtk' will instruct the ooc compiler to search for a file
named 'gtk.use'

Search paths
------------

The standard search path is /usr/lib/ooc/, but can be adjusted
by setting the OOC_LIBS environment variable

So in our case, let's say we have installed ooc-gtk and ooc-gdk
in /usr/lib/ooc/, the compiler will find gtk.use in /usr/lib/ooc/ooc-gtk,
which is fine.

Content of a .use file
----------------------

gtk.use contains something like::

    Name: GTK+ 2.0
    Version: head
    Origin: git://github.com/nddrylliog/ooc-gtk.git
    Description: GNU User interface Toolkit
    Pkgs: gtk+-2.0
    Includes: gtk/gtk.h, gdk/gdk.h
    Requires: gdk
    SourcePath: .

The format is very similar to .pc files from the pkg-config tool, but
it serves a higher purpose =)

Valid directives in .use files
------------------------------

The Name and Description directives are merely for humans

Version contains the name of this specific version. This can be ``0.1``, or
``2.12``, or ``3.7-alpha``, or ``head``. The ``head`` version makes clear
that this usefile describes the bleeding-edge version of the package, usually
located in a git repository.

The Origin directive lets us know how to get the sourcecode. This can be
an ordinary url (``http://myserver.com/packages/ooc-gtk.tar.gz``, ``ftp://.../ooc-gtk.tar.gz``)
or a ``git://`` url, usually for the ``head`` version.

The Pkgs directive defines which pkg-config package to use. This allows
to portably define include paths, library paths (-I and -L for gcc)
for libs with .pc files.

For libraries without .pc files, you can also use Libs, IncludePaths and
LibPaths directives.

The Includes directive add 'include' statements automatically in file 
using the lib.

Requires allow to specify dependencies between libraries. Since ooc-gtk
requires ooc-gdk, gtk.use has Requires: gdk, and then gdk.use will be
found and used too!

The SourcePath directive allows to add directories to the sourcepath.
For most libraries this will be '.' or 'source/', relative to the location
of the .use file. But you can also use absolute paths.

Lines starting with '#' are comments. They are ignored.

Known issues / possible improvements
------------------------------------

There should be some versioning support, both in the 'Requires' .use directive
and the 'use' statement in ooc code, e.g. in gtk-helloworld.ooc::

    use gtk >= 2.10

and in gtk.use::

    Requires: gdk >= 2.10

