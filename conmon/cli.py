# cli.py

import argparse

def read_user_cli_args():
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="Conmon",
        description="Check Availability of Websites.(developed by vernonthedev)",
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        type=str,
        default=[],
        help="Enter one or more website URLs."
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Read URLs from a File."
    )
    return parser.parse_args()

