import sys
sys.path.append('graph-homomorphism-network/src')
from ghc.utils.data import load_precompute_patterns
from ghc.generate_k_tree import get_pattern_list

import networkx as nx
import matplotlib.pyplot as plt

# datasets = ['MUTAG', ]#'CSL', 'PAULUS25', 'BZR', 'IMDBBINARY', 'IMDBMULTI', 'REDDIT-BINARY', 'NCI1', 'ENZYMES', 'DD', 'COLLAB']

# run_ids = ['run1',]#'run2','run3', 'run4', 'run5', 'run6', 'run7', 'run8', 'run9', 'run10']

# pattern_counts = [-5,] #[30, ] #10, 50, 100, 200]

# hom_types = ['random_ktree']

# hom_size = 'max'

# dloc = 'graph-homomorphism-network/data/precompute'

# patterns = load_precompute_patterns(datasets[0], hom_types[0], hom_size, pattern_counts[0], run_ids[0], dloc)

patterns, tree_decompositions = get_pattern_list(20, 20)

allpatterns = nx.disjoint_union_all(patterns)
nx.draw(allpatterns, arrows=False, node_size=20)
plt.show()