class DataChunker:

    def __init__(self, chunk_size):
        self.chunk_size = chunk_size
        self.size = 0
        self.bulk_data = []

    def feed(self, data):
        ret = None
        # full chunk, send it and start new one
        if self.bulk_data and self.size >= self.chunk_size:
            ret = self.bulk_data
            self.bulk_data, self.size = [], 0
            pass
        self.bulk_data.append(data)
        self.size += 1
        return ret

    def flush(self):
        ret = None
        if self.bulk_data:
            ret = self.bulk_data
            self.bulk_data = []
        return ret

def chunk_data(data, chunk_size=2):
    chunker = DataChunker(chunk_size=chunk_size)
    for i in data:
        ret = chunker.feed(i)
        if ret:
            yield ret
    ret = chunker.flush()
    if ret:
        yield ret

# Test
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
for n in range(1, 11):
    print(f"Chunk size:{n} |", *(i for i in chunk_data(d, n)))

# Method 2 (yield data not supported)
def chunk_data2(iterable, chunk_size=500):
    return list(iterable[j:j + chunk_size]
    for j in range(0, len(iterable), chunk_size))
