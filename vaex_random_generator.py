import vaex
import pandas as pd
import numpy as np

csv_file = "files/df.csv"

n_rows = 10000
n_cols = 1000

N = 20

for i in range(20):
    df = pd.DataFrame(np.random.randint(0,100,size=(n_rows,n_cols)), columns=['col'+str(i) for i in range(n_cols)])
    vx = vaex.from_pandas(df)
    vx.export_hdf5("files/vx_files/vx"+str(i)+".hdf5")
print("Done")
