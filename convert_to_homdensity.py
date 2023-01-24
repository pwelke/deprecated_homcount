import sys
sys.path.append('graph-homomorphism-network/src')
from ghc.utils.data import load_json, save_json
import json
import itertools


def file_homdensity_filter(run_ids, datasets, pattern_counts, hom_types):

    for run_id, dataset, pattern_count, hom_type in itertools.product(run_ids, datasets, pattern_counts, hom_types):

        try:

            meta = load_json(dataset.upper(), hom_type, hom_size, pattern_count, run_id, dloc)

            pattern_sizes = meta['pattern_sizes']
            data = meta['data']

            def density(n, counts, sizes):
                return [c / (n ** s) for c,s in zip(counts, sizes)]

            for x in data:
                hom_density = density(x['vertices'], x['counts'], pattern_sizes)
                x['counts'] = hom_density

            save_json(meta, dataset.upper(), hom_type, hom_size, pattern_count, run_id, dloc, suffix='densities')
        except FileNotFoundError:
            pass # we don't process whats not there
if __name__ == "__main__":
    datasets = ['ogbg-moltox21',
            'ogbg-molesol',
            'ogbg-molbace',
            'ogbg-molclintox',
            'ogbg-molbbbp',
            'ogbg-molsider',
            'ogbg-moltoxcast',
            'ogbg-mollipo',
            'ogbg-molhiv',]

    run_ids = ['il3',]# 'il4',] #'run3', 'run4', 'run5', 'run6', 'run7', 'run8', 'run9', 'run10']

    pattern_counts = [50,] #[30, ] #10, 50, 100, 200]

    hom_types = ['full_kernel']

    hom_size = 'max'

    dloc = 'forFabian/2023-01-12_fixedreps/'

    file_homdensity_filter(run_ids, datasets, pattern_counts, hom_types)
