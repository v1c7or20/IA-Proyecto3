import collections

class Cluster:
    def __init__(self,centroide):
        self.centroid = centroide
        self.individuos = []
    
    def anadirIndividuo(self,individuo):
        self.individuos.append(individuo)

    def freq(self):
        tamanio = len(self.individuos[0])
        temporal = []
        for iterador in self.individuos:
            temporal.append(iterador[tamanio-1])
        counter = collections.Counter(temporal)
        return counter
    
    def imprimirIndividuos(self):
        tamanio = len(self.individuos[0])
        for iterador in self.individuos:
            print(iterador[tamanio-1])
    
    
class Pareja:
    def __init__(self, individuo, id):
        #asignar cluster inicial de -1
        self.cluster = -1
        self.data = individuo
        self.id = id

    def asignarCluster(self, nuevoCluster):
        self.cluster = nuevoCluster

    def imprimirPareja(self,lista):
        print("{",self.cluster,",",lista[self.id],"}")

    def __eq__(self, x):
        comp = self.data == x.data
        lista = comp.all()
        return lista