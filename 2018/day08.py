def day08a():
	with open("2018/day08_input.txt", "r") as f:
		data = [int(num) for num in f.read().strip().split(' ')]
	
	metadata = 0

	def node(pos):
		nonlocal metadata
		# returns the length of the node
		child_qty = data[pos]
		meta_qty = data[pos+1]
		child_pos = pos + 2
		for _ in range(child_qty):
			child_pos += node(child_pos)
		for i in range(meta_qty):
			metadata += data[child_pos + i]
		return child_pos - pos + meta_qty
	
	node(0)
	return metadata

def day08b():
	with open("2018/day08_input.txt", "r") as f:
		data = [int(num) for num in f.read().strip().split(' ')]
	
	def node(pos):
		# returns the length of the node and its value
		child_qty = data[pos]
		meta_qty = data[pos+1]
		child_pos = pos + 2
		value = 0
		child_values = [0 for _ in range(child_qty)]
		for i in range(child_qty):
			retval = node(child_pos)
			child_pos += retval[0]
			child_values[i] = retval[1]
		for j in range(meta_qty):
			meta_index = data[child_pos + j]
			if child_qty > 0:
				if meta_index > child_qty:
					continue
				value += child_values[meta_index - 1]
			else:
				value += meta_index
		return [child_pos - pos + meta_qty, value]
	
	return node(0)[1]

print(day08b())
