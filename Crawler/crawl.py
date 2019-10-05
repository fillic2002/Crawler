from lxml import html
import requests
from html.parser import HTMLParser

def getresponse(siteurl):
    s = requests.get(siteurl)
    tree = html.fromstring(s.content)
    st ='//*[@class="rl3f9 _3mXOU"]li/text()'
    
    buyers = tree.xpath('//li[@class="EIR5N"]/a/div/span[1]/text()')
    for i in buyers:
        print(i.strip("₹ "))
    
      
    
getresponse("https://www.olx.in/bengaluru_g4058803/q-drawer")