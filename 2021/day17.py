def day17a():
	with open("2021/day17_input.txt", "r") as f:
		_, xstr, ystr = f.read().strip().replace(":", ",").split(", ")
	xpos = [int(num) for num in xstr[2:].split("..")]
	ypos = [int(num) for num in ystr[2:].split("..")]
	max_y_vel = abs(ypos[0]) - 1
	return (1 + max_y_vel) * max_y_vel // 2


def day17b():
	with open("2021/day17_input.txt", "r") as f:
		_, xstr, ystr = f.read().strip().replace(":", ",").split(", ")
	xpos = [int(num) for num in xstr[2:].split("..")]
	ypos = [int(num) for num in ystr[2:].split("..")]
	max_y_vel = abs(ypos[0]) - 1
	min_x_vel = 1
	while (min_x_vel + 1) * min_x_vel / 2 < xpos[0]:
		min_x_vel += 1
	
	def partial_sum(start, count):
		"""
		Returns the partial sum (start + (start - 1) + ...) over count terms.
		"""
		count = min(count, start)
		return (start + (start - count + 1)) * count // 2

	n_valid_vels = 0
	for y_vel in range(ypos[0], max_y_vel + 2):
		# Find the step number(s) for which yval is valid
		valid_steps = []
		y = 0
		step = 0
		if y_vel > 0:
			step += 2 * y_vel + 1
			y_vel *= -1
			y_vel -= 1
		while y >= ypos[0]:
			y += y_vel
			y_vel -= 1
			step += 1
			if ypos[0] <= y <= ypos[1]:
				valid_steps.append(step)
		if not valid_steps:
			continue
		# Search all x values from min_x_vel to xpos[1]
		for x in range(min_x_vel, xpos[1] + 1):
			n_valid_vels += int(any([
				xpos[0] <= partial_sum(x, s) <= xpos[1]
				for s in valid_steps
			]))
	return n_valid_vels


print(day17a())
print(day17b())
