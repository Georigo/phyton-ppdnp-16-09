import numpy as np
import pandas as pd
import openpyxl

# pip install openpyxl

technologies = ['Spark', 'Pandas', 'Python', 'PHP']
fee = [25000, 20000, 15000, 18000, 22000]
deuration = ['50 Days', '30 Days', np.nan, '15 Days']
discount = [2000, 1500, 800, 500, 100]
colums = ['Columns', 'Fee', 'Duration', 'Discount']

df = pd.DataFrame(list(zip(technologies, fee, deuration, discount)), columns=colums)
print(df)
#   Columns    Fee Duration  Discount
# 0   Spark  25000  50 Days      2000
# 1  Pandas  20000  30 Days      1500
# 2  Python  15000      NaN       800
# 3     PHP  18000  15 Days       500

df.to_excel('courses.xlsx')
