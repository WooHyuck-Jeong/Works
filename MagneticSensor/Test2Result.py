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
    plotData.plot(kind= "line", title= imgTitle, ylim= (-1000, 1000))

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
    
    res.to_csv(folderPath + saveFileName + ".csv", sep= ",")

# # Read csv files
convertedFileList = sorted(glob.glob(folderPath + "*.csv"))

base = pd.read_csv(convertedFileList[0], sep= ",", usecols= [1, 2, 3, 4, 5, 6])
baseMean = pd.DataFrame(base.mean(axis= 0)).T.to_numpy().reshape(6, )


cols = [1, 2, 3, 4, 5, 6]

for file in convertedFileList:
    name = file.split(f"{folderPath}")[1]
    name = name.split(".")[0]
    
    if not name.startswith("B"):
        
        if name.endswith("1"):
            scaledCase1 = getScaled(file)
        elif name.endswith("2"):
            scaledCase2 = getScaled(file)
        elif name.endswith("3"):
            scaledCase3 = getScaled(file)
        elif name.endswith("4"):
            scaledCase4 = getScaled(file)
        elif name.endswith("5"):
            scaledCase5 = getScaled(file)
        elif name.endswith("6"):
            scaledCase6 = getScaled(file)
        elif name.endswith("7"):
            scaledCase7 = getScaled(file)
        elif name.endswith("8"):
            scaledCase8 = getScaled(file)

minRows = 100
maxRows = 2000

plotResult(minRows, maxRows, scaledCase1, "Case1")
plotResult(minRows, maxRows, scaledCase2, "Case2")
plotResult(minRows, maxRows, scaledCase3, "Case3")
plotResult(minRows, maxRows, scaledCase4, "Case4")
plotResult(minRows, maxRows, scaledCase5, "Case5")
plotResult(minRows, maxRows, scaledCase6, "Case6")
plotResult(minRows, maxRows, scaledCase7, "Case7")
plotResult(minRows, maxRows, scaledCase8, "Case8")
plt.show()

# C:\Users\hyukk\Desktop\Test2\