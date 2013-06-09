## Grabber

Currently, just grabs .mp3 files from a given Apache Server Directory Listing

I guess eventually the aim would be to be given a blog's URL, and then find the download links
to the mp3's that the blogger blogs about.

#How to Use:
You'll need python installed, so go install it.
You'll also need lxml, so run `sudo apt-get install python-lxml`
Then, run `python grabber.py`

Or, open it up in IDLE and compile (on Windows)

###To Do
Find more Apache Index Directories

Add Soundcloud API support (to search soundcloud)

Find a way to access sites whose directories' indexes are not available (might be kinda hard) (like the music ninja)

Use a better data structure to store the mp3s (linear search bads).
