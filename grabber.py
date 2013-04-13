from database_parser import *
database = ("http://www.chubbybeavers.com/wp-content/uploads/", "http://www.projektjunkies.com/pjsounds/", "http://www.houseanthems.com/wp-content/uploads/", "http://buymixtapes.com/upload/flamplayer_main/")

parsedatabase = database_parser()
print 'Welcome to my blog mp3 grabber!'
print 'Written by Claudio Wilson'
update = raw_input("Would you like to update the mp3 database? Might take awhile (Y/n) ")
if update == 'Y':
    for s in database:
        parsedatabase.add_urls(s)
    parsedatabase.save_mp3_list()
else:
    parsedatabase.load_mp3_list()
print 'There are currently ' + str(len(parsedatabase.get_mp3_list())) + ' songs in the database'
name = raw_input('What would you like to search for (song name works better than artist name) ')
#print len(parsedatabase.get_db_list())
data = parsedatabase.search(name.lower())
print 'Name' + '{:>150}'.format('URL')
for songs in data:
    print songs[1].strip() + '{:>150}'.format(songs[0])
