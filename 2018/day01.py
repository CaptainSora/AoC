def day01a():
    with open("2018/day01_input.txt", 'r') as f:
        return sum([int(num) for num in f.read().strip().split('\n')])

def day01b():
    with open("2018/day01_input.txt", 'r') as f:
        freqs = [int(num) for num in f.read().strip().split('\n')]
    
    pos = 0
    freqlist = set([0])
    prev = 0
    while True:
        newfreq = prev + freqs[pos]
        if newfreq in freqlist:
            return newfreq
        freqlist.add(newfreq)
        prev = newfreq
        pos += 1
        if pos >= len(freqs):
            pos = 0


print(day01a())
print(day01b())
