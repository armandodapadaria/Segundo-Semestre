from __future__ import print_function, division

import random

def has_duplicates(t):
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()

    #check for adjacent elements that are equal
    for i in range(len(s)-1):
        if s[i] == s [s+i]:
            return True
    return False

def random_bdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t

def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):
        return True

def main ():
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)
    
if __name__ == '__main__':
    main()