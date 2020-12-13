from math import ceil

def day13a():
	with open("2020/day13_input.txt", "r") as f:
		dep_time, IDs = f.read().strip().split('\n')
	dep_time = int(dep_time)
	IDs = [int(id) for id in IDs.split(',') if id != "x"]
	times = []
	for id in IDs:
		times.append(id * ceil(dep_time/id))
	
	index = times.index(min(times))
	return IDs[index] * (times[index] - dep_time)


def day13b():
	with open("2020/day13_input.txt", "r") as f:
		IDs = f.read().strip().split('\n')[1]
	IDs = [int(id) if id != "x" else id for id in IDs.split(',')]
	dep_times = [[IDs[i], i] for i in range(len(IDs)) if IDs[i] != 'x']
	dep_times.sort(reverse = True)
	time = 0

	def satisfied(busid):
		return (time + busid[1]) % busid[0] == 0
	
	LCM = 1
	for bus in dep_times:
		while not satisfied(bus):
			time += LCM
		offset = LCM
		counter = 1
		while offset % bus[0] != 0:
			offset += LCM
			counter += 1
		LCM *= counter
	
	return time


print(day13b())
