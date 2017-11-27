from gcd import gcd
from fib import fib
import argparse
from time import time

def euclid(n_triples):
    i = 0
    m = 2
    e_list = []
    while i < n_triples:
        for n in range(1,m):
            if gcd(m,n) == 1:
                e_list.append(tuple(sorted([m*m - n*n, 2*m*n, m*m + n*n])))
                i += 1
        m += 1
    return e_list

def fibonacci(n_triples):
    i = 0
    k = 3
    e_list = []
    while i < n_triples:
        if (k**(1/2)) % 1 == 0:
            n = (k+1)/2
            e_list.append((int(k**(1/2)), int(n-1), int(n)))
            i += 1
        k += 2
    return e_list

def sequence(n_triples):
    n = 4
    e_list = [(4, 3, 5)]
    while len(e_list) < n_triples:
        a = e_list[-1][0] + e_list[-1][1] + e_list[-1][2]
        b = fib((2*n)-1) - e_list[-1][1]
        c = fib(2*n)
        e_list.append((a,b,c))
        n += 1
    return e_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    args = parser.parse_args()
    n = args.n
    print('\n')
    st_time = time()
    eu = euclid(n_triples=n)
    print('euclid({}) is {} \n--completed in {} seconds\n'.format(n, eu, round(time()-st_time, 5)))
    st_time = time()
    fi = fibonacci(n_triples=n)
    print('fibonacci({}) is {} \n--completed in {} seconds\n'.format(n, fi, round(time()-st_time, 5)))
    st_time = time()
    se = sequence(n_triples=n)
    print('sequence({}) is {} \n--completed in {} seconds\n'.format(n, se, round(time()-st_time, 5)))
