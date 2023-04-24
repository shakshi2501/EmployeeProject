import pandas as pd
import createdb
import equries

data = pd.read_csv('Employee_Dataset.csv', index_col=False, delimiter=',')
createdb.cdb(data)

equries.Queries()