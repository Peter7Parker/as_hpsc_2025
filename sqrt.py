def sqrt2(x):
    s = 1.
    kmax = 100
    tol = 1.0e-14
    for i in range(kmax):
        s0 = s
        print(f'At itertion {i} the value of s = {s:20.15f}')
        s = 0.5*(s + x/s)
        delta_s = s -s0
        if (abs(delta_s)/x < tol):
           break

    print(f"Finally, the value of s = {s:20.15f}")

    
