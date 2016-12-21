#!/usr/bin python

HELP = \
"""
usage:
    irs (-h | -v)
    irs [-l]
    irs -p PLAYLIST [-ng] [-c COMMAND] [-l]
    irs -a ARTIST (-s SONG | -A ALBUM [-st SEARCH_TERMS]) [-c COMMAND] [-l]

Options:
  -h, --help            show this help message and exit
  -v, --version         Display the version and exit.
  -c COMMAND, --command COMMAND
                        Run a background command with each song's location.
                        Example: `-c "rhythmbox %(loc)s"`
  -a ARTIST, --artist ARTIST
                        Specify the artist name.
  -p PLAYLIST, --playlist PLAYLIST
                        Specify playlist filename. Each line in the file
                        should be formatted like so: `SONGNAME - ARTIST`
  -s SONG, --song SONG  Specify song name of the artist.
  -A ALBUM, --album ALBUM
                        Specify album name of the artist.
  -st SEARCH_TERMS, --search-terms SEARCH_TERMS
                        Only use if calling -A/--album. Acts as extra search
                        terms when looking for the album.
  -l, --choose-link     If supplied, will bring up a console choice for what
                        link you want to download based off a list of titles.
  -ng, --no-organize    Only use if calling -p/--playlist. Forces all files
                        downloaded to be organized normally.
"""

# For exiting
from sys import exit

# Parsing args
import argparse

# Import the manager
from .manager import Manager

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='store_true', dest='help')
    parser.add_argument('-v', '--version', dest="version", action='store_true', help="Display the version and exit.")
    parser.add_argument('-c', '--command', dest="command", help="Run a background command with each song's location.")
    parser.add_argument('-a', '--artist', dest="artist", help="Specify the artist name.")

    parser.add_argument('-l', '--choose-link', action='store_true', dest="link", \
        help="Whether or not to choose the link from a list of titles.")

    parser.add_argument('-p', '--playlist', dest="playlist", \
    help="Specify playlist filename. Each line should be formatted like so: SONGNAME - ARTIST")
    parser.add_argument('-ng', '--no-organize', action="store_false", dest="no_organize", \
        help="Only use if calling -p/--playlist. Forces all files downloaded to be organizes normally.")

    media = parser.add_mutually_exclusive_group()
    media.add_argument('-s', '--song', dest="song", help="Specify song name of the artist.")

    media.add_argument('-A', '--album', dest="album", help="Specify album name of the artist.")
    parser.add_argument('-st', '--search-terms', dest="search_terms", \
        help="Only use if calling -A/--album. Acts as extra search terms for the album.")

    parser.add_argument('-o', '--order-files', action='store_true', dest="order_files",\
        help="Only use if callign with -p/--playlist or -A/--album. Adds a digit to front of each file specifying order.")


    args = parser.parse_args()

    if args.help:
        global HELP
        print (HELP)
        exit(1)

    Manager(args).main


if __name__ == "__main__":
    main()