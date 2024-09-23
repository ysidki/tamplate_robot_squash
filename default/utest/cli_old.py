#!/usr/bin/env python3
import argparse 
from utils.generate_score import send_all_scores_to_gamera

def main():
    # Command-line interface
    subparsers = parser.add_subparsers(dest='utest')
    parser_send_all_score = subparsers.add_parser('sendallscore', help='Send test automation score to Gamera by reading the score.xlsx')
    parser_send_all_score.set_defaults(func=send_all_scores_to_gamera)

    parser = argparse.ArgumentParser(description='utest command line')
    parser.add_argument('--name', type=str, help='Your name', required=True)
    args = parser.parse_args()

    # Call the script function with arguments
    # Parse arguments
    args = parser.parse_args()

    # Call the appropriate function based on the subcommand
    if hasattr(args, 'func'):
        args.func()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()