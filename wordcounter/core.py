import re
from collections import Counter


__all__ = ['countwords']


def countwords(filename, topn=10):
    with open(filename) as fh:
        text = fh.read()
    words = re.findall('\w+', text)
    counter = Counter(words)
    return counter.most_common(topn)
