from collections import deque
from json import loads


def day12a():
	with open("2015/day12_input.txt", "r") as f:
		q = deque(loads(f.read()))
	total = 0
	while q:
		item = q.popleft()
		if type(item) == list:
			q.extend(item)
		elif type(item) == dict:
			q.extend(item.values())
		elif type(item) == int:
			total += item
	return total

def day12b():
	with open("2015/day12_input.txt", "r") as f:
		q = deque(loads(f.read()))
	total = 0
	while q:
		item = q.popleft()
		if type(item) == list:
			q.extend(item)
		elif type(item) == dict:
			if "red" not in item and "red" not in item.values():
				q.extend(item.values())
		elif type(item) == int:
			total += item
	return total


print(day12a())
print(day12b())
