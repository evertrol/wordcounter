from __future__ import print_function

import sys
import re
from collections import Counter


def countwords(filename):
    with open(filename) as fh:
        text = fh.read()
    words = re.findall('\w+', text)
    counter = Counter(words)
    return counter.most_common(10)


most_common = countwords(sys.argv[1])
for word, n in most_common:
    print(word, ':', n, 'times')
