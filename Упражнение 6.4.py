b = []
import math
a = [2, 4, 9, 16, 25]

for i in a:
    i = math.sqrt(i)
    b.append(i)

b = [math.sqrt(i) for i in a]

def i(a):
    return math.sqrt(a)

b = list(map(i,[2, 4, 9, 16, 25]))

            
