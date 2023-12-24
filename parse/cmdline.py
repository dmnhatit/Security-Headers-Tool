import argparse

def initOption():
    # Initialize parser with a short description
    parser = argparse.ArgumentParser(description='Check the security headers of a website.')

    # Add positional and optional arguments
    target = parser.add_argument_group("Target")
    target.add_argument('-u', '--url', help='Target URL (e.g. \"http://www.site.com/\")')
    option = parser.add_argument_group("Option")
    option.add_argument('-p', '--print', choices=['alert', 'raw'], help='information will be printed, "alert" - Alerts about headers, "raw" - Information about raw headers, default is all', default='all')

    # Parse argument
    args = parser.parse_args()

    return parser, args