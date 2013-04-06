#Class to parse index of data urls, to find links to the path before the .mp3 file.
import urllib
import cPickle as pickle
from lxml import html
class database_parser(object):
    def __init__(self):
        self.db_list = []
        self.mp3_list = []

    def add_urls(self, db_url):
        page = html.fromstring(urllib.urlopen(db_url).read())
        for link in page.xpath("//a"): #To get text, it's link.text
            if '/' in link.get("href") and '/' in link.text:
                self.add_urls(db_url + link.get("href")) #LOOK! Recursion IN THE WILD!
            elif '.mp3' in link.text:
                mp3_name = link.text.replace('-', ' ').lower()
                self.mp3_list.append((db_url + link.get("href"),mp3_name))
    def get_mp3_list(self):
        return self.mp3_list
    def get_db_list(self):
        return self.db_list
    def save_mp3_list(self):
        pickle.dump(self.mp3_list, open('mp3list.pkl','wb'))
    def load_mp3_list(self):
        pkl_file = open('mp3list.pkl','rb')
        self.mp3_list = pickle.load(pkl_file)
        pkl_file.close()
    #Probably a shitty searching algorithm (goes through the WHOLE list), I'll have to update this
    def search(self, filename):
        data = []
        for s in self.mp3_list:
            if filename in s[1]:
                data.append(s)
        return data
