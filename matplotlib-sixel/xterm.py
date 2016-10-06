#!/usr/bin/env python
import curses

from sys import stdin, stdout


class raw_terminal(object):
    """ change terminal mode that the input is unbuffered """
    def __init__(self, fd):
        self.fd = fd

    def __enter__(self):
        curses.initscr()
        curses.cbreak()

    def __exit__(self, type, value, traceback):
        curses.endwin()


def read_until(fd, delim):
    out = ""
    c = stdin.read(1)
    while c != delim:
        out += c
        c = stdin.read(1)
    return out


def xterm_pixels():
    code = "\x1b\x5b\x31\x34\x74\x0a"

    with raw_terminal(stdin):
        stdout.write(code)
        stdout.flush()

        c = stdin.read(1)
        assert c == '\x1b'
        read_until(stdin, ';')
        height = read_until(stdin, ';')
        width = read_until(stdin, 't')

    return (int(width), int(height))


if __name__ == '__main__':
    print("Height and width of the xterm terminal:")
    print(xterm_pixels())
    print(".")
