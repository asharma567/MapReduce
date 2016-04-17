import sys
from ast import literal_eval
from collections import Counter

'''
find the pairwise intersection
'''

def find_n_grams(n, work_list):
    return zip(*[work_list[i:] for i in range(n)])

if __name__ == '__main__':
    master_list = []
    for line in sys.stdin:
        user, friends = line.split(' ', 1)
        x = literal_eval(friends)
    
        #chain all the lists together
        master_list.extend(x)
    
    #find all bigrams
    all_bigrams = find_n_grams(2, master_list)

    #print the count of all bigrams
    counted = Counter(all_bigrams)
    print counted


