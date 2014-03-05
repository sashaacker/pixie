Configuration and Running
#########################

Starting Pixie
==============

Starting the bot is simple.  Once installed, there will be a new executable
available on the system.  Presuming the bot was installed with ``pip install
--user``, the following will start the bot.  If installed in a virtual
environment, the path should be adjusted.

.. code-block:: bash

   $ $HOME/.local/bin/pixie

Configuring Pixie
=================

The sole means of configuring Pixie is through a Windows-style configuration
file ('INI File'), located at ``$HOME/.config/pixie/conf.ini``.  An example
configuration file is given bellow.

.. code-block:: ini

   [connection]
   servers=
       ircs://irc.bondage.com:6697
       irc://irc.bondage.com:6667
   bindip=0
   nickname=Pixie{NP}
   username=pixie
   realname=|Nyx|'s Pixie
   usermodes=+B
   
   [ssl]
   keyfile=./key.pem
   certfile=./cert.pem
   ca_certs=./ca.pem

``connection`` Section
----------------------

``servers``
  A sequence  of URIs for the IRC servers to connect to.  Only specify the
  schema (``irc`` or ``ircs``), the host of the server, and optionally the
  port.  For non-secure connections, the port ``6667`` is the default, with
  ``6697`` being assumed as the secure default.  If the server requires a
  password, provide it in the URI using the ``username:password@`` syntax (e.g.
  ``irc://:password@host:port``).  In this case, the user portion is ignored,
  and you can omit it.  The ``:`` must not be omitted.

  Multiple URIs may be provided, one per line, indented.  The first server will
  be attempted, and if the connection fails, will attempt the next, in
  sequence.

``bindip``
  The local IP address to bind the outgoing connection to (and any incoming
  connections in any future expansion)

``nickname``
  The nickname to connect to the server with.  If the nickname is already in
  use, ``_`` will be appended to the end.

``username``
  The username (the portion after the ``!`` and before the ``@`` in a hostmask)
  to connect to the server with.

``realname``
  Also known as `GECOS` or `ircname`, it is the name that will be used in the
  real name section of a ``/whois``.

``usermode``
  The modes to set on the bot once it connects.  Note: on UnrealIRCD based IRC
  networks, it is polite, and sometimes a rule, that bots set usermode +B

``ssl`` Section
---------------

``keyfile``
  If using SSL (defined a server with an ``ircs`` scheme), this may optionally
  be set to the private key to use for the ssl connection.

``certfile``
  As ``keyfile``, but sets the public key.  ``keyfile`` must not also include a
  public key if this is set.  This may also reference the path of a file with
  both a public and private key.

``ca_certs``
  As ``keyfile``, but sets the path to a file containing certificate authority
  certificates.

Starting off with a Shebang
===========================

It may be desirable in some cases to run the bot with alternate configuration
files.  To this end, the bot will accept, as its only command line argument,
the path to a configuration file to load.  Any other data the bot needs will
still be loaded from ``$HOME/.config/pixie`` as needed.  The most convenient
method of using this feature is to put a shebang line at the beginning of the
configuration file, and executing the file.  For example:

.. code-block:: ini

   #!/home/username/.local/bin/pixie
   [connection]
   servers=
       irc://irc.bondage.com
   ...

.. code-block:: bash

   $ chmod +x config.ini
   $ ./config.ini
