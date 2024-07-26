import os
import numpy as np
import pandas as pd

folderPath = "C:\\Users\\hyukk\\Desktop\\Rotation\\"
print("folder path", folderPath)

file = folderPath + "Base456"
print("file path :", file)

col_name = "col"
sensor_col_name = [f"s{i}" for i in np.arange(1, 7, 1)]

df = pd.read_table(file, names= [col_name], skiprows= 50)
df = df.iloc[:, 0].str[-39:]
df = pd.DataFrame(df, columns= [col_name])

s1 = df[col_name].str[4:9]
s2 = df[col_name].str[9:14]
s3 = df[col_name].str[14:19]
s4 = df[col_name].str[20:25]
s5 = df[col_name].str[25:30]
s6 = df[col_name].str[30:35]

res = pd.concat((s1, s2), axis= 1)
res = pd.concat((res, s3), axis= 1)
res = pd.concat((res, s4), axis= 1)
res = pd.concat((res, s5), axis= 1)
res = pd.concat((res, s6), axis= 1)

res.columns = sensor_col_name

save_file_name = str(file.split((f"{folderPath}"))[1])
save_path = folderPath + "result\\"

res.to_csv(save_path + save_file_name + ".csv", index= False)