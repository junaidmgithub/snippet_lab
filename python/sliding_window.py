def sliding_window2(iterable, batch_size=2):
    # Overlapped
    return list(iterable[i:i+batch_size]
    for i in range(len(iterable)-batch_size+1))

def sliding_window3(iterable, batch_size=2):
    # Non-Overlapped
    return list(iterable[i:i + batch_size]
    for i in range(0, len(iterable) - batch_size + 1, batch_size))

# Test
l = [1,2,3,4,5,6,7,8,9,0]
for i, item in enumerate(sliding_window3(l)):
    print(i, list(item))
