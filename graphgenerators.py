import numpy as np
import networkx as nx


def erGraph(n: int, p: float=.5) -> np.array:
    '''Create adjacency matrix of random Erdos Renyi graph with parameter $p \in [0,1]$'''
    matA = np.zeros([n, n])
    edges = np.random.rand(n * (n - 1) // 2)
    edges = edges <= p
    matA[np.triu_indices(n, k=1)] = edges
    matA += matA.T
    return matA


def erGraph2(n: int, m: int) -> np.array:
    '''Compute adjacency matrix of random Erdos Renyi graph with expected number m of edges'''
    p = 2 * m / (n * (n-1))
    return erGraph(n, p)


def baGraph(n: int, m: int) -> np.array:
    '''Compute adjacency matrix of random Barabasi Albert graph that attaches m edges per new vertex'''
    return nx.adjacency_matrix(nx.barabasi_albert_graph(n, m)).toarray()


def baGraph2(n: int, m: int) -> np.array:
    '''Compute adjacency matrix of random Barabasi Albert graph with at most m edges'''
    m0 = m // n
    return nx.adjacency_matrix(nx.barabasi_albert_graph(n, m0)).toarray()


def random_permutation_matrix(n:int, p:int):
    '''Return a random permutation matrix for n elements. If p<n, perform a cyclic permutation of p randomly selected elements.'''
    if p == n:
        permutation = np.eye(n)
        np.random.shuffle(permutation)
        return permutation
    if p < n:
        idx = np.arange(n)
        np.random.shuffle(idx)
        idx = idx[:p]
        ring = np.hstack([idx[1:p], idx[0]])
        permutation = np.eye(n)
        permutation[idx, :] = permutation[ring, :]
        return permutation
    if p > n:
        raise ValueError(f'Parameter p must be at most as large as parameter n, but is {p} > {n}')
    

def distort_adjacency_matrix(g, i):
    '''Flip i indices in the adjacency matrix g.'''
    n = g.shape[0]
    idx = np.unravel_index(np.random.randint(0, n*n, size=i), shape=[n, n])
    gd = np.copy(g)
    gd[idx[0], idx[1]] = gd[idx[0], idx[1]] + 1 % 2
    gd[idx[1], idx[0]] = gd[idx[1], idx[0]] + 1 % 2
    return gd