"""
 _                                   _      
| |_ ___ _ __ _ __ ___    _ __ _   _| | ___ 
| __/ _ \ '__| '_ ` _ \  | '__| | | | |/ _ \
| ||  __/ |  | | | | | | | |  | |_| | |  __/
 \__\___|_|  |_| |_| |_| |_|   \__,_|_|\___|
 
author: Nauman Ahmad
description: Provide a coloured horizontal rule for your terminal.
version: 0.14
license: MIT
"""
from __future__ import print_function
from __future__ import division

from termcolor import colored
import os
import struct
import fcntl
import termios
import argparse


class InvalidColorException(Exception):

    """
    Exception raised when invalid color name is entered
    """
    pass


class TermRule(object):

    @staticmethod
    def _echo(msg, color_name):
        """
        Colored outputs to terminal using the termcolor library
        """
        try:
            return colored(msg, color_name)
        except:
            raise InvalidColorException("Invalid Color Name!")

    @classmethod
    def _parse_args(cls):
        """
        Method to parse command line arguments
        """
        cls.parser = argparse.ArgumentParser()
        cls.parser.add_argument(
            "symbol", help="Symbol for horizontal line", nargs="*")
        cls.parser.add_argument(
            "--color", "-c", help="Color of the line", default=None, nargs=1)
        cls.parser.add_argument(
            "--version", "-v", action="version", version="0.13")

        return cls.parser

    def run_args(self):
        """
        Pass in the parsed args to the script
        """
        self.arg_parser = self._parse_args()
        self.args = self.arg_parser.parse_args()
        color_name = self.args.color
        if color_name is not None:
            color_name = color_name[0]
        symbol = self.args.symbol
        try:
            self.tr(symbol, color_name)
        except InvalidColorException:
            print("Invalid Color Name!")

    def _ioctl_GWINSZ(self, fd):
        return struct.unpack("hh", fcntl.ioctl(fd, termios.TIOCGWINSZ, "1234"))

    def _term_size(self):
        """
        Method returns lines and columns according to terminal size
        """
        for fd in (0, 1, 2):
            try:
                return self._ioctl_GWINSZ(fd)
            except:
                pass
        # try os.ctermid()
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            try:
                return self._ioctl_GWINSZ(fd)
            finally:
                os.close(fd)
        except:
            pass
        # try `stty size`
        try:
            return tuple(int(x) for x in os.popen("stty size", "r").read().split())
        except:
            pass
        # try environment variables
        try:
            return tuple(int(os.getenv(var)) for var in ("LINES", "COLUMNS"))
        except:
            pass
        # i give up. return default.
        return (25, 80)

    def tr(self, args, color=None):
        """
        Method to print ASCII patterns to terminal
        """
        width = self._term_size()[1]
        if not args:
            if color is not None:
                print(self._echo("#" * width, color))
            else:
                print(self._echo("#" * width, "green"))
        else:
            for each_symbol in args:
                chars = len(each_symbol)
                number_chars = width // chars
                if color is not None:
                    print(self._echo(each_symbol * number_chars, color))
                else:
                    print(each_symbol * number_chars)


def main():
    """
    Main function for the entry point in setup.py
    """
    app = TermRule()
    app.run_args()

if __name__ == "__main__":
    # If this program is run as a script
    main()
