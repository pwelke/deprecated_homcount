import subprocess
import itertools
import sys
import os

# parameters to iterate over
cwd = './'

datasets = ['MUTAG', 'CSL', 'PAULUS25', 'BZR']

executables = ['graph-homomorphism-network/models/feature_extraction.py', ] #'graph-homomorphism-network/models/mlp.py', 'graph-homomorphism-network/models/svm.py']

run_ids = ['slytherin1', 'slytherin2']

pattern_counts = [30, ] #10, 50, 100, 200]

hom_types = ['random_ktree']


for run_id, dataset, executable, pattern_count, hom_type in itertools.product(run_ids, datasets, executables, pattern_counts, hom_types):
    
    args = ['python', executable, 
            '--data', dataset,
            '--dloc', 'graph-homomorphism-network/data',
            '--pattern_count', str(pattern_count),
            '--run_id', run_id,
            '--hom_type', hom_type,
            '--hom_size', '-1',
            ]
    subprocess.run(args, cwd=cwd, stdout=sys.stdout, stderr=sys.stderr, check=True)
