H, *P = input().split()
P = P[0] if len(P) > 0 else ''
print(2**(int(H)+1) - 2**len(P) - (int(P.replace('L','0').replace('R','1'),2) if len(P) > 0 else 0))
