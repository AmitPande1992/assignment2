Dict = {}
keys = range(97,123)
values = []
alpha = 'a'
for i in range(0, 26):
    values.append(alpha)
    alpha = chr(ord(alpha) + 1) 
    Dict[i] = values[i]
print(Dict)
