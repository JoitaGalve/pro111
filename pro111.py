import plotly.figure_factory as ff
import pandas as pd
import csv
import random
import statistics
import plotly.graph_objects as go

df = pd.read_csv("article.csv")
data = df["reading_time"].tolist()


pMean = statistics.mean(data)
pstandardDeviation = statistics.stdev(data)

print("Mean of population is: " + str(pMean))
print("Standard deviation is: " + str(pstandardDeviation))

def randomSetOfMean(counter):
    dataSet = []

    for i in range(0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)

    sampleMean = statistics.mean(dataSet)
    standardDeviation = statistics.stdev(dataSet)

    return sampleMean

meanList = []
    
for i in range(0, 1000):
    setOfMeans = randomSetOfMean(30)
    meanList.append(setOfMeans)

sStdDev = statistics.stdev(meanList)
mean = statistics.mean(meanList)

print("Mean of sample is: " + str(mean))
print("Standard deviation is: " + str(sStdDev))



fstdStart, fstdEnd = mean - sStdDev, mean + sStdDev
sstdStart, sstdEnd = mean - (sStdDev * 2), mean + (sStdDev * 2)
tstdStart, tstdEnd = mean - (sStdDev * 2), mean + (sStdDev * 2)

print("Std 1: ", fstdStart, fstdEnd)
print("Std 2: ", sstdStart, sstdEnd)
print("Std 3: ", tstdStart, tstdEnd)

fig = ff.create_distplot([meanList], ["Reading time"], show_hist = False)
fig.add_trace(go.Scatter(x = [pMean, pMean], y = [0, 0.20], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [fstdStart, fstdStart], y = [0, 0.20], mode = "lines", name = "Standard Deviation"))
fig.add_trace(go.Scatter(x = [sstdStart, sstdStart], y = [0, 0.20], mode = "lines", name = "Standard Deviation"))
fig.add_trace(go.Scatter(x = [tstdStart, tstdStart], y = [0, 0.20], mode = "lines", name = "Standard Deviation"))

fig.add_trace(go.Scatter(x = [fstdEnd, fstdEnd], y = [0, 0.20], mode = "lines", name = "Standard Deviation"))
fig.add_trace(go.Scatter(x = [sstdEnd, sstdEnd], y = [0, 0.20], mode = "lines", name = "Standard Deviation"))
fig.add_trace(go.Scatter(x = [tstdEnd, tstdEnd], y = [0, 0.20], mode = "lines", name = "Standard Deviation"))
fig.show()
