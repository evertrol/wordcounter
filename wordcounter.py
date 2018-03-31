from __future__ import print_function

import sys
import re
from collections import Counter


with open(sys.argv[1]) as fh:
    text = fh.read()
words = re.findall('\w+', text)
counter = Counter(words)
for word, n in counter.most_common(10):
    print(word, ':', n, 'times')