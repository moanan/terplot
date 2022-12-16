terplot
---
Plot terminal output (numbers) in real time.
![demo](https://user-images.githubusercontent.com/22083538/208100103-580f2bc3-ad75-4dc8-ac7a-c8509414689e.gif)

A python script to plot multiple channels of time-series data from terminal output.
Very useful for debugging setpoint vs system output in robotic applications, e.g. PID controllers.

Usage:
```bash
python3 plot.py -t <X axis index length> -c <data channel index (start from 0)>
```

Run the following command for a demo live plotting:
(the terminal output from syn.py will be plotted, for data channel 0, 1, 2)
```bash
python3 syn.py | python3 main.py -t 500 -c 0,1,2
```

You might want to replace the delimiter if you are not using 'Tab', search and update the following line:
```python
parts = data.split('\t') # note: last element is '\n'
```

You can easily debug a remote device with ssh connection, e.g.:
```bash
ssh your_remote@192.168.2.9 'sudo ./your_project/your_program' | python3 \Desktop/plot_script.py -t 100 -c 4,13
```

Adapted from Manash Pratim Das
https://manashpratim.com/plot-realtime-terminal-data
