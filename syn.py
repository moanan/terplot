import sys
import math
import time

i = 0
while True:
    x = math.sin(float(i)*3.14/180)
    y = math.cos(float(i)*3.14/180)
    z = -x
    print(str(x)+"\t"+str(y)+"\t"+str(z))
    sys.stdout.flush()
    i = i+1
    time.sleep(0.01)