from classes import Veiculo,Vertices
import random
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
import math
import collections


def Main():
    arquivo = open('instanciaMayron.txt','r')
    leitura = arquivo.readlines()
    numClientes=int(leitura[0])
    numSubRegioes=int(leitura[1])
    tiposVeiculos=int(leitura[2])
    horasJornada=int(leitura[3])
    listaClientes =[]
    '''
    numClientes=10
    numSubRegioes=5
    tiposVeiculos=5
    horasJornada = 7
    '''
    for cliente in range(4,(numClientes+4)):
        x,y,volume,valor,qtd=leitura[cliente].split()
        listaClientes.append(Vertices(float(x),float(y),float(volume),float(valor),float(qtd)))
    
    #listaClientes = [Vertices(random.uniform(0.01, 0.001),random.randint(10,1001), random.randint(1,11)) for i in range(0,numClientes)]
    
    # NÃO ESQUECER QUE : os 5 primeiros clientes são centros de distribuição
    for i in range(5):
        listaClientes[i].volumeMáximo = 0
        listaClientes[i].valorMáximo = 0
        listaClientes[i].qtdVeiculos = 0

    veiculos=[]

    for veiculo in range((4+numClientes),((4+numClientes) + 4 ) ):
        V,P,Nv,Vf,Vd,tc,td,ph,pkm,pf=leitura[veiculo].split()
        veiculos.append((float(V),float(P),float(Nv),float(Vf),float(Vd),float(tc),float(td),float(ph),float(pkm),float(pf)))
    
    '''
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

    for i in range(5):
        print(veiculos[i].V ," ",veiculos[i].P ," ",veiculos[i].Nv," ",veiculos[i].td," ",veiculos[i].ph," ",veiculos[i].pkm," ",veiculos[i].pf)
    '''


    #Montando o Grafo
    G=nx.Graph()
    for i in range (0,numClientes):
        G.add_node(i,pos=(listaClientes[i].x,listaClientes[i].y))

    #Peso de cada aresta é a distancia entre os pontos ( fórmula de dist.)
    for i in range(numClientes):
        for j in range(numClientes):
            if(i!=j):
                G.add_edge(i,j,weight= calculaDistanciaEntrePontos(listaClientes[i], listaClientes[j]))
    
    #Transforma o Grafo num Dicionario de Dicionarios
    MatrizDeDistancias = nx.to_dict_of_dicts(G)
    somaDosPedidos = 0
    for i in range(4,numClientes):
        somaDosPedidos += listaClientes[i].volumePedido
    somaDosPedidos = somaDosPedidos/5
    somaDosPedidos = round(somaDosPedidos,5)
    somaDosPedidos = somaDosPedidos*1 #Margem de erro de 7%
        
    #print(MatrizDeDistancias[0])
    #print(sorted(MatrizDeDistancias[0,0]))
    #print(sorted(MatrizDeDistancias[0],key = ))
    proximo0_peso = []
    proximo0_chave = []
    proximo1_peso = []
    proximo1_chave = []
    proximo2_peso = []
    proximo2_chave = []
    proximo3_peso = []
    proximo3_chave = []
    proximo4_peso = []
    proximo4_chave = []
    
    for i in range(5,numClientes):
        proximo0_chave.append(i)
        proximo0_peso.append(MatrizDeDistancias[0][i]['weight'])
    bubbleSort(proximo0_chave,proximo0_peso)

    for i in range(5,numClientes):
        proximo1_chave.append(i)
        proximo1_peso.append(MatrizDeDistancias[1][i]['weight'])
    bubbleSort(proximo1_chave,proximo1_peso)

    for i in range(5,numClientes):
        proximo2_chave.append(i)
        proximo2_peso.append(MatrizDeDistancias[2][i]['weight'])
    bubbleSort(proximo2_chave,proximo2_peso)

    for i in range(5,numClientes):
        proximo3_chave.append(i)
        proximo3_peso.append(MatrizDeDistancias[3][i]['weight'])
    bubbleSort(proximo3_chave,proximo3_peso)

    for i in range(5,numClientes):
        proximo4_chave.append(i)
        proximo4_peso.append(MatrizDeDistancias[4][i]['weight'])
    bubbleSort(proximo4_chave,proximo4_peso)
   
    area0 = [0]
    area1 = [1]
    area2 = [2]
    area3 = [3]
    area4 = [4]
    verticesInseridos = []

    fluxo0 = somaDosPedidos
    fluxo1 = somaDosPedidos
    fluxo2 = somaDosPedidos
    fluxo3 = somaDosPedidos
    fluxo4 = somaDosPedidos

    for i in range(0,(numClientes-5)):
        if(proximo0_chave[i] not in verticesInseridos and fluxo0 >= listaClientes[proximo0_chave[i]].volumePedido):
            area0.append(proximo0_chave[i])
            verticesInseridos.append(proximo0_chave[i])
            fluxo0 -= listaClientes[proximo0_chave[i]].volumePedido
        if(proximo1_chave[i] not in verticesInseridos and fluxo1 >= listaClientes[proximo1_chave[i]].volumePedido):
            area1.append(proximo1_chave[i])
            verticesInseridos.append(proximo1_chave[i] )
            fluxo1 -= listaClientes[proximo1_chave[i]].volumePedido
        if(proximo2_chave[i] not in verticesInseridos and fluxo2 >= listaClientes[proximo2_chave[i]].volumePedido):
            area2.append(proximo2_chave[i])
            verticesInseridos.append(proximo2_chave[i])
            fluxo2 -= listaClientes[proximo2_chave[i]].volumePedido
        if(proximo3_chave[i] not in verticesInseridos and fluxo3 >= listaClientes[proximo3_chave[i]].volumePedido):
            area3.append(proximo3_chave[i])
            verticesInseridos.append(proximo3_chave[i])
            fluxo3 -= listaClientes[proximo3_chave[i]].volumePedido
        if(proximo4_chave[i] not in verticesInseridos and fluxo4 >= listaClientes[proximo4_chave[i]].volumePedido):
            area4.append(proximo4_chave[i])
            verticesInseridos.append(proximo4_chave[i])
            fluxo4 -= listaClientes[proximo4_chave[i]].volumePedido
    
    print("Vetores Refetentes a cada Área")

    print("Area 0: ",area0)
   
    print("Area 1: ",area1)

    print("Area 2: ",area2)
 
    print("Area 3: ",area3)

    print("Area 4: ",area4)
    
    print()
    for i in range(0,(numClientes-5)):
        if(proximo0_chave[i] not in verticesInseridos):
            area0.append(proximo0_chave[i])
            verticesInseridos.append(proximo0_chave[i])
            fluxo0 -= listaClientes[proximo0_chave[i]].volumePedido
       
        if(proximo1_chave[i] not in verticesInseridos ):
            area1.append(proximo1_chave[i])
            verticesInseridos.append(proximo1_chave[i] )
            fluxo1 -= listaClientes[proximo1_chave[i]].volumePedido
       
        if(proximo2_chave[i] not in verticesInseridos ):
            area2.append(proximo2_chave[i])
            verticesInseridos.append(proximo2_chave[i])
            fluxo2 -= listaClientes[proximo2_chave[i]].volumePedido
       
        if(proximo3_chave[i] not in verticesInseridos  ):
            area3.append(proximo3_chave[i])
            verticesInseridos.append(proximo3_chave[i])
            fluxo3 -= listaClientes[proximo3_chave[i]].volumePedido
        
        if(proximo4_chave[i] not in verticesInseridos ):
            area4.append(proximo4_chave[i])
            verticesInseridos.append(proximo4_chave[i])
            fluxo4 -= listaClientes[proximo4_chave[i]].volumePedido
    

    G0=nx.Graph()
    G1=nx.Graph()
    G2=nx.Graph()
    G3=nx.Graph()
    G4=nx.Graph()

     #Cria Imagem do Grafo
  
    G0.add_node(0,pos0=(listaClientes[0].x,listaClientes[0].y))
    for i in area0:
        G0.add_node(i,pos0=(listaClientes[i].x,listaClientes[i].y))

    for i in area0:
        for j in area0:
            if(i!=j):
                G0.add_edge(i,j,weight= MatrizDeDistancias[i][j]['weight'])
                

    G1.add_node(1,pos1=(listaClientes[1].x,listaClientes[1].y))
    for i in area1:
        G1.add_node(i,pos1=(listaClientes[i].x,listaClientes[i].y))

    for i in area1:
        for j in area1:
            if(i!=j):
                G1.add_edge(i,j,weight= MatrizDeDistancias[i][j]['weight'])
    
    G2.add_node(2,pos2=(listaClientes[2].x,listaClientes[2].y))
    for i in area2:
        G2.add_node(i,pos2=(listaClientes[i].x,listaClientes[i].y))

    for i in area2:
        for j in area2:
            if(i!=j):
                G2.add_edge(i,j,weight= MatrizDeDistancias[i][j]['weight'])

    G3.add_node(3,pos3=(listaClientes[3].x,listaClientes[3].y))
    for i in area3:
        G3.add_node(i,pos3=(listaClientes[i].x,listaClientes[i].y))

    for i in area3:
        for j in area3:
            if(i!=j):
                G3.add_edge(i,j,weight= MatrizDeDistancias[i][j]['weight'])

    G4.add_node(4,pos4=(listaClientes[4].x,listaClientes[4].y))
    for i in area4:
        G4.add_node(i,pos4=(listaClientes[i].x,listaClientes[i].y))

    for i in area4:
        for j in area4:
            if(i!=j):
                G4.add_edge(i,j,weight= MatrizDeDistancias[i][j]['weight'])

    print("\nFluxo de Cada Centro de Distribuição")
    print("Fluxo 0: ",somaDosPedidos-fluxo0)
    print("Fluxo 1: ",somaDosPedidos-fluxo1)
    print("Fluxo 2: ",somaDosPedidos-fluxo2)
    print("Fluxo 3: ",somaDosPedidos-fluxo3)
    print("Fluxo 4: ",somaDosPedidos-fluxo4)

    arq = open('saida.txt', 'w')
    arq.write(str(somaDosPedidos-fluxo0))
    arq.write(str(somaDosPedidos-fluxo1))
    arq.write(str(somaDosPedidos-fluxo2))
    arq.write(str(somaDosPedidos-fluxo3))
    arq.write(str(somaDosPedidos-fluxo4))
    arq.close()


    #Conversão das subdivisões para dicionário de dicionário
    SubDivisao0= nx.to_dict_of_dicts(G0)
    SubDivisao1= nx.to_dict_of_dicts(G1)
    SubDivisao2= nx.to_dict_of_dicts(G2)
    SubDivisao3= nx.to_dict_of_dicts(G3)
    SubDivisao4= nx.to_dict_of_dicts(G4)


    '''
    #Impressao dos Grafos, só descomentar!
    
    #Grafo Completo
    pos=nx.get_node_attributes(G,'pos')
    nx.draw(G,pos,with_labels = True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.draw()
    plt.show()
    
    #Subdivisão 0
    pos0=nx.get_node_attributes(G0,'pos0')
    nx.draw(G0,pos0,with_labels = True)
    labels = nx.get_edge_attributes(G0,'weight')
    nx.draw_networkx_edge_labels(G0,pos0,edge_labels=labels)
    plt.draw()
    plt.show()    

    #Subdivisão 1
    pos1=nx.get_node_attributes(G1,'pos1')
    nx.draw(G1,pos1,with_labels = True)
    labels = nx.get_edge_attributes(G1,'weight')
    nx.draw_networkx_edge_labels(G1,pos1,edge_labels=labels)
    plt.draw()
    plt.show()

    #Subdivisão 2
    pos2=nx.get_node_attributes(G2,'pos2')
    nx.draw(G2,pos2,with_labels = True)
    labels = nx.get_edge_attributes(G2,'weight')
    nx.draw_networkx_edge_labels(G2,pos2,edge_labels=labels)
    plt.draw()
    plt.show()

    #Subdivisão 3
    pos3=nx.get_node_attributes(G3,'pos3')
    nx.draw(G3,pos3,with_labels = True)
    labels = nx.get_edge_attributes(G3,'weight')
    nx.draw_networkx_edge_labels(G3,pos3,edge_labels=labels)
    plt.draw()
    plt.show()

    #Subdivisão 4
    pos4=nx.get_node_attributes(G4,'pos4')
    nx.draw(G4,pos4,with_labels = True)
    labels = nx.get_edge_attributes(G4,'weight')
    nx.draw_networkx_edge_labels(G4,pos4,edge_labels=labels)
    plt.draw()
    plt.show()
    '''
    

#Método que calcula a distancia entre os pontos, o resultado é o peso das arestas!
def calculaDistanciaEntrePontos(i, j):
    return round(((i.x - j.x)**2 + (i.y - j.y)**2)**0.5,2)


#Ordenação utilizada para ordenar os clientes mais próximos de cada centro de dostribuição
def bubbleSort(chave,peso):
    for passnum in range(len(peso)-1,0,-1):
        for i in range(passnum):
            if peso[i]>peso[i+1]:
                temp = peso[i]
                temp2 = chave[i]
                peso[i] = peso[i+1]
                chave[i]=chave[i+1]
                peso[i+1] = temp
                chave[i+1] = temp2
   
Main()