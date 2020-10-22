import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não esta acessivel no momento')
else:
    print('consegui acessar o site pudim com sucesso')
    #print(site.read()) #é uma função que pega o codigo HTML inteiro do site
