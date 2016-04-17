import sys


if __name__ == '__main__':
    for line in sys.stdin:
        user, friend = line.strip().split()
        print (user, friend)

