﻿"""
# A python script to plot sets of time-series data.
# Multiple sets can be plotted simultaneously.
# Ideally developed to plot setpoint vs system output in Robotic
   P.I.D controllers.

# Usage: python plot.py -t <X axis timesteps> -c <data channel>
# E.g.: ssh your_remote@192.168.2.9 'sudo ./your_project/your_program' | python \Desktop/plot_script.py -t 100 -c 4,13

# Adapted from 
https://manashpratim.com/plot-realtime-terminal-data
Manash Pratim Das (mpdmanash@iitkgp.ac.in)
"""

import sys, getopt
from collections import deque
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


class AnalogPlot:
    # constr
    def __init__(self, maxLen, variables):
        self.datan = []
        for i in range(variables):
            datai = deque([0.0] * maxLen)
            self.datan.append(datai)
        self.maxLen = maxLen
        self.variables = variables

    # add to buffer
    def addToBuf(self, buf, val):
        if len(buf) < self.maxLen:
            buf.append(val)
        else:
            buf.pop()
            buf.appendleft(val)

    # add data
    def add(self, data):
        assert(len(data) == self.variables)
        for i in range(self.variables):
            self.addToBuf(self.datan[i], data[i])

    # update plot
    def update(self, frameNum, an, values):
        try:
            data = values
            self.add(data)
            for i in range(self.variables):
                an[i].set_data(range(self.maxLen), self.datan[i])
        except KeyboardInterrupt:
            print('exiting')
        return

    # clean up
    def close(self):
        pass


def main(argv):
    # default plot parameters
    timesteps = 1000
    variables = 1

    try:
        opts, args = getopt.getopt(argv,"ht:c:")
    except getopt.GetoptError:
        print ('python plot.py -t < X axis timesteps > -n < number of variables>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print ('python plot.py -t < X axis timesteps > -n < number of variables>')
            sys.exit()
        elif opt == '-t':
            timesteps = int(arg)
        elif opt == '-c':
            channels = [int(i) for i in arg.split(',')]

    variables = len(channels)

    # variables = variables - 1

    print ('Using timesteps =', timesteps) 
    print ('Number of variables =', variables)
    analogPlot = AnalogPlot(timesteps, variables)
    fig = plt.figure()
    ax = plt.axes(xlim=(0, timesteps))
    an = []
    for i in range(variables):
        ai, = ax.plot([], [])
        an.append(ai)

    x = 1
    fig.show()

    while True:
        try:
            data = sys.stdin.readline()
            sys.stdout.write(data)
            sys.stdout.flush()
            parts = data.split('\t') # note: last element is '\n'
            
            if max(channels) <= len(parts)-1:
                # print(parts)
                channel = []
                for i in range(variables):
                    channel.append(parts[channels[i]-1])
                values = []
                for i in range(variables):
                    vi = float(channel[i])
                    values.append(vi)
                analogPlot.update(x, an, values)
                x = x + 1
                ax.relim()
                ax.autoscale_view(True,False,True)
                plt.draw()
                plt.pause(0.000001)
            else:
                print ('Invalid channel index: channel index is larger than the total number of availble data channels.')
                sys.exit()
        except KeyboardInterrupt:
            print('exiting.')
            sys.exit()

    analogPlot.close()
    print('exiting.')

main(sys.argv[1:])