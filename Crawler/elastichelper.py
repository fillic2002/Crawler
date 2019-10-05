import subprocess
from lxml import html
import requests
from html.parser import HTMLParser

def url_ok(url):
    r = requests.head(url)
    if(r.status_code == 200):
        print('Elastic is up and runnin')
        return True
    else:
        print('Elastic is down')
        return False

def make_Elastic_Up():
    if (url_ok('http://localhost:9200') != True):
        subprocess.call([r'C:\Users\u0156319\Desktop\E.bat'])
        print('Elastic is up')

 
make_Elastic_Up()

