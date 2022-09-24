#!/usr/bin/python3
""" A script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response """
from urllib.request import urlopen
import sys


url = sys.argv[1]
with urlopen(url) as response:
    body = response.info()
    print(body.get('X-Request-Id'))
