import math
import random
import cluster as clst

class Kmeans:

    clusters = []
    
    def __init__(self,data,k):
        self.data = data
        self.k = k
        self.filas = len(data)
        self.columnas = len(data.columns)
        self.nombreColumnas = valoresUnicos(data.iloc[:,-1].values.tolist())

    def actualizarCentroides(self):
        #Lista de nuevos centroides
        nuevosCentroides = []

        for iterador in range(self.k):
            nuevoCentroide = []
            individuos = self.clusters[iterador].individuos
            tamanio = len(individuos)
            for iterador2 in individuos:
                if len(nuevoCentroide)==0:
                    nuevoCentroide = iterador2[:-1].copy()
                else:
                    temporal = [iterador2[x] + nuevoCentroide[x] for x in range(len(nuevoCentroide))]
                    nuevoCentroide = temporal.copy()

            centroideTemporal = [x / tamanio for x in nuevoCentroide]
            nuevosCentroides.append(centroideTemporal)
        return nuevosCentroides

    def asignarIndividosaClusters(self,centroides):
        for iterador in range(self.filas):
            row = self.data.iloc[iterador,:].values.tolist()
            distancias = [calculardistancia(row[:-1],centroides[iterador2]) for iterador2 in range(self.k)]
            minimoValor = min(distancias)
            indiceMinimoValor = distancias.index(minimoValor)
            self.clusters[indiceMinimoValor].anadirIndividuo(row)
    
    def asignarCentroideaCluster(self,centroides):
        for iterador in centroides:
            nuevoCluster = clst.Cluster(iterador)
            #Añado el nuevo cluster a mi lista clusters.
            self.clusters.append(nuevoCluster)
        
    def algoritmo(self):
        random_indexes = random.sample(range(self.filas), self.k)
        centroides = [self.data.iloc[i,:-1].values.tolist() for i in random_indexes]
        #Boleano para saber si tiene centroides diferentes
        centroidesDiferentes = True

        self.asignarCentroideaCluster(centroides)
        self.asignarIndividosaClusters(centroides)
        
        while centroidesDiferentes:
            nuevosCentroides = self.actualizarCentroides()

            if((len(nuevosCentroides) == len(centroides)) and (all(iterador in centroides for iterador in nuevosCentroides))):
                centroides = nuevosCentroides
                #Actualizo mi lista de clusters
                self.clusters.clear()
                self.asignarCentroideaCluster(centroides)
                self.asignarIndividosaClusters(centroides)
            else:
                centroidesDiferentes = False
        return self.clusters


def valoresUnicos(individuos):
    listaNombres = []
    valores = set(individuos)
    for iterador in valores:
        listaNombres.append(iterador)
    return listaNombres

def calculardistancia(centroide,filaActual):
    distancia = 0
    for iterador in range(len(centroide)):
        distancia += pow(centroide[iterador] - filaActual[iterador], 2)
    return math.sqrt(distancia)


def pares(individuos):
    pares = []
    lista = individuos.values.tolist()
    for iterador in range(len(lista)):
        temp = clst.Pair(lista[iterador], iterador)
        pares.append(temp)
    return pares

