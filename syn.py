import sys
import math
import time

i = 0
while True:
    x = math.sin(float(i)*3.14/180)
    y = math.cos(float(i)*3.14/180)
    z = -x
    # print(str(x)+"\t"+str(y)+"\t"+str(z))
    print("{:10.2f}".format(x) + "\t" + "{:10.2f}".format(y) + "\t" + "{:10.2f}".format(z))
    sys.stdout.flush()
    i = i+1
    time.sleep(0.01)