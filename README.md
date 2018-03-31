A wordcounter example package

Simple demonstration package that counts word frequencies in a file.
It is used to show how to execute a Python package.

# Installation

    python setup.py install


# Usage

    python -m wordcounter [-n TOP_N] <filename>


For example:

    python -m wordcounter -n5 README.md

times : 6 times
wordcounter : 5 times
package : 4 times
python : 4 times
example : 3 times


# Details

For details, see https://evertrol.github.io/posts/make-your-python-packages-executable/ .
