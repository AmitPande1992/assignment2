l = [(2,5), (1,2), (4,4), (2,3), (2,1)]
first = len(l)
for i in range(0,first):
    for j in range (0, first-i-1):
        if(l[j][1]) > l[j+1][1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
print(l)