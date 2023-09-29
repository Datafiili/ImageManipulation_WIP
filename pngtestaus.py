#I can't remember what this code was about.
#TODO: Figure it out

import math
pieces = 8
scores = []
Ascores = []
for i in range(pieces):
    scores.append(math.sin(math.pi / 2 / pieces * i))
    print(scores[i])
print("---------------------------")

for i in range(len(scores)):
    Ascores.append(math.asin(scores[i]))
    print(Ascores[i])