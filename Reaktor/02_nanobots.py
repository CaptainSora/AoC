def solve():
    with open('Reaktor/02_nanobots.txt', 'r') as f:
        signal = f.read().strip()
    basevalue = ''
    freqtable = [0] * 128
    for char in signal:
        freqtable[ord(char)] += 1
    basevalue += chr(freqtable.index(max(freqtable)))
    while basevalue[-1] != ';':
        freqtable = [0] * 128
        for i in range(len(signal) - 1):
            if signal[i] == basevalue[-1]:
                freqtable[ord(signal[i+1])] += 1
        basevalue += chr(freqtable.index(max(freqtable)))
    return basevalue[:-1]

print(solve())