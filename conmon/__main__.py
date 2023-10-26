# __main__.py

import sys
import pathlib
from conmon.cli import read_user_cli_args

def main():
    """Run Conmon Connection Checker"""
    user_args = read_user_cli_args()
    urls = _get_websites_urls(user_args)
    if not urls:
        print("Error: No URLs to check", file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)
     
def _get_websites_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += read_urls_from_file(user_args.input_file)
    return urls

def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: Empty input file, {file}", file=sys.stderr)
    else:
        print("Error: Input file not found", file=sys.stderr)
    return []
