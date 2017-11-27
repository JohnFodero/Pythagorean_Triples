import argparse

def fib(n):
    assert n >= 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    args = parser.parse_args()

    print('fib({}) is {}'.format(args.n, fib(args.n)))
