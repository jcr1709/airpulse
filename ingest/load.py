import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://admin:admin@localhost:5432/de_project')

df= pd.read_csv('data/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69.csv')

df.to_sql("raw_air_quality", engine, if_exists='append', index=False)

print(f'loaded {len(df)} records to the database')