import os
print (os.getcwd())
numComp = {0:6,
           1:2,
           2:5,
           3:5,
           4:4,
           5:5,
           6:6,
           7:3,
           8:7,
           9:6}

inputString = input()
total = 0
for i in inputString:
    total += int(numComp[int(i)])
print (total)
    