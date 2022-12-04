from itertools import permutations


def day21a():
	with open("2020/day21_input.txt", "r") as f:
		ingrlist = [row.split(' (contains ')
			for row in f.read().strip().split('\n')]
	all_ingr = set()
	all_agn = set()
	for i in range(len(ingrlist)):
		ingr, agn = ingrlist[i]
		ingrlist[i] = [ingr.split(' '), agn[:-1].split(', ')]
		for n in ingrlist[i][0]:
			all_ingr.add(n)
		for g in ingrlist[i][1]:
			all_agn.add(g)

	all_ingr = list(all_ingr)
	all_agn = list(all_agn)

	print(len(all_ingr), len(all_agn))
	agn_dict = {}
	for ingr, agn in ingrlist:
		for a in agn:
			if a not in agn_dict:
				agn_dict[a] = set(ingr)
			else:
				agn_dict[a].intersection_update(ingr)
	agn_list = list(set([a for sub in agn_dict.values() for a in sub]))
			
	counter = 0
	for ingr, _ in ingrlist:
		counter += len([i for i in ingr if i not in agn_list])

	return counter


def day21b():
	with open("2020/day21_input.txt", "r") as f:
		ingrlist = [row.split(' (contains ')
			for row in f.read().strip().split('\n')]
	all_ingr = set()
	all_agn = set()
	for i in range(len(ingrlist)):
		ingr, agn = ingrlist[i]
		ingrlist[i] = [ingr.split(' '), agn[:-1].split(', ')]
		for n in ingrlist[i][0]:
			all_ingr.add(n)
		for g in ingrlist[i][1]:
			all_agn.add(g)

	all_ingr = list(all_ingr)
	all_agn = list(all_agn)

	num_agn = len(all_agn)
	agn_dict = {}
	for ingr, agn in ingrlist:
		for a in agn:
			if a not in agn_dict:
				agn_dict[a] = set(ingr)
			else:
				agn_dict[a].intersection_update(ingr)
	raw_agn_list = [[k, list(v)] for k, v in agn_dict.items()]

	agn_list = {}
	while len(agn_list) < num_agn:
		for i in range(len(raw_agn_list)):
			a = raw_agn_list[i][0]
			b = raw_agn_list[i][1]
			if len(b) == 1:
				if a not in agn_list.keys():
					agn_list[a] = b[0]
					for j in range(len(raw_agn_list)):
						if j == i:
							continue
						if b[0] in raw_agn_list[j][1]:
							raw_agn_list[j][1].remove(b[0])
	agn_list = [[k, v] for k, v in agn_list.items()]
	agn_list.sort()
	return ','.join([item[1] for item in agn_list])

print(day21b())
