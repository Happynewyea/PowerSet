import math





p = 10
comb = math.comb

lis = []
for i in range(p + 1):
    lis.append(comb(p, i))

primelist = []

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
            yield [ss for mask, ss in zip(masks, s) if i & mask]
    
sil = list(powerset(lis))
sil.remove([])
ils = []
for i in range(len(sil)):
    ils.append(sum(sil[i]))

print(ils)

