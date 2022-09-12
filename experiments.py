import subprocess
import itertools
import sys
import os

# parameters to iterate over
cwd = './'

datasets = ['MUTAG'] #['REDDIT-BINARY', 'IMDB-BINARY', 'PAULUS25', 'CSL', ]

executables = ['graph-homomorphism-network/models/mlp.py', ] #'graph-homomorphism-network/models/svm.py']

run_ids = ['taschenrechner']

pattern_counts = [10, ] #50, 100, 200]

hom_types = ['random_ktree']


for dataset, executable, pattern_count, hom_type, run_id in itertools.product(datasets, executables, pattern_counts, hom_types, run_ids):
    
    args = ['python', executable, 
            '--data', dataset,
            '--dloc', 'graph-homomorphism-network/data',
            '--pattern_count', str(pattern_count),
            '--run_id', run_id,
            '--hom_type', hom_type,
            ]
    subprocess.run(args, cwd=cwd, stdout=sys.stdout, stderr=sys.stderr, check=True)