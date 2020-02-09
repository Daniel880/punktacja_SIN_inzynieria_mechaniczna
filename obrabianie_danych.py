
import re
import os
from tqdm import tqdm
import sys

od_roku = str(sys.argv[1])

lista_artykulow = os.listdir('./publikacje/{}'.format(od_roku))
lista_autorow = {}

for id_num in tqdm(range(len(lista_artykulow))):
    
    art_id = lista_artykulow[id_num][:-5]
    
    with open('./publikacje/{}/'.format(od_roku) + lista_artykulow[id_num],'rb') as f:
        req = f.read().decode("UTF-8")
        
        autorzy_PP = re.findall('people.+".(.+)<.+\n.+\n.+sin', req)
        autorzy_all = re.findall('people.+".(.+)<.+', req)
        
            
        punktacja = -1
        
        try:
            punktacja = re.findall('MNiSW.+\n+.+\n.+\n(.+\d)', req)[0]
            punktacja = re.findall('\d{1,3}', punktacja)[0]
            punktacja = int(punktacja)
        except:
            pass
            
        
        # liczba_publikacji, liczba_slotow, liczba_punktow
        if punktacja > 0:
            for a in autorzy_PP:
                if a not in lista_autorow:
                    lista_autorow[a] = [0,0,0]
                    
                lista_autorow[a][0] += 1
                lista_autorow[a][1] += 1/len(autorzy_all)
                lista_autorow[a].append(str(art_id))
                if punktacja >= 140:
                    lista_autorow[a][2] += punktacja
                else:
                    lista_autorow[a][2] += punktacja/len(autorzy_all)
        else:
            print("Pub bez pkt id:{}".format(art_id))

            
            
with open('Dane_{}.csv'.format(od_roku),'w') as f:
    f.write('Autor, Liczba publikacji, Liczba "slotow", liczba punktow na autora\n')
    for a in lista_autorow:
        f.write("{},".format(a))
        for i in lista_autorow[a]:
            f.write("{},".format(i))
        f.write("\n".format(a))
        
