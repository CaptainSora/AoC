def day14a():
	with open("2015/day14_input.txt", "r") as f:
		reindeer = [line.split() for line in f.read().strip().split("\n")]
	# Indices: 3, 6, 13
	def dist(rdeer):
		speed, t1, t2 = int(rdeer[3]), int(rdeer[6]), int(rdeer[13])
		q, r = divmod(2503, t1+t2)
		return q * t1 * speed + min(r, t1) * speed
	
	return max([dist(rdeer) for rdeer in reindeer])

def day14b():
	with open("2015/day14_input.txt", "r") as f:
		reindeer = [line.split() for line in f.read().strip().split("\n")]
	reindeer = [
		[int(rdeer[3]), int(rdeer[6]), int(rdeer[13])]
		for rdeer in reindeer
	]
	points = [0 for _ in reindeer]
	dist = [0 for _ in reindeer]
	for t in range(2503):
		for i in range(len(reindeer)):
			speed, t1, t2 = reindeer[i]
			if t % (t1 + t2) < t1:
				dist[i] += speed
		points = [
			points[i] + (dist[i] == max(dist))
			for i in range(len(reindeer))
		]
	return max(points)


print(day14a())
print(day14b())
