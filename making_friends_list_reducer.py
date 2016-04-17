import sys
from collections import defaultdict
from ast import literal_eval


if __name__ == '__main__':
    out_list = []
    dic = defaultdict(list)
    for line in sys.stdin:
        user, friend_connection = literal_eval(line)
        dic[user].append(friend_connection)

    #print each key s.t. user [friends]
    for user, friends_list in dic.iteritems():
        print user, friends_list

