from ghc.utils.data import gen_bipartite
import pickle


if __name__ == '__main__':
    g, n_classes, y = gen_bipartite()
    pickle.dump(g, 'graph-homomorphism-graph-homomorphism-network/data/BIPARTITE.graph')
    pickle.dump(y, 'graph-homomorphism-graph-homomorphism-network/data/BIPARTITE.y')