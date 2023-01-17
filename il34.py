import subprocess
import itertools
import sys
import os
import hashlib 

from pams import *

# parameters to iterate over
cwd = './'

executables = ['graph-homomorphism-network/models/fabian_extraction.py', ] 

datasets = ['ogbg-molsider',
            'ogbg-moltoxcast',
            'ogbg-mollipo',
            ]

# download and preprocess all datasets
args = ['python', 'import_from_ogb.py']
subprocess.run(args, cwd=cwd, stdout=sys.stdout, stderr=sys.stderr, check=True)
args = ['python', 'import_from_pyg.py']
subprocess.run(args, cwd=cwd, stdout=sys.stdout, stderr=sys.stderr, check=True)


# a deterministic hash function returning a 32 bit integer value for a given utf-8 string
hashfct = lambda x: str(int(hashlib.sha1(bytes(x, 'utf-8')).hexdigest(), 16) & 0xFFFFFFFF)

for run_id, dataset, executable, pattern_count, hom_type in itertools.product(run_ids, datasets, executables, pattern_counts, hom_types):
    print(f'{run_id}: {dataset} {executable}')    
    args = ['python', executable, 
            '--data', dataset,
            '--seed', hashfct(run_id),
            '--dloc', 'graph-homomorphism-network/data',
            '--pattern_count', str(pattern_count),
            '--run_id', run_id,
            '--hom_type', hom_type,
            '--hom_size', '-1',
            ]
    print(args)
    subprocess.run(args, cwd=cwd, stdout=sys.stdout, stderr=sys.stderr, check=True)

# remove features with problems
args = ['python', 'convert_to_overflowfiltered.py']
subprocess.run(args, cwd=cwd, stdout=sys.stdout, stderr=sys.stderr, check=True)
