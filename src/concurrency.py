from time import sleep
from joblib import Parallel, delayed
from sqlalchemy import create_engine
from loky import wrap_non_picklable_objects

#r = Parallel(n_jobs=10, verbose=100)(delayed(sleep)(.2) for _ in range(10))

from pandas import DataFrame
import pandas as pd
import numpy as np
import time
start_time = time.time()
engine = create_engine('postgresql://postgres:123@localhost:5432/cardb')
N = 5000
cars = pd.util.testing.rands_array(10, N)
prices = np.random.randint(5,30,size=N)
data = pd.DataFrame()
data['car'] = cars
data['price'] = prices
split_n = 1000

@delayed
@wrap_non_picklable_objects
def insert_df(df):
    df.to_sql('cars', con=engine, if_exists='replace')
group_data = data.groupby(np.arange(len(data)) // split_n)
r = Parallel(n_jobs=10)(delayed(insert_df)(df) for _,df in group_data)
for i, df in group_data:
    insert_df(df)
    print(df.shape)
print("Execution success in %s " % (time.time() - start_time))