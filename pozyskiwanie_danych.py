import urllib
import re
from tqdm import tqdm
from threading import Thread 


lista_stron = ['https://sin.put.poznan.pl/search/publications/all?yearFrom=2018&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page=1',
                'https://sin.put.poznan.pl/search/publications/all?yearFrom=2018&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page=2',
                'https://sin.put.poznan.pl/search/publications/all?yearFrom=2018&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page=3',
                'https://sin.put.poznan.pl/search/publications/all?yearFrom=2018&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page=4',
                'https://sin.put.poznan.pl/search/publications/all?yearFrom=2018&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page=5',
                'https://sin.put.poznan.pl/search/publications/all?yearFrom=2018&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page=6',
                'https://sin.put.poznan.pl/search/publications/all?yearFrom=2018&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page=7',
                'https://sin.put.poznan.pl/search/publications/all?yearFrom=2018&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page=8',
                'https://sin.put.poznan.pl/search/publications/all?yearFrom=2018&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page=9',
                'https://sin.put.poznan.pl/search/publications/all?yearFrom=2018&yearTo=2020&disciplineCode=inzynieria-mechaniczna&page=10',
               ]

lista_id = []

cnt=0
for url in lista_stron:
    cnt+=1
    print("pobieram dane strona:{}".format(cnt))
    req = urllib.request.urlopen(url).read().decode("UTF-8")
    pub_id = re.findall('href="/publications/details/(i\d{1,6})">', req)
    for i in pub_id:
        lista_id.append(i)
    
print("liczba publikacji:{}".format(len(lista_id)))


lista_autorow = {}


def pobierz_html(art_id):
    req = urllib.request.urlopen('https://sin.put.poznan.pl/publications/details/' + art_id).read()

    with open('pub_18_20/' + art_id+'.html','wb') as f:
        f.write(req)

watki = []

for id_num in tqdm(range(len(lista_id))):
    watki.append(Thread(target = pobierz_html, args =(lista_id[id_num])))
    watki[-1].start()
    
for i in tqdm(range(len(watki))):
    watki[i].join()
