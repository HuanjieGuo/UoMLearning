import numpy as np
import math

def tetrahedron():
    dist = np.ones((4,4))
    for i in range(4):
        dist[i,i] = 0
    return dist

def airline_dist():
    import pandas as pd

    data = pd.read_csv('./Data/dist_18_cities.csv')
    data.fillna(0, inplace=True)
    data = data.to_numpy()
    city = data[:,0].astype(str)
    dist = data[:,1:].astype(np.float64)
    return dist, city

def synthetic_spiral():
    """
    Spiral data
    """
    sqrt_two = math.sqrt(2)
    data = [ [math.cos(k/sqrt_two), math.sin(k/sqrt_two), k/sqrt_two] for k in range(30)]
    data = np.vstack(data)
    return data.T

def bars():
    file_name = './Data/bars.npz'
    data = np.load(file_name)
    v_bars = data['v_bars'].astype(np.float)
    v_centers = data['v_centers'].astype(np.float)
    h_bars = data['h_bars'].astype(np.float)
    h_centers = data['h_centers'].astype(np.float)
    return np.vstack((v_bars, h_bars)), np.vstack((v_centers, h_centers))

def face_tenenbaum():
    data = np.load('./Data/face_tenenbaum.npz')
    data = data['face']
    return data.T