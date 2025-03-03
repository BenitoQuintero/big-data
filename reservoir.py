import argparse
from random import randrange
from random import shuffle
import unittest
import sys

def rsample(stream, size=10):
    """
    Produce a simple random sample with `size` elements from `stream`
    using reservoir sampling, without collecting stream into memory
    """
    reservoir = []
    for num_observations,item in enumerate(stream):
        if num_observations >= size:
            rand_num = randrange(num_observations)
            if rand_num < size:
                reservoir[rand_num] = item
        else:
            reservoir.append(item)
            if num_observations == size-1:
                shuffle(reservoir)
    if len(reservoir) < size:
        shuffle(reservoir)
    return reservoir

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--sample-size", help = "Size of the sample to be taken")
    args = parser.parse_args()

    if sys.stdin.isatty():
        print("Error: No input from stdin")
        exit(1)

    if args.sample_size:
        res = rsample(sys.stdin,int(args.sample_size))
    else:
        res = rsample(sys.stdin)

    for item in res: sys.stdout.write(item)


class rsampleTest(unittest.TestCase):
    
    def test_defaults(self):
        g = (i**2 for i in range(20))
        s = rsample(g)
        self.assertEqual(len(s), 10)
        
    def test_too_small_input(self):
        d = range(5)
        s = rsample(d)
        self.assertEqual(set(s), set(d))

    def test_string(self):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        s = rsample(letters, 26)
        self.assertEqual(set(s), set(letters))

    #-------------------------------------------------------------
    # Following tests *should* pass with high probability ;)
    #-------------------------------------------------------------

    def test_permutation(self):
        n = 100
        d = range(n)
        s = rsample(d, n)
        self.assertEqual(len(s), n)
        self.assertNotEqual(s, list(d))

    def test_not_begin(self):
        n = int(1e6)
        d = range(n)
        s = rsample(d)
        self.assertTrue(1000 < max(s))

    def test_not_end(self):
        n = int(1e6)
        d = range(n)
        s = rsample(d)
        self.assertTrue(min(s) < (n - 1000))
