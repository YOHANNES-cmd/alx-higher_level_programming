#!/usr/bin/python3
for j in range(0, 100):
    if j != 99:
        print("{:02d}".format(j), end=', ')
    else:
        print("{}".format(j), end='\n')
