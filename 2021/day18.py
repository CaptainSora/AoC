from itertools import permutations


class SnailNum:
	def __init__(self, numstr="[0,0]"):
		# Find middle comma
		open_bkt = 0
		for i in range(len(numstr)):
			if numstr[i] == "[":
				open_bkt += 1
			elif numstr[i] == "]":
				open_bkt -= 1
			elif open_bkt == 1 and numstr[i] == ",":
				delim = i
				break
		# Assign left and right halves recursively
		lstr, rstr = numstr[1:delim], numstr[delim+1:-1]
		if lstr.isdecimal():
			self.left = int(lstr)
		else:
			self.left = SnailNum(lstr)
		if rstr.isdecimal():
			self.right = int(rstr)
		else:
			self.right = SnailNum(rstr)
	
	def __str__(self):
		return f"SN[{str(self.left)}, {str(self.right)}]"
	
	def add(self, other):
		"""
		Returns a new SnailNum as self + other, with self as the left
		child and other as the right child.
		"""
		parent = SnailNum()
		parent.left = self
		parent.right = other
		return parent
	
	def push_left(self, num):
		if isinstance(self.left, int):
			self.left += num
		else:
			self.left.push_left(num)
	
	def push_right(self, num):
		if isinstance(self.right, int):
			self.right += num
		else:
			self.right.push_right(num)
	
	def reduce(self):
		"""
		Reduces the SnailNum in-place.
		Returns the SnailNum for efficient chaining.
		"""
		while self.explode(1) or self.split():
			continue
		return self

	def explode(self, depth):
		"""
		Searches for and explodes the first applicable pair.
		Three-element return: Explode result (left, right, None)
		Two-element return: Propagate upwards (num, left?)
		One-element return: Propagation complete, exit
		No-element return: No explode
		"""
		if depth > 4:
			return (self.left, self.right, None)
		debris = tuple()
		# Check left child
		if isinstance(self.left, SnailNum):
			debris = self.left.explode(depth + 1)
			if len(debris) == 3:
				# Set left child to zero
				self.left = 0
				# Push the second element
				if isinstance(self.right, int):
					self.right += debris[1]
				else:
					self.right.push_left(debris[1])
				# Raise the first element
				return [debris[0], True]
			elif len(debris) == 2:
				# First element, looking to head left
				if debris[1]:
					return debris
				else:
					# Second element, headed nearest right
					if isinstance(self.right, int):
						self.right += debris[0]
					else:
						self.right.push_left(debris[0])
					return [True]
			elif len(debris) == 1:
				return debris
		# Check right child
		if not debris and isinstance(self.right, SnailNum):
			debris = self.right.explode(depth + 1)
			if len(debris) == 3:
				# Set right child to zero
				self.right = 0
				# Push the first element
				if isinstance(self.left, int):
					self.left += debris[0]
				else:
					self.left.push_right(debris[0])
				# Raise the second element
				return [debris[1], False]
			elif len(debris) == 2:
				# Second element, looking to head right
				if not debris[1]:
					return debris
				else:
					# First element, headed nearest left
					if isinstance(self.left, int):
						self.left += debris[0]
					else:
						self.left.push_right(debris[0])
					return [True]
			elif len(debris) == 1:
				return debris
		# Nothing exploded
		return debris

	def split(self):
		"""
		Searches for and splits the first applicable number.
		"""
		# Check left child recursively
		if isinstance(self.left, int):
			if self.left >= 10:
				x = self.left // 2
				y = self.left - x
				self.left = SnailNum(f"[{x},{y}]")
				return True
		else:
			if self.left.split():
				return True
		# Check right child
		if isinstance(self.right, int):
			if self.right >= 10:
				x = self.right // 2
				y = self.right - x
				self.right = SnailNum(f"[{x},{y}]")
				return True
		else:
			return self.right.split()
		# Nothing happened
		return False
	
	def magnitude(self):
		lmag = self.left
		rmag = self.right
		if isinstance(self.left, SnailNum):
			lmag = self.left.magnitude()
		if isinstance(self.right, SnailNum):
			rmag = self.right.magnitude()
		return 3 * lmag + 2 * rmag


def day18a():
	with open("2021/day18_input.txt", "r") as f:
		homework = f.read().strip().split("\n")
	sn = SnailNum(homework[0])
	for line in homework[1:]:
		sn = sn.add(SnailNum(line)).reduce()
	return sn.magnitude()
	

def day18b():
	with open("2021/day18_input.txt", "r") as f:
		homework = f.read().strip().split("\n")
	return max([
		SnailNum(l1).add(SnailNum(l2)).reduce().magnitude()
		for l1, l2 in permutations(homework, r=2)
	])


print(day18a())
print(day18b())
