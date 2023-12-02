from math import prod


def day16a():
	with open("2021/day16_input.txt", "r") as f:
		bincode = f"{int(f.read().strip(), 16):0>b}"
	version_total = 0

	def read_packets(bitstr):
		nonlocal version_total
		version, type_id, rest = bitstr[:3], bitstr[3:6], bitstr[6:]
		version_total += int(version, 2)
		if type_id == "100":
			value = ""
			while True:
				pref, num, rest = rest[0], rest[1:5], rest[5:]
				value += num
				if pref == "0":
					break
			return rest
		# Else, operator
		ltype, rest = rest[0], rest[1:]
		if ltype == "0":
			bitlen, rest = rest[:15], rest[15:]
			bitlen = int(bitlen, 2)
			child_bits, rest = rest[:bitlen], rest[bitlen:]
			while child_bits:
				child_bits = read_packets(child_bits)
		else:
			npacks, rest = rest[:11], rest[11:]
			npacks = int(npacks, 2)
			for _ in range(npacks):
				rest = read_packets(rest)
		# Return packet
		return rest
	
	read_packets(bincode)
	return version_total

def day16b():
	with open("2021/day16_input.txt", "r") as f:
		bincode = f"{int(f.read().strip(), 16):0>b}"

	def read_packets(bitstr):
		version, type_id, rest = bitstr[:3], bitstr[3:6], bitstr[6:]
		if type_id == "100":
			value = ""
			while True:
				pref, num, rest = rest[0], rest[1:5], rest[5:]
				value += num
				if pref == "0":
					break
			return int(value, 2), rest
		# Else, operator
		ltype, rest = rest[0], rest[1:]
		children = []
		if ltype == "0":
			bitlen, rest = rest[:15], rest[15:]
			bitlen = int(bitlen, 2)
			child_bits, rest = rest[:bitlen], rest[bitlen:]
			while child_bits:
				child, child_bits = read_packets(child_bits)
				children.append(child)
		else:
			npacks, rest = rest[:11], rest[11:]
			npacks = int(npacks, 2)
			for _ in range(npacks):
				child, rest = read_packets(rest)
				children.append(child)
		# Handle operation
		if type_id == "000":
			return sum(children), rest
		elif type_id == "001":
			return prod(children), rest
		elif type_id == "010":
			return min(children), rest
		elif type_id == "011":
			return max(children), rest
		elif type_id == "101":
			return int(children[0] > children[1]), rest
		elif type_id == "110":
			return int(children[0] < children[1]), rest
		elif type_id == "111":
			return int(children[0] == children[1]), rest
	
	return read_packets(bincode)[0]


print(day16a())
print(day16b())
