import urllib
import re
from tqdm import tqdm
from threading import Thread 
import os

od_roku = '2018'
liczba_watkow = 32
liczba_stron_do_przejrzenia = 20

lista_stron =['https://sin.put.poznan.pl/search/publications/all?yearFrom={}&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page={}'.format(od_roku, i) for i in range(1, liczba_stron_do_przejrzenia+1)]

lista_id = []

try:
    os.makedirs("./publikacje/{}".format(od_roku))
except:
    pass

cnt=0
pbar = tqdm(total = len(lista_stron))

for url in lista_stron:
    cnt+=1
    req = urllib.request.urlopen(url).read().decode("UTF-8")
    pub_id = re.findall('href="/publications/details/(i\d{1,6})">', req)
    for i in pub_id:
        lista_id.append(i)
    pbar.update(1)
    
print("\r\nliczba publikacji:{}\r\n".format(len(lista_id)))

lista_autorow = {}



            
            

def pobierz_html(art_id):
    req = urllib.request.urlopen('https://sin.put.poznan.pl/publications/details/' + art_id).read()

    with open("./publikacje/{}/{}.html".format(od_roku, art_id),'wb') as f:
        f.write(req)



watki = []
    
liczba_aktywnych_watkow = 0
ostatni_uruchomiony_watek = 0
liczba_art = len(lista_id)
id_num = 0

pbar = tqdm(total=liczba_art)

while id_num < liczba_art or liczba_aktywnych_watkow > 0:
    if liczba_aktywnych_watkow < liczba_watkow and id_num < liczba_art:
        liczba_aktywnych_watkow += 1
        watki.append(Thread(target = pobierz_html, args =(lista_id[id_num],)))
        id_num += 1
        watki[-1].start()
        ostatni_uruchomiony_watek+=1
    else:
        for x in range(len(watki)):
            if not watki[x].isAlive():
                del watki[x]
                liczba_aktywnych_watkow -= 1
                pbar.update(1)
                break


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        