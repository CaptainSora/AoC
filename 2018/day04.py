def day04a():
    with open("2018/day04_input.txt", 'r') as f:
        record = [
            row.strip().replace('[', '').replace(']', '').split(' ')
            for row in sorted(f.read().strip().split('\n'))
        ]
    
    sleepdict = {}
    cur_guard = ''
    sleepstart = -1
    for row in record:
        if len(row) == 6:
            cur_guard = row[3]
            if cur_guard not in sleepdict:
                sleepdict[cur_guard] = [0] * 60
        elif row[2] == 'falls':
            sleepstart = int(row[1].split(':')[1])
        elif row[2] == 'wakes':
            sleepend = int(row[1].split(':')[1])
            for i in range(sleepstart, sleepend):
                sleepdict[cur_guard][i] += 1
    sleepyguard = ''
    maxsleep = []
    for k, v in sleepdict.items():
        if sum(v) > sum(maxsleep):
            sleepyguard = k
            maxsleep = v
    return int(sleepyguard[1:]) * maxsleep.index(max(maxsleep))

def day04b():
    with open("2018/day04_input.txt", 'r') as f:
        record = [
            row.strip().replace('[', '').replace(']', '').split(' ')
            for row in sorted(f.read().strip().split('\n'))
        ]
    
    sleepdict = {}
    cur_guard = ''
    sleepstart = -1
    for row in record:
        if len(row) == 6:
            cur_guard = row[3]
            if cur_guard not in sleepdict:
                sleepdict[cur_guard] = [0] * 60
        elif row[2] == 'falls':
            sleepstart = int(row[1].split(':')[1])
        elif row[2] == 'wakes':
            sleepend = int(row[1].split(':')[1])
            for i in range(sleepstart, sleepend):
                sleepdict[cur_guard][i] += 1
    sleepyguard = ''
    maxsleep = [0]
    for k, v in sleepdict.items():
        if max(v) > max(maxsleep):
            sleepyguard = k
            maxsleep = v
    return int(sleepyguard[1:]) * maxsleep.index(max(maxsleep))

print(day04b())