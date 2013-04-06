from database_parser import *
database = ("http://www.chubbybeavers.com/wp-content/uploads/", "http://www.projektjunkies.com/pjsounds/")

parsedatabase = database_parser()
print 'Welcome to my blog mp3 grabber!'
print 'Written by Claudio Wilson'
s = raw_input("Would you like to update the mp3 database? Might take awhile (Y/n) ")
if s == 'Y':
    for s in database:
        parsedatabase.add_urls(s)
    parsedatabase.save_mp3_list()
else:
    parsedatabase.load_mp3_list()

song = raw_input('What would you like to search for (song name works better than artist name) ')
#print len(parsedatabase.get_db_list())
print parsedatabase.search(song.lower())
