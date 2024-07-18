import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plotResult(minRow, maxRow, data, imgTitle):
    rowList = np.arange(minRow, maxRow + 1, 1)
    plotData = data.loc[rowList, :]
    plotData.plot(kind= "line", title= imgTitle)

# Read raw data file names
folderPath = input("폴더 경로: ")
fileNames = sorted(glob.glob(folderPath + "*"))

# Convert raw data to csv file
for file in fileNames:
    df = pd.read_table(file, names= ["col"])
    df = df.iloc[:, 0].str[-39:]
    df = pd.DataFrame(df, columns= ["col"])

    s1 = df["col"].str[4:9]
    s2 = df["col"].str[9:14]
    s3 = df["col"].str[14:19]
    s4 = df["col"].str[20:25]
    s5 = df["col"].str[25:30]
    s6 = df["col"].str[30:35]

    res = pd.concat((s1, s2), axis= 1)
    res = pd.concat((res, s3), axis= 1)
    res = pd.concat((res, s4), axis= 1)
    res = pd.concat((res, s5), axis= 1)
    res = pd.concat((res, s6), axis= 1)

    res.columns = ["s1", "s2", "s3", "s4", "s5", "s6"]

    saveFileName = str(file.split(f"{folderPath}")[1])
    # res.to_csv(folderPath + saveFileName + ".csv", sep= ",")

convertedFileList = sorted(glob.glob(folderPath + "*.csv"))

cols = [1, 2, 3, 4, 5, 6]

centerData = pd.read_csv(convertedFileList[1], usecols= cols)
leftData = pd.read_csv(convertedFileList[2], usecols= cols)
rightData = pd.read_csv(convertedFileList[3], usecols= cols)

baseMean = pd.read_csv(convertedFileList[0], usecols= cols)
baseMean = baseMean.mean(axis= 0).T.to_numpy().reshape(6, )
    
scaledCenterData = pd.DataFrame()
scaledLeftData = pd.DataFrame()
scaledRightData = pd.DataFrame()

for i in range(len(baseMean)):
    scaledCenterSensor = centerData.iloc[:, i] - baseMean[i]
    scaledCenterData = pd.concat((scaledCenterData, scaledCenterSensor), axis= 1)
    
    scaledLeftSensor = leftData.iloc[:, i] - baseMean[i]
    scaledLeftData = pd.concat((scaledLeftData, scaledLeftSensor), axis= 1)

    scaledRightSensor = rightData.iloc[:, i] - baseMean[i]
    scaledRightData = pd.concat((scaledRightData, scaledRightSensor), axis= 1)

