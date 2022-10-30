import leerdataset as dataset
import kmeans as km


datasetCompleta, x = dataset.leerData()


def kmeans(cantidadPruebas):

    for interador in range(cantidadPruebas):
        kmeans = km.Kmeans(datasetCompleta,7)
        kmeans.algoritmo()

kmeans(7)
