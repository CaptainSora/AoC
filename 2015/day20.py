from functools import reduce
from itertools import count
from math import sqrt


def sieve(size, floor=2):
    """
    Returns a list of all primes up to and including size.
    Much faster than primegen, and should be used when a ceiling is known.

    Optionally, excludes primes below floor.
    """
    size += 1
    is_prime = [True] * (size + 1)
    for i in range(2, int(sqrt(size)) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = [False] * len(is_prime[i*i::i])
    return [i for i in range(size+1) if is_prime[i] and i >= floor]


def prime_factors(num, mode="count"):
    """
    "count" : Returns the number of unique prime factors of num.
    "max"   : Returns the greatest prime factor of num.
    "min"   : Returns the smallest prime factor of num.
    "list"  : Returns a list of prime factors of num.
    "dict"  : Returns a dict of the prime factorization of num.
    "rad"   : Returns the product of the unique prime factors of num.

    e.g. input 43, test with primes [2, 3, 5], remainder [1, 1, 3]
    """
    pfactors = {}
    # Generate potential prime factors
    ppf_list = sieve(int(sqrt(num)))
    for x in ppf_list:
        if num % x == 0:
            pfactors[x] = 0
            while num % x == 0:
                pfactors[x] += 1
                num /= x
        if num == 1:
            break
    if num > 1:
        pfactors[num] = 1
    pflist = list(pfactors.keys())
    pflist.sort()
    # Output based on mode
    if mode == "count":
        return len(pflist)
    elif mode == "max":
        return pflist[-1]
    elif mode == "min":
        return pflist[0]
    elif mode == "list":
        return pflist
    elif mode == "dict":
        return pfactors
    elif mode == "rad":
        return prod(pflist)


def all_factors(num, mode="list"):
    """
    "list" : Returns a list of all proper divisors of num.
    "sum"  : Returns the sum of all proper divisors of num.
    """
    pfac_dict = prime_factors(num, mode="dict")
    pfac = [[x, pfac_dict[x]] for x in pfac_dict]
    pfac.sort(key=lambda x: x[0])
    fac_list = []
    pfac_cur = [[x[0], 0] for x in pfac]
    while pfac_cur != pfac:
        fac_list.append(int(reduce(lambda x, y: x * y[0]**y[1], pfac_cur, 1)))
        pfac_cur[0][1] += 1
        for i in range(len(pfac_cur)):
            if pfac_cur[i][1] > pfac[i][1]:
                pfac_cur[i][1] = 0
                pfac_cur[i+1][1] += 1
            else:
                break
    if mode == "list":
        return fac_list
    elif mode == "sum":
        return sum(fac_list)


# ================= IMPORTED FROM PROJECT EULER ==============================


def day20a():
	input = 29000000
	for i in count(1):
		if (all_factors(i, "sum") + i) * 10 >= input:
			return i

def day20b():
	input = 29000000
	for i in count(1):
		f = [fac for fac in all_factors(i, "list") if fac >= i / 50]
		if (sum(f) + i) * 11 >= input:
			return i

print(day20a())
print(day20b())
