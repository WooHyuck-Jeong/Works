import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def getScaled(filePath):
    df = pd.read_csv(filePath, sep = ",", usecols = useCols)
    res = pd.DataFrame()
    
    for i in range(len(baseMean)):
        temp = df.iloc[:, i] - baseMean.iloc[i, 0]
        res = pd.concat((res, temp), axis = 1)

    return res

folderPath = input("Folder: ")
fileList = [file for file in sorted(glob.glob(folderPath + "*.csv")) if os.path.isfile(file)]

useCols = [0, 1, 2, 3, 4, 5]
base = pd.read_csv(fileList[0], sep = ",", usecols = useCols)
baseMean = pd.DataFrame(base.mean(axis= 0))
print(baseMean)

scaledCase1 = getScaled(fileList[1])
scaledCase10 = getScaled(fileList[2])
scaledCase11 = getScaled(fileList[3])
scaledCase12 = getScaled(fileList[4])
scaledCase13 = getScaled(fileList[5])
scaledCase14 = getScaled(fileList[6])
scaledCase15 = getScaled(fileList[7])
scaledCase2 = getScaled(fileList[8])
scaledCase3 = getScaled(fileList[9])
scaledCase4 = getScaled(fileList[10])
scaledCase5 = getScaled(fileList[11])
scaledCase6 = getScaled(fileList[12])
scaledCase7 = getScaled(fileList[13])
scaledCase8 = getScaled(fileList[14])
scaledCase9 = getScaled(fileList[15])

yMinLim = -2500
yMaxLim = 2500

fig, axs = plt.subplots(3, 5, figsize= (20, 10))
scaledCase1.plot(kind= "line", ax= axs[0, 0], title= "Case1", ylim= (yMinLim, yMaxLim))
scaledCase2.plot(kind= "line", ax= axs[0, 1], title= "Case2", ylim= (yMinLim, yMaxLim))
scaledCase3.plot(kind= "line", ax= axs[0, 2], title= "Case3", ylim= (yMinLim, yMaxLim))
scaledCase4.plot(kind= "line", ax= axs[0, 3], title= "Case4", ylim= (yMinLim, yMaxLim))
scaledCase5.plot(kind= "line", ax= axs[0, 4], title= "Case5", ylim= (yMinLim, yMaxLim))

scaledCase6.plot(kind= "line", ax= axs[1, 0], title= "Case6", ylim= (yMinLim, yMaxLim))
scaledCase7.plot(kind= "line", ax= axs[1, 1], title= "Case7", ylim= (yMinLim, yMaxLim))
scaledCase8.plot(kind= "line", ax= axs[1, 2], title= "Case8", ylim= (yMinLim, yMaxLim))
scaledCase9.plot(kind= "line", ax= axs[1, 3], title= "Case9", ylim= (yMinLim, yMaxLim))
scaledCase10.plot(kind= "line", ax= axs[1, 4], title= "Case10", ylim= (yMinLim, yMaxLim))

scaledCase11.plot(kind= "line", ax= axs[2, 0], title= "Case11", ylim= (yMinLim, yMaxLim))
scaledCase12.plot(kind= "line", ax= axs[2, 1], title= "Case12", ylim= (yMinLim, yMaxLim))
scaledCase13.plot(kind= "line", ax= axs[2, 2], title= "Case13", ylim= (yMinLim, yMaxLim))
scaledCase14.plot(kind= "line", ax= axs[2, 3], title= "Case14", ylim= (yMinLim, yMaxLim))
scaledCase15.plot(kind= "line", ax= axs[2, 4], title= "Case15", ylim= (yMinLim, yMaxLim))

plt.subplots_adjust(wspace= 0.4, hspace= 0.6)
plt.show()

# C:\Users\hyukk\Desktop\MagneticTest\Test2\Result\