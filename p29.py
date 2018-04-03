from urllib.request import urlopen
from urllib.request import HTTPError
from bst4 import BeautifulSoup


try:
    html = urlopen("http://www.pythonscraping.com/pages/error.html")
except HTTPError as e:
    print(e)

else:
    
