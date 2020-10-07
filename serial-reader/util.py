#combines a bytestring to a single int. Little endian
def combineBytes(bytes):
    total = 0
    count = 0
    for v in bytes:
        total += v << (count * 8)
        count += 1
    return total

