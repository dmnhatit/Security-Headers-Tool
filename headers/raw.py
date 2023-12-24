def rawHeaders(url, headers):
    #raw headers
    print("Raw Headers:")
    for key, value in headers.items():
        print("+", key, ":", value)