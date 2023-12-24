"""
1. Receive url target
2. Send request to target and receive response
3. Missing
4. Warning
5. Raw Headers
"""

"""
Debug:
1. Argument expected one argument
"""

#library
import requests
from optparse import OptionError as ArgumentError
from controller.checks import checkHeader
from parse.cmdline import initOption

if __name__ == '__main__':
    try:
        parser, args = initOption()
        checkHeader(args.url, args.print)
    except requests.exceptions.MissingSchema:
        print("Invalid URL")
    except (ArgumentError, TypeError) as ex:
        parser.error(ex)
