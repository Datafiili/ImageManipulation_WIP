#I will probaly redo all of this.

import random
Data = []
for i in range(2):
    Data.append([])
    for k in range(5):
        Data[i].append(random.randint(0,256))
for i in range(len(Data)):
    print(Data[i])

def XA(Data):
    print("X-A")
    for i in range(len(Data) - 1,-1,-1):
        for k in range(len(Data[i]) - 1,0,-1):
            Data[i][k] -= Data[i][k-1]
    for i in range(len(Data)):
        print(Data[i])
XA(Data)