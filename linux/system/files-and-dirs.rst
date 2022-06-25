Files and Directories
=====================
* extension is not needed
* ``.myfile`` - hidden, if name starts with dot
* ``.mydirectory/`` - hidden, if name starts with dot
* ``/`` - root dir
* ``.`` - current dir
* ``..`` - upper dir


Change Directory
----------------
- ``cd``
- ``cd /absolute/path``
- ``cd relative/path``
- ``cd ~``
- ``cd -``
- ``cd ..``


List Files and Directories
--------------------------
* ``ls``
* ``ls /absolute/path``
- ``ls relative/path``
- ``ls -lah``
- ``alias l='ls -lAh --color=auto'``


Files
-----
.. csv-table:: Files
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``sum``,      "(1)",         "checksum and count the blocks in a file"
    ``vi``,       "(1)",         "Vi IMproved, a programmer's text editor"
    ``vim``,      "(1)",         "Vi IMproved, a programmer's text editor"
    ``vimdiff``,  "(1)",         "edit between two and eight versions of a file with Vim and show differences"
    ``wc -c``,    "",            "print number of characters in file"
    ``wc -l``,    "",            "print number of lines in file"
    ``wc``,       "(1)",         "print newline, word, and byte counts for each file"
    ``egrep``,    "(1)",         "print lines that match patterns"
    ``cut``,      "(1)",         "remove sections from each line of files"
    ``head``,     "(1)",         "output the first part of files"
    ``hexdump``,  "(1)",         "display file contents in hexadecimal, decimal, octal, or ascii"
    ``grep``,     "(1)",         "print lines that match patterns"
    ``join``,     "(1)",         "join lines of two files on a common field"
    ``diff``,     "(1)",         "compare files line by line"
    ``split``,    "(1)",         "split a file into pieces"
    ``view``,     "(1)",         "Vi IMproved, a programmer's text editor"
    ``strings``,  "(1)",         "print the sequences of printable characters in files"
    ``write``,    "(2)",         "write to a file descriptor"
    ``uniq``,     "(1)",         "report or omit repeated lines"
    ``sort``,     "(1)",         "sort lines of text files"
    ``pico``,     "(1)",         "Nano's ANOther editor, inspired by Pico"
    ``open``,     "(2)",         "open and possibly create a file"
    ``read``,     "(2)",         "read from a file descriptor"
    ``puts``,     "(3)",         "output of characters and strings"
    ``readline``, "(3readline)", "get a line from a user with editing"
    ``cat``,      "(1)",         "concatenate files and print on the standard output"
    ``dd``,       "(1)",         "convert and copy a file"
    ``ed``,       "(1)",         "line-oriented text editor"
    ``edit``,     "",            ""
    ``encguess``, "(1)",         "guess character encodings of files"
    ``file``,     "(1)",         "determine file type"
    ``file``,     "(3)",         "overview of system data types"
    ``more``,     "(1)",         "file perusal filter for crt viewing"
    ``nano``,     "(1)",         "Nano's ANOther editor, inspired by Pico"
    ``setcap``,   "(8)",         "set file capabilities"
    ``tail -f``,  "",            ""
    ``tail``,     "(1)",         "output the last part of files"
    ``tailf``,    "",            ""
    ``tee``,      "(1)",         "read from standard input and write to standard output and files"
    ``tee``,      "(2)",         "duplicating pipe content"
    ``tempfile``, "(1)",         "create a temporary file in a safe manner"
    ``unlink``,   "(1)",         "call the unlink function to remove the specified file"
    ``unlink``,   "(2)",         "delete a name and possibly the file it refers to"
    ``patch``,    "(1)",         "apply a diff file to an original"


Directories
-----------
.. csv-table:: Directories
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``chroot``,                     "(2)",              "change root directory"
    ``chroot``,                     "(8)",              "run command or interactive shell with special root directory"
    ``mkdir``,                      "(1)",              "make directories"
    ``mkdir``,                      "(2)",              "create a directory"
    ``rmdir``,                      "(1)",              "remove empty directories"
    ``rmdir``,                      "(2)",              "delete a directory"


Files and Directories
---------------------
.. csv-table:: Files and Directories
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``mc``,                         "",                  "Midnight Commander"
    ``cd``,                         "",                 "Change directory"
    ``chattr``,                     "(1)",              "change file attributes on a Linux file system"
    ``chgrp``,                      "(1)",              "change group ownership"
    ``chmod``,                      "(1)",              "change file mode bits"
    ``chmod``,                      "(2)",              "change permissions of a file"
    ``chown``,                      "(1)",              "change file owner and group"
    ``chown``,                      "(2)",              "change ownership of a file"
    ``cp``,                         "(1)",              "copy files and directories"
    ``cpio``,                       "(1)",              "copy files to and from archives"
    ``dir``,                        "(1)",              "list directory contents"
    ``dirname``,                    "(1)",              "strip last component from file name"
    ``dirname``,                    "(3)",              "parse pathname components"
    ``du -hs``,                     "",                 ""
    ``du``,                         "(1)",              "estimate file space usage"
    ``find``,                       "(1)",              "search for files in a directory hierarchy"
    ``l``,                          "",                 ""
    ``la``,                         "",                 ""
    ``less``,                       "(1)",              "opposite of more"
    ``ll``,                         "",                 ""
    ``ln -s``,                      "",                 ""
    ``ln``,                         "(1)",              "make links between files"
    ``locate``,                     "",                 "Locates file (from updatedb database)"
    ``ls``,                         "(1)",              "list directory contents"
    ``lsattr``,                     "(1)",              "list file attributes on a Linux second extended file system"
    ``mv``,                         "(1)",              "move (rename) files"
    ``pwd``,                        "(1)",              "print name of current/working directory"
    ``rcp``,                        "(1)",              "OpenSSH secure file copy"
    ``rm -fr``,                     "",                 ""
    ``rm``,                         "",                 "Remove"
    ``rm``,                         "(1)",              "remove files or directories"
    ``rsync``,                      "",                 "Syncronizes two directories"
    ``rsync``,                      "(1)",              "a fast, versatile, remote (and local) file-copying tool"
    ``scp``,                        "(1)",              "OpenSSH secure file copy"
    ``shred``,                      "(1)",              "overwrite a file to hide its contents, and optionally delete it"
    ``size``,                       "(1)",              "list section sizes and total size of binary files"
    ``stat``,                       "(1)",              "display file or file system status"
    ``touch``,                      "(1)",              "change file timestamps"
    ``tree``,                       "(1)",              "list contents of directories in a tree-like format."
    ``umask``,                      "(2)",              "set file mode creation mask"
    ``updatedb``,                   "",                 "Scans filesystem and create database for locate"
