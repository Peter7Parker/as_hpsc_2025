x = 2
s = 1.
kmax = 10
for i in range(kmax):
    print(f'At itertion {i} the value of s = {s}')
    s = 0.5*(s + x/s)
    
print(s)
    
    
