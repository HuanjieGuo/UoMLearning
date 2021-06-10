import numpy as np
from sklearn.neighbors import NearestNeighbors 
def radius_nbor_Mat(X, epsilon):
    Xt = X.T
    neigh = NearestNeighbors(radius=epsilon, metric="euclidean").fit(Xt)
    dist, nbors = neigh.radius_neighbors(Xt)
        
    return nbors

def Knbor_Mat(X, K):
    """
    K-nearest neighbours
    
    Parameters
    ----------
    X: (n,d) array, where n is the number of points and d is its dimensionality
    K: number of neighbours
    
    
    Returns
    -------
    nbours: (n,K) array.
        Indices of neighbours
    
    """
    Xt = X.T
    knn = NearestNeighbors(n_neighbors=K+1, metric="euclidean", algorithm="ball_tree").fit(Xt)
    distances, nbors = knn.kneighbors(Xt)
    
    return(nbors[:,1:])

def get_weights(data, nbors_idx, reg_func=None):
    """
    Calculate weights
    
    Parameters
    ----------
    data: (d,n) array, Input data
        d is its dimensionality
        n is the number of points. 
    nbors: (n,k) array. Indices of neghbours
        n is the number of points 
        k is the number of neighbours
    reg: regularization function
        
    Returns
    -------
    weights: (n,n) array. Weight matrix in row-major order
        weights[i,:] is weights of x_i
    """
    
    n = data.shape[1]
    weights = np.zeros((n, n))
   
    eps = 1e-3
    for i in range(n):
        x = data[:,i].reshape(-1,1)
        k = nbors_idx[i].shape[0] # number of neighbors
        ones = np.ones((k,1))

        # k-neareast neighbors
        eta = data[:,nbors_idx[i]]
        eta_t = eta.T
        C = eta_t.dot(eta)

        # regularization term
        if reg_func is None:
            trace = np.trace(C)
            if trace >0 :
                R = eps/k*trace
            else:
                R = eps
            C += np.eye(k)*R
        else:
            C += reg_func(C, k)

        # C_inv = np.linalg.inv(C)
        C_inv = np.linalg.pinv(C)

        # calculate lagranian multipler lamda
        tmp = eta_t.dot(x)
        lam_num = 1. - ones.T.dot(C_inv).dot(tmp)
        lam_denom = ones.T.dot(C_inv).dot(ones)
        lam = lam_num / lam_denom
        w = C_inv.dot(tmp + lam*ones)
        weights[i, nbors_idx[i]] = w.reshape(-1)
    
    return weights

from scipy.linalg import eigh

def Y_(Weights,d):
    """
    Calculate embedded coordinates in target space
    
    Parameters
    ----------
    Weights: (n,n) array, weight matrix
    d: dimensionality of target space
    
    Returns
    -------
    Y: (n,d) array
        Embedded coordinates in target space
    """
    n,p = Weights.shape
    I = np.eye(n)
    m = (I-Weights)
    M = m.T.dot(m)
    
    eigvals, eigvecs = eigh(M)
    ind = np.argsort(np.abs(eigvals))
    
    return(eigvecs[:, ind[1:d+1]])

def lle(data, n_components=2, n_neighbors=None, epsilon=None, reg_func=None):
    """
    Locally Linear Embedding 
    
    Parameters
    ----------
    data: (d,n) array, input data
        d is the dimensionality of points
        n is the number of points
    n_components: dimensionality in target space
    n_neighbors: number of nearest neighbors for KNN
    epsilon: fixed radius for epsilon-isomap
    reg_func: regularisation function
    
    Returns
    -------
    Y: (n,d) array
        Embedded coordinates in target space
    """
    # Select neighbors
    if epsilon is not None:
        nbors = radius_nbor_Mat(data, epsilon)
    elif n_neighbors is not None:
        nbors = Knbor_Mat(data,n_neighbors)

    # Reconstruct with linear weights
    Weights = get_weights(data, nbors, reg_func)

    # Map to embedded coordinates
    Y = Y_(Weights,n_components)
    
    return Y.T