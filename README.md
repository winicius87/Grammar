This grammar check server uses link-parser (https://manpages.ubuntu.com/manpages/trusty/man1/link-parser.1.html) found in Ubuntu.


First, install link-grammar on Ubuntu.
apt install link-grammar

Then, change the form action from /g/ to /.

To load it, type:
./gram.py &

Or type:
nohup ./gram.py &

Navigate to http://localhost:8001/ to begin using it.

This HTTP server is written in Python.

It is light weight. Files are served from ./_public/

![Screenshot](https://isellemails.com/MediaLight/XEhA2/LEBAteNO88.jpg/raw)
