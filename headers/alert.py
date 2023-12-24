def alertHeaders(url, headers):
    #missing
    print("Warnings:")
    if 'x-frame-options' in headers:
        #warning
        if headers['x-frame-options'] == 'allow-from':
            print("The 'allow-from' directive of the X-Frame-Options header potentially permits untrusted websites to embed iframes and perform clickjacking.")
    else:
        print("X-Frame-Options tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking. Recommended value 'X-Frame-Options: SAMEORIGIN'.")