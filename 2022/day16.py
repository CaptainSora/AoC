from collections import deque, namedtuple
from copy import copy


def day16a():
	with open("2022/day16_input.txt", "r") as f:
		volcano = f.read().replace(";", "").replace("=", " ") \
			.replace(",", "").strip().split("\n")
	valves = {}
	tunnels = {}
	for line in volcano:
		line = line.split()
		room, rate = line[1], int(line[5])
		if rate > 0:
			valves[room] = rate
		tunnels[room] = line[10:]

	State = namedtuple(
		'State',
		['room', 'time', 'released', 'flow', 'open', 'hist']
	)
	q = deque([State('AA', 0, 0, 0, [], {})])
	max_p = 0

	while q:
		state = q.popleft()
		# End condition
		if state.time == 30:
			max_p = max(max_p, state.released)
			continue
		# Add to room_best and prune
		if state.room not in state.hist or state.hist[state.room] < state.flow:
			state.hist[state.room] = state.flow
		else:
			continue
		# Create children for each action
		if state.room in valves and state.room not in state.open:
			q.append(State(
				state.room, state.time + 1, state.released + state.flow,
				state.flow + valves[state.room], state.open + [state.room],
				state.hist
			))
		for other in tunnels[state.room]:
			q.append(State(
				other, state.time + 1, state.released + state.flow,
				state.flow, state.open, state.hist
			))
	return max_p


def day16b():
	with open("2022/day16_input.txt", "r") as f:
		volcano = f.read().replace(";", "").replace("=", " ") \
			.replace(",", "").strip().split("\n")
	valves = {}
	tunnels = {}
	for line in volcano:
		line = line.split()
		room, rate = line[1], int(line[5])
		tunnels[room] = line[10:]
		if rate > 0:
			valves[room] = rate
			tunnels[room].append(room) # Stay in the room
	nvalves = len(valves)
	
	State = namedtuple(
		'State',
		['room', 'eroom', 'time', 'released', 'flow', 'open',
		'hist', 'ehist', 'phist']
	)
	q = deque([State('AA', 'AA', 0, 0, 0, [], {}, {}, [])])
	max_p = 0
	
	while q:
		state = q.popleft()
		# End conditions
		if state.time == 26:
			max_p = max(max_p, state.released)
			continue
		elif len(state.open) == nvalves:
			# All valves open
			remain = (26 - state.time) * state.flow
			max_p = max(max_p, state.released + remain)
			if state.released + remain == max_p:
				print(state.released + remain, state.phist + [state.flow], "Done")
			continue
		# Add to room_best and prune
		newbest = False
		if state.room not in state.hist or state.hist[state.room] < state.flow:
			state.hist[state.room] = state.flow
			newbest = True
		if state.eroom not in state.ehist or state.ehist[state.eroom] < state.flow:
			state.ehist[state.room] = state.flow
			newbest = True
		if not newbest:
			remain = (26 - state.time) * state.flow
			max_p = max(max_p, state.released + remain)
			if state.released + remain == max_p:
				print(state.released + remain, state.phist)
			continue
		# Create children for each action
		for next in tunnels[state.room]:
			if next == state.room and next in state.open:
				continue
			for enext in tunnels[state.eroom]:
				if enext == state.eroom and enext in state.open:
					continue
				if next == state.room == enext == state.eroom:
					continue
				newflow = valves[state.room] if next == state.room else 0
				neweflow = valves[state.eroom] if enext == state.eroom else 0
				newopen = [state.room] if next == state.room else []
				neweopen = [state.eroom] if enext == state.eroom else []
				q.append(State(
					next, enext, state.time + 1, state.released + state.flow,
					state.flow + newflow + neweflow,
					state.open + newopen + neweopen, copy(state.hist), copy(state.ehist),
					state.phist + [state.flow]
				))

		# if state.room in valves and state.room not in state.open:
		# 	q.append(State(
		# 		state.room, state.time + 1, state.released + state.flow,
		# 		state.flow + valves[state.room], state.open + [state.room],
		# 		state.hist
		# 	))
		# for other in tunnels[state.room]:
		# 	q.append(State(
		# 		other, state.time + 1, state.released + state.flow,
		# 		state.flow, state.open, state.hist
		# 	))
	return max_p


print(day16a())
print(day16b())
