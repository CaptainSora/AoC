def str_cond(num):
    numstr = str(num)
    two_adj = False
    for i in range(5):
        if numstr[i] > numstr[i+1]:
            return False
        elif numstr[i] == numstr[i+1]:
            two_adj = True
    return two_adj

def day04a():
    lower = 246540
    upper = 787419
    counter = 0
    for i in range(lower+1, upper):
        if str_cond(i):
            counter += 1
    return counter

def str_cond2(num):
    numstr = str(num)
    adj = [1] * 10
    for i in range(5):
        if numstr[i] > numstr[i+1]:
            return False
        elif numstr[i] == numstr[i+1]:
            adj[int(numstr[i])] += 1
    return 2 in adj

def day04b():
    lower = 246540
    upper = 787419
    counter = 0
    for i in range(lower+1, upper):
        if str_cond2(i):
            counter += 1
    return counter

print(day04b())
