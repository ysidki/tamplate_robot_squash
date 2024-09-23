#!/usr/bin/env python3
import click
from ..utils.generate_score import send_all_scores_to_gamera

@click.group()
def cli():
    """A command-line tool with multiple scripts."""
    pass

@cli.command()
def sendallscores():
    """Send all scores to gamera"""
    print("sending scores to gamera")
    send_all_scores_to_gamera()

@cli.command()
def script2():
    """Run script 2."""
    print("Executing script 2")

if __name__ == "__main__":
    cli()