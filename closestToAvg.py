def avg(array):
    avg = sum(array) / len(array)
    return round(avg, 3)


def compareToAvg(array, average):
    arrayOfDifferences = []
    for i in range(len(array)):
        arrayOfDifferences.append(abs(array[i] - average))
    return arrayOfDifferences


fiveCounts = []
for i in range (5):
    fiveCounts.append(float(input()))    


average = avg(fiveCounts)
comparedValues = compareToAvg(fiveCounts, average)
minimalComparedValue = min(comparedValues)
indexOfClosestValue = comparedValues.index(minimalComparedValue)
theClosestValue = fiveCounts[indexOfClosestValue]
if theClosestValue.is_integer() == True:
    theClosestValue = int(theClosestValue)    


print("Average:", average)
print("Differences list: ", comparedValues)
# print("The minimal value of differences between average and value is: ", minimalComparedValue)
print("The closest value:", theClosestValue)