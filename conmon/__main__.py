# __main__.py

import sys
from conmon.cli import read_user_cli_args

def main():
    """Run Conmon Connection Checker"""
    user_args = read_user_cli_args()
    urls = _get_websites_urls(user_args)
    if not urls:
        print("Error: No URLs to check", file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)
    