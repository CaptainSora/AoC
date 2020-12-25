def solve():
    with open("Reaktor/01_tattoo.txt", 'r') as f:
        data = [[int(stream[i:i+8], 2) for i in range(0, len(stream), 8)]
            for stream in f.read().strip().split('\n')]
    password = ''
    for stream in data:
        cur = 0
        while stream[cur] >= len(stream):
            cur += 1
        while stream[cur] < len(stream):
            cur = stream[cur]
        password += chr(stream[cur])
    return password

print(solve())