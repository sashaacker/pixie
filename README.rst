Nyxie's Pixie
=============

Pixie is an IRC bot that provides channel services as well as some nick
tracking features.  Or rather I should say it will provide them.  This is the
skeleton of a project.  Some of the features, which will be developed openly,
are for a need that is not for public consumption.

Planned features include tracking of nicks-to-hosts to help build constant
identities amongst people.  Additionally it will provide general channel
services; maintaining a autokick/multi-channel-ban list, a seen facility, and
perhaps even a user-mailable database.

The architecture of the bot is intended to be easily, though not trivially
extendible.  Pragmatism will rule over a truly pure API, though there is an
intent on having a clean API.

Pixie will be written in Python, as that is the only language I care to use for
personal projects, and while it may work on Windows, that will be a happy
accident.  The entire point is to run this damn thing from a Linux VPS.
Extensions to Python implemented in C can and will be used in this project, and
the intent is for this bad girl to daemonize itself as fork()ing is easier for
me to do than to sit down and try and configure some third party process
manager.

This project will also be an experiment in
documentation-driving-test-driven-development - I will write the docs first,
then the test then the code.  That is the plan at least.

I have not committed on any particular networking framework.  I do not want to
be calling select myself, so I will not be writing this to the bare sockets.
