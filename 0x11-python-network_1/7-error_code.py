#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays:
- The body of the response if there are no errors
- The error code when there is an HTTP error.
"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        if response.status_code >= 400:
            print('Error code: {}'.format(response.status_code))
        else:
            print(response.text)
