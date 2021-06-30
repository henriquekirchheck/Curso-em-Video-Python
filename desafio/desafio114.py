import urllib.request
from utils.colours import colour

url = "http://pudim.com.br"

try:
    status_code = urllib.request.urlopen(url).getcode()

    website_is_up = status_code == 200

    colour('bold', 'green')
    print('Pudim esta funcionando')
    colour()
except:
    colour('bold', 'red')
    print('Pudim não esta funcionando')
    colour()

