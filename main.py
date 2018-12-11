from classes import Veiculo,Vertices
import random
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
import math

def Main():
    numClientes=100
    numSubRegioes=5
    tiposVeiculos=5
    horasJornada=7
    listaClientes = [Vertices(random.uniform(0.001, 0.01),random.randint(10,1001), random.randint(1,11)) for i in range(0,numClientes)]
    # NÃO ESQUECER QUE : os 5 primeiros clientes são centros de distribuição
    for i in range(5):
        listaClientes[i].volumeMáximo = 0
        listaClientes[i].valorMáximo = 0
        listaClientes[i].qtdVeiculos = 0
    veiculos = [Veiculo(0, 0, 0, 25, 30, 0.01, 0, 0, 0, 0) for i in range(5)]

    # Tipo 0: Van
    veiculos[0].V = random.randint(8,16)
    veiculos[0].P = random.randint(70000,75000)
    veiculos[0].Nv = random.randint(10,20)
    veiculos[0].td = random.uniform(0.04, 0.08)
    veiculos[0].ph = random.randint(30,60)
    veiculos[0].pkm = random.randint(2,4)
    veiculos[0].pf = random.randint(100,200)
    # Tipo 1: Mini-Van
    veiculos[1].V = random.randint(2,4)
    veiculos[1].P = random.randint(70000,75000)
    veiculos[1].Nv = random.randint(10,20)
    veiculos[1].td = random.uniform(0.02, 0.04)
    veiculos[1].ph = random.randint(30,60)
    veiculos[1].pkm = random.randint(2,4)
    veiculos[1].pf = random.randint(90,180)
    # Tipo 2: Comum
    veiculos[2].V = random.uniform(0.7,1.4)
    veiculos[2].P = random.randint(30000,35000)
    veiculos[2].Nv = random.randint(20,30)
    veiculos[2].td = random.uniform(0.02, 0.04)
    veiculos[2].ph = random.randint(30,60)
    veiculos[2].pkm = random.randint(1,2)
    veiculos[2].pf = random.randint(60,120)
    # Tipo 3: Motocicleta
    veiculos[3].V = random.uniform(0.02,0.04)
    veiculos[3].P = random.randint(1000,5000)
    veiculos[3].Nv = random.randint(20,30)
    veiculos[3].td = random.uniform(0.02, 0.04)
    veiculos[3].ph = random.randint(30,60)
    veiculos[3].pkm = random.randint(1,2)
    veiculos[3].pf = random.randint(40,80)
    # Tipo 4: Van terceirizada
    veiculos[4].V = random.uniform(0.08,0.16)
    veiculos[4].P = random.randint(75000,80000)
    veiculos[4].Nv = numClientes
    veiculos[4].td = random.uniform(0.04, 0.08)
    veiculos[4].ph = 0
    veiculos[4].pkm = random.randint(2,4)
    veiculos[4].pf = 0

    #Montando o Grafo
    G=nx.Graph()
    for i in range (0,10):
        G.add_node(i,pos=(listaClientes[i].x,listaClientes[i].y))

    #Peso de cada aresta é a distancia entre os pontos ( fórmula de dist.)
    for i in range(10):
        for j in range(10):
            if(i!=j):
               G.add_edge(i,j,weight= calculaDistanciaEntrePontos(listaClientes[i], listaClientes[j]))
    
    #Transforma o Grafo num Dicionario de Dicionarios
    Matriz = nx.to_dict_of_dicts(G)



    
    
    
    
    #Cria Imagem do Grafo
    pos=nx.get_node_attributes(G,'pos')
    nx.draw(G,pos,with_labels = True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.draw()
    plt.show()

def calculaDistanciaEntrePontos(i, j):
    return round(((i.x - j.x)**2 + (i.y - j.y)**2)**0.5,2)


Main()