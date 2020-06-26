from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('postgresql://postgres:123@localhost:5432/bloggo')
df = pd.read_sql_query("SELECT * FROM users", con=engine)
df.columns.list()
df.values
print(df)
print(df.columns)