def alertHeaders(url, headers):
    print("- Alerts:")
    #missing - strict-transport-security
    if 'strict-transport-security' in headers:
        #warning
        if 'includeSubDomains' not in headers['strict-transport-security']:
            print("+ Cookies can be manipulated from sub-domains, so omitting the 'includeSubDomains' option permits a broad range of cookie-related attacks that HSTS would otherwise prevent by requiring a valid certificate for a subdomain.")
    else:
        print("+ HTTP Strict Transport Security is an excellent feature to support on your site and strengthens your implementation of TLS by getting the User Agent to enforce the use of HTTPS. Recommended value \"Strict-Transport-Security: max-age=31536000; includeSubDomains\".")

    #missing - content-security-policy
    if 'content-security-policy' in headers:
        #warning
        if 'unsafe-inline' in headers['content-security-policy']:
            print("+ This policy contains 'unsafe-inline' which is dangerous in the script-src directive.")
        if 'unsafe-eval' in headers['content-security-policy']:
            print("+ This policy contains 'unsafe-eval' which is dangerous in the script-src directive.")
    else:
        print("+ Content Security Policy is an effective measure to protect your site from XSS attacks. By whitelisting sources of approved content, you can prevent the browser from loading malicious assets.")

    #missing - x-frame-options
    if 'x-frame-options' in headers:
        #warning
        if  'allow-from' in headers['x-frame-options']:
            print("+ The 'allow-from' directive of the X-Frame-Options header potentially permits untrusted websites to embed iframes and perform clickjacking.")
    else:
        print("+ X-Frame-Options tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking. Recommended value 'X-Frame-Options: SAMEORIGIN'.")

    #missing - x-content-type-options
    if 'x-content-type-options' in headers:
        #warning
        pass
    else:
        print("+ X-Content-Type-Options stops a browser from trying to MIME-sniff the content type and forces it to stick with the declared content-type. The only valid value for this header is \"X-Content-Type-Options: nosniff\".")

    #missing - referrer-policy
    if 'referrer-policy' in headers:
        #warning
        if  'strict-origin-when-cross-origin' not in headers['referrer-policy']:
            print("+ The 'strict-origin-when-cross-origin' directive helps users prevent the disclosure of sensitive information.")
    else:
        print("+ Referrer Policy is a new header that allows a site to control how much information the browser includes with navigations away from a document and should be set by all sites.")

    #missing - referrer-policy
    if 'Permissions-Policy' in headers:
        #warning
        pass
    else:
        print("+ Permissions Policy is a new header that allows a site to control which features and APIs can be used in the browser.")