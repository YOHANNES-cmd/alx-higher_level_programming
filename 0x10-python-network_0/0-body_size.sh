#!/bin/bash
# Gets the size of the body of a response from a URL
curl -sI "$1" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2
