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

def checkArguments(parser, arguments):
    if not arguments.url:
        parser.exit(1, message="Argument -u expected one argument")
    if not arguments.print:
        parser.exit(1, message="Argument -p expected one argument")

def alertHeaders(url, headers):
    #missing
    print("Warnings:")
    if 'x-frame-options' in headers:
        #warning
        if headers['x-frame-options'] == 'allow-from':
            print("The 'allow-from' directive of the X-Frame-Options header potentially permits untrusted websites to embed iframes and perform clickjacking.")
    else:
        print("X-Frame-Options tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking. Recommended value 'X-Frame-Options: SAMEORIGIN'.")

def rawHeaders(url, headers):
    #raw headers
    print("Raw Headers:")
    for key, value in headers.items():
        print(key, " : ", value)

def checkHeader(url, option):
    #send HEAD request to fetch header
    res = requests.head(url)

    #fectch header
    headers = res.headers

    if option=="alert":
        alertHeaders(url, headers)
    elif option=="raw":
        rawHeaders(url, headers)
    elif option=="all":
        alertHeaders(url, headers)
        rawHeaders(url, headers)

def initOption():
    # Initialize parser with a short description
    parser = argparse.ArgumentParser(description='Check the security headers of a website.')

    # Add positional and optional arguments
    target = parser.add_argument_group("Target")
    target.add_argument('-u', '--url', help='target url')
    option = parser.add_argument_group("Option")
    option.add_argument('-p', '--print', choices=['alert', 'raw'], help='information will be printed, "alert" - Alerts about headers, "raw" - Information about raw headers, default is all', default='all')

    # Parse argument
    args = parser.parse_args()

    # Check arguments
    checkArguments(parser, args)

    return parser, args

if __name__ == '__main__':

    try:
        parser, args = initOption()
        checkHeader(args.u, args.p)
    except requests.exceptions.MissingSchema:
        print("Invalid URL")
