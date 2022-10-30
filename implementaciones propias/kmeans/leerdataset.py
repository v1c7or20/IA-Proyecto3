import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


#Lectura de la data.
def leerData(dataset = 'dataset_tissue.txt', clases = 'clases'):
    df = pd.read_csv(dataset, delimiter = ",")
    df.rename(columns={'Unnamed: 0':'ROW_NAME'}, inplace=True)
    numeroColumnas = df.columns.size
    df = df.T
    
    y = pd.read_csv(clases, delimiter = ",")
    y.rename(columns={'x':'tissue'}, inplace=True)
    y_list = y.iloc[:,-1].values.tolist()
    
    x = df.iloc[1:numeroColumnas,:]
    dataCompleta = x.copy()
    dataCompleta['tissue'] = y_list
    return dataCompleta, x

