import pandas as pd
import matplotlib.pyplot as plt
import datetime

#excelFile = 'C:\MaximLogs\Rate 25.csv'
#excelFile = 'C:\MaximLogs\Rate 50.csv'
excelFile = 'C:\MaximLogs\Rate 100.csv'

pattern = '%Y-%m-%d %H:%M:%S.%f'

df1 = pd.read_csv(excelFile, usecols=['Time'])
df2 = pd.read_csv(excelFile, usecols=[' Green Count'])

arrX = []
arrY = []

for cell1 in df1.values:
    for x in cell1:
        arrX.append(datetime.datetime.strptime(x, pattern).timestamp())

for cell2 in df2.values:
    for y in cell2:
        arrY.append(y)

plt.plot(arrX, arrY)
plt.xlabel('Time-axis')
plt.ylabel('Green-axis')
plt.show()




# df1 = pd.read_csv(excelFile, usecols=['Time'])
# df2 = pd.read_csv(excelFile, usecols=[' Green Count'])
#
# arrX = df1.to_numpy()
# arrY = df2.to_numpy()
#
# x: str = str(arrX[0])
# for i in x:
#     print(i,end="")

# total = 0;
# index = 1;
# for i in x:
#     if i.isalnum():
#           if index is 1:
#               total += i * 31556926
#           elif index is 2:
#               total += i *

        



# x = ["A", "B", "C", "D", "E", "F"]
# y = [1,5,3, 7, 9, 2]

