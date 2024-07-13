import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 결과 저장 폴더 생성
def makeDirectory(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok= True)

# Read file names
folderPath = input("Test2 Result Folder: ")
fileNames = sorted(glob.glob(folderPath + "*"))

savePath = folderPath + "Result/"
makeDirectory(savePath)

# for file in fileNames:
#     df = pd.read_table(file, names= ["col"])
#     df = df.iloc[:, 0].str[-39:]
#     df = pd.DataFrame(df, columns= ["col"])

#     idx = df["col"].str[0:4]
#     s1 = df["col"].str[4:9]
#     s2 = df["col"].str[9:14]
#     s3 = df["col"].str[14:19]
#     s4 = df["col"].str[20:25]
#     s5 = df["col"].str[25:30]
#     s6 = df["col"].str[30:35]

#     res = pd.concat((idx, s1), axis= 1)
#     res = pd.concat((res, s2), axis= 1)
#     res = pd.concat((res, s3), axis= 1)
#     res = pd.concat((res, s4), axis= 1)
#     res = pd.concat((res, s5), axis= 1)
#     res = pd.concat((res, s6), axis= 1)

#     res.columns = ["idx", "s1", "s2", "s3", "s4", "s5", "s6"]

#     saveFileName = str(file.split(f"{folderPath}")[1])
    

#     res.to_csv(savePath + "/" + saveFileName + ".csv", sep= ",")

# Read csv files
convertedFileList = sorted(glob.glob(savePath + "*.csv"))

base = pd.read_csv(convertedFileList[0], sep= ",", usecols= [1, 2, 3, 4, 5, 6, 7])
# baseMean = pd.DataFrame(base.mean(axis= 0))
# # baseMean.columns = ["mean"]

# print(baseMean.head())