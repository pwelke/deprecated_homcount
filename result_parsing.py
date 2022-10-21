import pandas as pd
import numpy as np

infiles = ['2022-10-19.csv', '2022-10-20.csv']

for infile in infiles:
    df = pd.read_csv(infile, header=None, delimiter=' ')
    print(df.groupby([5,6], ).agg(mean=(8, np.mean), std=(8, np.std)).to_latex())