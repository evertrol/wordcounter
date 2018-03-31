from __future__ import print_function

import sys
import re
from collections import Counter
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Count length of filenames")
    parser.add_argument('filename', help="Input files")
    parser.add_argument('-n', '--top-n', type=int, default=10,
                        help="List top `n`")
    args = parser.parse_args()
    return args


def countwords(filename, topn=10):
    with open(filename) as fh:
        text = fh.read()
    words = re.findall('\w+', text)
    counter = Counter(words)
    return counter.most_common(topn)


def main():
    args = parse_args()
    most_common = countwords(args.filename, args.top_n)
    for word, n in most_common:
        print(word, ':', n, 'times')


if __name__ == "__main__":
    main()
