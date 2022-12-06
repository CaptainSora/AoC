from hashlib import md5
from itertools import count


def day04a():
	input = "iwrupvqb"
	for i in count(1):
		if md5((input + str(i)).encode("utf-8")).hexdigest()[:5] == "00000":
			return i


def day04b():
	input = "iwrupvqb"
	for i in count(1):
		if md5((input + str(i)).encode("utf-8")).hexdigest()[:6] == "000000":
			return i


print(day04a())
print(day04b())
