"""
1. Receive url target
2. Send request to target and receive response
3. Missing
4. Warning
5. Raw Headers

"""

#library
import requests
import sys
import argparse

def checkHeader(url, option):
    #send HEAD request to fetch header
    res = requests.head(url)

    #fectch header
    headers = res.headers

    if option=="a":
        #missing
        print("Warnings:")
        if 'x-frame-options' in headers:
            #warning
            if headers['x-frame-options'] == 'allow-from':
                print("The 'allow-from' directive of the X-Frame-Options header potentially permits untrusted websites to embed iframes and perform clickjacking.")
        else:
            print("X-Frame-Options tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking. Recommended value 'X-Frame-Options: SAMEORIGIN'.")
    elif option=="r":
        #raw headers
        print("Raw Headers:")
        for key, value in headers.items():
            print(key, " : ", value)

if __name__ == '__main__':
    # Initialize parser with a short description
    parser = argparse.ArgumentParser(description='Check the security headers of a website.')

    # Add positional and optional arguments
    parser.add_argument('-u', help='target url')
    parser.add_argument('-p', help='information will be printed, "a" - Alerts about headers, "r" - Information about raw headers, default is all', default='all')

    # Parse argument
    args = parser.parse_args()

    try:
        checkHeader(args.u, args.p)
    except requests.exceptions.MissingSchema:
        print("Invalid URL")


