import requests
from headers.alert import alertHeaders
from headers.raw import rawHeaders

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