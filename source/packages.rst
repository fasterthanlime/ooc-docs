Packages
========

ooc's standard packaging system is the combination of `nirvana`_, `reincarnate`_ and meatshops.

The Nirvana takes care of the usefiles. The usefiles contain the meta-information about a package.
The Meatshops host the actual archives, most likely tarballs.
Reincarnate is responsible of the client side. It installs, removes and updates packages.

Installation
------------

reincarnate itself is written in ooc, but it has some dependencies that you have to install
by hand.

.. note:: The following guide is for linux only. Windows will follow.

Linux
~~~~~

You need the following non-ooc libraries and tools:

 * `git <http://git-scm.com>`_
 * `the j/ooc compiler <http://ooc-lang.org>`_
 * `yajl <http://lloyd.github.com/yajl>`_
 * `libcurl <http://curl.haxx.se>`_
 * `uriparser <http://uriparser.sourceforge.net>`_

Look out for a directory that will contain the reincarnate sources. Once you have found a nice
place, run the following::

    git clone git://github.com/fredreichbier/reincarnate.git

You can now either create a temporary library directory just for building reincarnate or create a
custom library directory somewhere or just use the default library direcory `/usr/lib/ooc` (see :ref:`libs`).
Type::

    export OOC_LIBS=/path/to/your/libraries/directory

Then, fetch all ooc dependencies::

    git clone git://github.com/nddrylliog/ooc-curl.git
    git clone git://github.com/fredreichbier/oocini.git
    git clone git://github.com/fredreichbier/gifnooc.git
    git clone git://github.com/fredreichbier/deadlogger.git
    git clone git://github.com/fredreichbier/ooc-uriparser.git
    git clone git://github.com/fredreichbier/ooc-yajl.git

Create softlinks to all package directories in the lib directory::

    ln -s `pwd`/ooc-curl $OOC_LIBS
    ln -s `pwd`/oocini $OOC_LIBS
    ln -s `pwd`/gifnooc $OOC_LIBS
    ln -s `pwd`/deadlogger $OOC_LIBS
    ln -s `pwd`/ooc-iniparser $OOC_LIBS
    ln -s `pwd`/ooc-yajl $OOC_LIBS

Now, you can install reincarnate::

    cd reincarnate
    make

In the end, you should have a single executable file `reincarnate` which you can copy
to `/usr/bin` if you wish to.

Usage
-----

To install a package, you can just type::

    reincarnate install name

This will install the latest version. If a `head` version is available, this one is installed -
the `head` version marks the bleeding-edge version, most likely fetched from a git/hg/svn repository.

If you want to install one exact version (e.g. the version `0.1`), type::

    reincarnate install name=0.1

Remove a package::

    reincarnate remove name

Update a package::

    reincarnate update name

With reincarnate, it is possible to have multiple different versions of the same package installed simultaneously.
To make sure that a version is kept installed, even when you update the package, you have to mark it as kept::

    reincarnate keep name=0.3b

To unmark it::

    reincarnate unkeep name=0.3b

Configuration
-------------

Reincarnate reads its configuration from `/etc/reincarnate/config` and `~/.reincarnate/config`. Both files
are INI files, with the following options (the listed values are default values)::

    [Nirvana]
    APITemplate: http://nirvana.ooc-lang.org/api%s # The API URL template of your nirvana instance
    UsefileTemplate: http://nirvana.ooc-lang.org%s # The usefile URL template of your nirvana instance
    User: # Your nirvana user. Needed for package submission.
    Token: # Your API token. Needed for package submission.
    [Meatshop]
    # ... TODO
    [Paths]
    oocLibs: # If given, this will overwrite the OOC_LIBS environment variable.
    Temp: /var/tmp/ooc # The path to a temporary directory.
    Yard: $oocLibs/.yard # Path to the reincarnate yard. Reincarnate stores internal data in the yard.
    
.. _nirvana: http://nirvana.ooc-lang.org
.. _reincarnate: http://github.com/fredreichbier/reincarnate
