import sys
from collections import Counter

if __name__ == '__main__':
    for line in sys.stdin:
        print dict(Counter(line.split())) 