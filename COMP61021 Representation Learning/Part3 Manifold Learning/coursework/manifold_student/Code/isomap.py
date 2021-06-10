import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
def nearest_neighbor_distance(X, n_neighbors):
    """
    Calculate distances of neigghbors for K-isomap
    
    Parameters
    ----------
    X: (d,n) array, where n is the number of points and d is its dimension
    n_neighbors: number of neighbors
        Select n_neighbors(k) nearest neighbors
    """
    
    # Compute distance map
    X_t = X.T
    distances = euclidean_distances(X_t, X_t)

    # Keep only the n_neighbors nearest neighbors, others set to 0 (= unreachable)
    neighbors = np.zeros_like(distances)
    sort_distances = np.argsort(distances, axis=1)[:, 1:n_neighbors+1]
    for k,i in enumerate(sort_distances):
        neighbors[k,i] = distances[k,i]
    return neighbors

def isomap(x, n_components, **kwargs):
    dist_type = kwargs['dist_type']

    # Step 1.
    # find nearest neighbors to each sample with the given condition
    if dist_type == 'radius':
        assert ('epsilon' in kwargs)
        epsilon = kwargs['epsilon']
        dist = kwargs['dist_func'](x, epsilon)
    elif dist_type == 'nearest':
        assert ('n_neighbors' in kwargs)
        n_neighbors = kwargs['n_neighbors']
        dist = kwargs['dist_func'](x, n_neighbors)
    else:
        raise ValueError("improper option")

    # Step 2.
    # Find shortest paths
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import shortest_path
    graph = csr_matrix(dist)
    dist_matrix, predecessors = shortest_path(csgraph=graph, 
                                              directed=False, 
                                              indices=None, 
                                              return_predecessors=True)

    # Step 3.
    # Apply cMDS
    Y, _, _ = kwargs['cmds_func'](X=dist_matrix, n_dim=n_components, input_type='distance')

    return Y, dist, predecessors