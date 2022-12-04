def day02a():
    with open("2018/day02_input.txt", 'r') as f:
        boxes = f.read().strip().split('\n')
    
    twocount = 0
    threecount = 0
    for label in boxes:
        counter = [0] * 26
        for letter in label:
            counter[ord(letter) - ord('a')] += 1
        if 2 in counter:
            twocount += 1
        if 3 in counter:
            threecount += 1
    return twocount * threecount

def day02b():
    with open("2018/day02_input.txt", 'r') as f:
        boxes = f.read().strip().split('\n')
    
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            diff = -1
            for k in range(len(boxes[i])):
                if boxes[i][k] != boxes[j][k]:
                    if diff < 0:
                        diff = k
                    else:
                        diff = -1
                        break
            if diff > 0:
                return ''.join([boxes[i][:diff], boxes[i][diff+1:]])


print(day02a())
print(day02b())
