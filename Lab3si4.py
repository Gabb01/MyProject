import sys
from collections import namedtuple

from random import shuffle

Drum = namedtuple("Drum", ['A', 'B', 'dist'])

Nod = namedtuple("Nod", ['stare','predecesori','d','g'])

estimare = {
"Arad": 366,
"Bucuresti": 0,
"Craiova": 160,
"Drobeta": 242,
"Fagaras": 172,
"Giurgiu": 77,
"Hirsova": 151,
"Eforie": 161,
"Iasi": 226,
"Lugoj": 244,
"Mehadia": 241,
"Neamt": 234,
"Oradea": 380,
"Pitesti": 100,
"Rimnicu_Valcea": 193,
"Sibiu": 253,
"Timisoara": 329,
"Urziceni": 80,
"Vaslui": 199,
"Zerind": 374}

def expandare(nod):
    noduri = []
    for drum in drumuri:
        if(drum.A == nod.stare) and (drum.B not in nod.predecesori):
            nod3 = Nod(drum.B, nod.predecesori[:]+[nod.stare], nod.d+1, nod.g + drum.dist)
            noduri.append(nod3)
        if(drum.B == nod.stare) and (drum.A not in nod.predecesori):
            nod3 = Nod(drum.A, nod.predecesori[:]+[nod.stare], nod.d+1, nod.g + drum.dist)
            noduri.append(nod3)
    return noduri
    
def citire_date_din_fisier(fisier):
    input_data = ""
    with open(fisier, 'r') as f:
        input_data = f.read().split('\n')
        
    linie = input_data[0].split()
    numar_orase = int(linie[0])
    numar_drumuri = int(linie[1])
    
    drumuri = []
    
    for i in range(1, numar_drumuri+1):
        linie = input_data[i].split()
        drumuri.append(Drum(linie[0], linie[1], int(linie[2])))
        
        
    return numar_orase, drumuri
    
    
locatie_fisier = "D:\\work\\map_input.txt"
numar_orase, drumuri = citire_date_din_fisier(locatie_fisier)
numar_drumuri = len(drumuri)

drum = drumuri[0]

stare_initiala = "Arad"
stare_finala   = "Bucuresti"
nod_initial = Nod(stare_initiala, [], 0, 0)

#########

def select_dupa_adancime(frontiera):
    nod = frontiera[-1]
    del frontiera[-1] #se sterge ultimul element din frontiera
    return nod, frontiera

def select_dupa_largime(frontiera):
    nod = frontiera[0]
    del frontiera[0] #este echivalent cu frontiera[:-2] #Stergem primul element din frontiera
    return nod,frontiera
    
def select_g(nod):
    return nod.g
    
def select_dupa_cost_minim(frontiera):
#    frontiera.sort(key = select_g)
    frontiera.sort(key = lambda nod:nod.g, reverse=True)
    nod = frontiera[-1]
    del frontiera[-1] #este echivalent cu frontiera[:-2] #Stergem primul element din frontiera
    return nod,frontiera
    
def select_dupa_greedy(frontiera):
    frontiera.sort(key = lambda nod: estimare[nod.stare], reverse=True)
    nod = frontiera[-1]
    del frontiera[-1] #este echivalent cu frontiera[:-2] #Stergem primul element din frontiera
    return nod,frontiera

def select_dupa_a(frontiera):
    frontiera.sort(key = lambda nod:nod.g + estimare[nod.stare], reverse=True)
    nod = frontiera[-1]
    del frontiera[-1] #este echivalent cu frontiera[:-2] #Stergem primul element din frontiera
    return nod,frontiera
#########


#Cautare in Adancime
def cauta(nod, sf, select_dupa=select_dupa_adancime):
    count = 0
    frontiera = [nod]
    while(frontiera != []):
        nod, frontiera = select_dupa(frontiera)
        if nod.stare == sf:
            return nod, count, len(frontiera)
        frontiera.extend(expandare(nod))
        count = count+1
        if count == 10000:
            break
    print("Fara solutii")
    return nod, count, len(frontiera)

for _ in range(2):    
    shuffle(drumuri)
    info = cauta(nod_initial, stare_finala, select_dupa=select_dupa_a)
    print(info)
    