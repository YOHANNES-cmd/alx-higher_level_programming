#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of the variable X-Request-Id
in the response header
"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
