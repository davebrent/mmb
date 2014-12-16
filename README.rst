MMB is a command line tool for saving the state of an Elektron Monomachine::

    pip install mmb

Usage
-----

Connect the monomachine to a midi device and run::

    mmb backup --port="Name of midi device"

This will save all the kits, patterns, songs and global settings. To view a
list of all backups run::

    mmb info

And to restore the monomachine to a previous state, set the momomachine to
recieve Sysex messages and run::

    mmb send <BACKUP_ID>

To configure mmb to always use a specific port run::

    mmb configure

And save the port name in the opened settings file.
