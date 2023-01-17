import sys
sys.path.append('graph-homomorphism-network/src')
from ghc.utils.data import load_json, save_json
import json
import itertools
import numpy as np

from pams import *

dloc = 'graph-homomorphism-network/data/precompute/'


def filter_overflow(patterns, sizes):
    minval = np.min(patterns, axis=0)
    patterns = patterns[:, minval >= 0]
    sizes = sizes[minval >= 0]

    if patterns.shape[1] > 0:
        return patterns, sizes
    else: 
        # if nothing worked, return zeros
        return np.zeros([patterns.shape[0], 1]), np.zeros(1)

for run_id, dataset, pattern_count, hom_type in itertools.product(run_ids, datasets, pattern_counts, hom_types):

    try:

        meta = load_json(dataset.upper(), hom_type, hom_size, pattern_count, run_id, dloc)

        pattern_sizes = np.array(meta['pattern_sizes'])
        data = meta['data']
        features = np.array([x['counts'] for x in data], dtype=float)

        size_before = pattern_sizes.shape[0]

        features, pattern_sizes = filter_overflow(features, pattern_sizes)

        size_after = pattern_sizes.shape[0]

        meta['pattern_sizes'] = pattern_sizes.tolist()
        for x, f in zip(data, features):
            x['counts'] = f.tolist()

        print(f'{dataset} {size_before}->{size_after}, min={np.min(features)}')

        save_json(meta, dataset.upper(), hom_type, hom_size, pattern_count, run_id, dloc, suffix='overflow_filtered')
    except FileNotFoundError:
        pass # we don't process whats not there