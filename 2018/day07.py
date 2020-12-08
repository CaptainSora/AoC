def day07a():
	with open("2018/day07_input.txt", "r") as f:
		order = [[row[5], row[36]] for row in f.read().strip().split('\n')]
	
	all_steps = set([step for instr in order for step in instr])
	build_order = ""
	incomplete = all_steps.copy()
	while len(build_order) < len(all_steps):
		not_ready = set([instr[1] for instr in order])
		ready = sorted(list(incomplete - not_ready))[0]
		build_order += ready
		incomplete.remove(ready)
		order = [instr for instr in order if instr[0] != ready]
	return build_order

def day07b():
	with open("2018/day07_input.txt", "r") as f:
		order = [[row[5], row[36]] for row in f.read().strip().split('\n')]
	
	all_steps = set([step for instr in order for step in instr])
	build_order = ""
	incomplete = all_steps.copy()
	workers = [["", -1] for _ in range(5)]
	time = 0

	def occupied():
		nonlocal workers
		for i in range(5):
			if workers[i][0] == "":
				return i
		return -1

	def update_workers():
		nonlocal order, build_order, time, workers
		time += 1
		for i in range(5):
			if workers[i][1] > 0:
				workers[i][1] -= 1
			if workers[i][1] == 0:
				build_order += workers[i][0]
				order = [instr for instr in order if instr[0] != workers[i][0]]
				workers[i] = ["", -1]
	
	def get_next():
		# Returns the character which is next up
		nonlocal incomplete, order
		not_ready = set([instr[1] for instr in order])
		ready = sorted(list(incomplete - not_ready))
		if len(ready) == 0:
			return None
		incomplete.remove(ready[0])
		return ready[0]
	
	while len(build_order) < len(all_steps):
		# Get next project details, waiting for project completion
		next_proj = get_next()
		while next_proj is None:
			if len(build_order) == len(all_steps):
				return time
			update_workers()
			next_proj = get_next()
		proj_dur = ord(next_proj) - ord('@') + 60
		# Wait for first free worker
		worker_index = occupied()
		while worker_index < 0:
			update_workers()
			worker_index = occupied()
		# Assign task to worker
		workers[worker_index] = [next_proj, proj_dur]
	return time

print(day07b())
