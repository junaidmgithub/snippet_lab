
def recursive_sum(l, s=0):
    l1, l2 = l[:1], l[1:]
    s += l1[0]
    if l2:
        s = recursive_sum(l2, s)
    return s

l = [1,2,3,4]

result = recursive_sum(l)

print(result)
