#!/usr/bin/env python

"""Utility to find all twiki.cern.ch URLs in sources."""

import re
import subprocess

DEBUG = False


def main():
    """Main script doing the work."""
    found = []
    # find unique twiki.cern.ch URLs
    source = subprocess.getoutput("git grep twiki.cern.ch")
    for line in source.split("\n"):
        urls = re.findall(r'(https://twiki.cern.ch.*?)["\)\\]', line)
        if DEBUG:
            print("*" * 80)
            print("INPUT:", repr(line))
        for url in urls:
            if DEBUG:
                print("FOUND", repr(url))
            if url not in found:
                found.append(url)
    # print what was found
    for url in found:
        print(url)


if __name__ == "__main__":
    main()
