from time import sleep
from joblib import Parallel, delayed
from sqlalchemy import create_engine

r = Parallel(n_jobs=10, verbose=100)(delayed(sleep)(.2) for _ in range(10))

from pandas import DataFrame
import pandas as pd
import numpy as np
Cars = {'car': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'price': [22000,25000,27000,35000]
}
engine = create_engine('postgresql://postgres:123@localhost:5432/cardb')
df = DataFrame(Cars, columns= ['car', 'price'])
#df.to_sql('cars', con=engine, if_exists='replace')
print(df)
N = 500000
cars = pd.util.testing.rands_array(10, N)
prices = np.random.randint(5,30,size=N)
df = pd.DataFrame()
df['car'] = cars
df['price'] = prices
df.to_sql('cars', con=engine, if_exists='replace')