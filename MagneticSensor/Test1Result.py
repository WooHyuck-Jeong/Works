import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def makeDirectory(dirName):
    """
        폴더 생성 함수
    """
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok= True)

def plotResult(minRow, maxRow, data, imgTitle):
    rowList = np.arange(minRow, maxRow, 1)
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

    res = pd.concat((s1, s2), axis=1)
    res = pd.concat((res, s3), axis=1)
    res = pd.concat((res, s4), axis=1)
    res = pd.concat((res, s5), axis=1)
    res = pd.concat((res, s6), axis=1)

    res.columns = ["s1", "s2", "s3", "s4", "s5", "s6"]
    
    saveFileName = str(file.split(f"{folderPath}")[1])
    # res.to_csv(folderPath + saveFileName + ".csv", sep = ",")

# Read csv files
convertedFileList = sorted(glob.glob(folderPath + "*.csv"))

sensor1Data = pd.DataFrame()
sensor2Data = pd.DataFrame()
sensor3Data = pd.DataFrame()
sensor4Data = pd.DataFrame()
sensor5Data = pd.DataFrame()
sensor6Data = pd.DataFrame()

dfBaseMean = pd.DataFrame()

for file in convertedFileList:
    name = file.split(f"{folderPath}")[1]

    if name.startswith("s"):
        distance = name.split('_')[1]
        distance = distance.split(".")[0]

        if name.split("_")[0] == "s1":
            sensorData = pd.read_csv(file, sep= ",", usecols= [1], names = [f"d{distance}"], skiprows= [0])
            sensor1Data = pd.concat((sensor1Data, sensorData), axis = 1)
            
        elif name.split("_")[0] == "s2":
            sensorData = pd.read_csv(file, sep= ",", usecols= [2], names = [f"d{distance}"], skiprows= [0])
            sensor2Data = pd.concat((sensor2Data, sensorData), axis = 1)

        elif name.split("_")[0] == "s3":
            sensorData = pd.read_csv(file, sep= ",", usecols= [3], names = [f"d{distance}"], skiprows= [0])
            sensor3Data = pd.concat((sensor3Data, sensorData), axis = 1)

        elif name.split("_")[0] == "s4":
            sensorData = pd.read_csv(file, sep= ",", usecols= [4], names = [f"d{distance}"], skiprows= [0])
            sensor4Data = pd.concat((sensor4Data, sensorData), axis = 1)

        elif name.split("_")[0] == "s5":
            sensorData = pd.read_csv(file, sep= ",", usecols= [5], names = [f"d{distance}"], skiprows= [0])
            sensor5Data = pd.concat((sensor5Data, sensorData), axis = 1)

        elif name.split("_")[0] == "s6":
            sensorData = pd.read_csv(file, sep= ",", usecols= [6], names = [f"d{distance}"], skiprows= [0])
            sensor6Data = pd.concat((sensor6Data, sensorData), axis = 1)

    elif name.startswith("Base"):
        base = pd.read_csv(file, sep= ",", usecols= [1, 2, 3, 4, 5, 6])
        baseMean = base.mean(axis = 0)
        dfBaseMean = pd.concat((dfBaseMean, baseMean), axis= 1).T.to_numpy().reshape(6,)

scaledSensor1 = sensor1Data - dfBaseMean[0]
scaledSensor2 = sensor2Data - dfBaseMean[1]
scaledSensor3 = sensor3Data - dfBaseMean[2]
scaledSensor4 = sensor4Data - dfBaseMean[3]
scaledSensor5 = sensor5Data - dfBaseMean[4]
scaledSensor6 = sensor6Data - dfBaseMean[5]

plotResult(1000, 3000, scaledSensor1, "Sensor 1")
plotResult(1000, 3000, scaledSensor2, "Sensor 1")
plotResult(1000, 3000, scaledSensor3, "Sensor 1")
plotResult(1000, 3000, scaledSensor4, "Sensor 4")
plotResult(1000, 3000, scaledSensor5, "Sensor 5")
plotResult(1000, 3000, scaledSensor6, "Sensor 6")
plt.show()