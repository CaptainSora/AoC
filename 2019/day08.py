def day08a():
    with open("2019/day08_input.txt", 'r') as f:
        imagedata = f.read().strip()
    
    width = 25
    height = 6
    layers = int(len(imagedata)/width/height)
    
    zerocount = float("inf")
    product = 0
    for i in range(layers):
        layer = imagedata[i*width*height:(i+1)*width*height]
        count0 = layer.count('0')
        if count0 < zerocount:
            zerocount = count0
            count1 = layer.count('1')
            count2 = layer.count('2')
            product = count1 * count2
    return product

def day08b():
    with open("2019/day08_input.txt", 'r') as f:
        imagedata = f.read().strip()
    
    width = 25
    height = 6
    
    output = ""
    for i in range(width*height):
        pixel = imagedata[i::width*height]
        for j in pixel:
            if j == '0':
                output += " "
                break
            elif j == "1":
                output += "#"
                break
        if i % width == width - 1:
            output += '\n'
        
    return output


print(day08a())
print(day08b())
            