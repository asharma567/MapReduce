import sys
from collections import defaultdict


if __name__ == '__main__':
    matches = defaultdict(list)
    for line in sys.stdin:
        user, friend = line.strip().split()
    
        matches[user].append(friend)

    print matches