#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status str version"""

from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as fetch:
        page = fetch.read()
        page = page.decode('utf-8')
        print("Body response:")
        print("\t- type: " + str(type(page)))
        print("\t- content: " + str(page))
