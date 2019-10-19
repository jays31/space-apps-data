#!/usr/bin/python3

import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
dataframe = pd.read_csv("./records.csv")
print(dataframe.to_json(orient='records'))
input()
