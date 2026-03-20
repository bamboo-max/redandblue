import pandas as pd

df = pd.read_excel("xsq.xlsx")

data1 = df.tail(5) #读取文件后2行
rows_as_dicts = data1.to_dict(orient='records') #将读取DataFrame 对象转换为字典
print(rows_as_dicts)

for val in rows_as_dicts:
    print(val["redstr"])