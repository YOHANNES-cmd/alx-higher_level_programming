#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
"""
from urllib import request
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        with request.urlopen(url) as response:
            print(response.headers['X-Request-Id'])
