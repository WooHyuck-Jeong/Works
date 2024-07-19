import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def getScaled(filePath):
    df = pd.read_csv(filePath, sep= ",", usecols= cols)
    res = pd.DataFrame()
    for i in range(len(baseMean)):
        temp = df.iloc[:, i] - baseMean[i]
        res = pd.concat((res, temp), axis= 1)
    return res

def plotResult(minRow, maxRow, data, imgTitle):
    rowList = np.arange(minRow, maxRow, 1)
    plotData = data.loc[rowList, :]
    plotData.plot(kind= "line", title= imgTitle, ylim= (-500, 500), figsize= (6, 5))

# Read file names
folderPath = input("Test2 Result Folder: ")
fileNames = sorted(glob.glob(folderPath + "*"))

res = pd.DataFrame()
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


# # Read csv files
convertedFileList = sorted(glob.glob(folderPath + "*.csv"))

base = pd.read_csv(convertedFileList[0], sep= ",", usecols= [1, 2, 3, 4, 5, 6])
baseMean = pd.DataFrame(base.mean(axis= 0)).T.to_numpy().reshape(6, )


cols = [1, 2, 3, 4, 5, 6]

scaledCase1 = getScaled(convertedFileList[1])
scaledCase10 = getScaled(convertedFileList[2])
scaledCase11 = getScaled(convertedFileList[3])
scaledCase12 = getScaled(convertedFileList[4])
scaledCase13 = getScaled(convertedFileList[5])
scaledCase14 = getScaled(convertedFileList[6])
scaledCase15 = getScaled(convertedFileList[7])
scaledCase2 = getScaled(convertedFileList[8])
scaledCase3 = getScaled(convertedFileList[9])
scaledCase4 = getScaled(convertedFileList[10])
scaledCase5 = getScaled(convertedFileList[11])
scaledCase6 = getScaled(convertedFileList[12])
scaledCase7 = getScaled(convertedFileList[13])
scaledCase8 = getScaled(convertedFileList[14])
scaledCase9 = getScaled(convertedFileList[15])

minRows = 1000
maxRows = 3300

plotResult(minRows, maxRows, scaledCase1, "Case1")
plotResult(minRows, maxRows, scaledCase2, "Case2")
plotResult(minRows, maxRows, scaledCase3, "Case3")
plotResult(minRows, maxRows, scaledCase4, "Case4")
plotResult(minRows, maxRows, scaledCase5, "Case5")
plotResult(minRows, maxRows, scaledCase6, "Case6")
plotResult(minRows, maxRows, scaledCase7, "Case7")
plotResult(minRows, maxRows, scaledCase8, "Case8")

plotResult(minRows, maxRows, scaledCase9, "Case9")
plotResult(minRows, maxRows, scaledCase10, "Case10")
plotResult(minRows, maxRows, scaledCase11, "Case11")
plotResult(minRows, maxRows, scaledCase12, "Case12")
plotResult(minRows, maxRows, scaledCase13, "Case13")
plotResult(minRows, maxRows, scaledCase14, "Case14")
plotResult(minRows, maxRows, scaledCase15, "Case15")

plt.show()

# C:\Users\hyukk\Desktop\Test2\