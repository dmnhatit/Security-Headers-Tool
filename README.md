# Security Headers Tool
usage: secheaders.py [-h] [-u URL] [-p {alert,raw}]

Check the security headers of a website.

options:

  -h, --help            show this help message and exit

Target:

  -u URL, --url URL     target URL (e.g. "http://www.site.com/")

Option:

  -p {alert,raw}, --print {alert,raw} information will be printed, "alert" - Alerts about headers, "raw" - Information about raw headers, default is all

Reference Documents

[1] https://securityheaders.com/

[2] https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html#permissions-policy-formerly-feature-policy

[3] https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html

