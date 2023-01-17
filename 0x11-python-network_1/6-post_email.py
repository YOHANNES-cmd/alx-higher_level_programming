#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email,
and displays the body of the response
"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        form_data = [('email', email)]
        response = requests.post(url, data=form_data)
        print(response.text)
