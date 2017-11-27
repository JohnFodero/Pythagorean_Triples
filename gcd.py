import argparse

def gcd(a, b):
    remainder = a % b
    if remainder != 0:
        return gcd(b, remainder)
    return b
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    args = parser.parse_args()

    print('GCD of {} and {} is {}'.format(args.a, args.b, gcd(args.a, args.b)))
