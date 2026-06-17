def decompress_rle(data):
    result = ""
    i = 0

    while i < len(data):
        char = data[i]
        i += 1

        count = ""
        while i < len(data) and data[i].isdigit():
            count += data[i]
            i += 1

        result += char * int(count)

    return result


compressed = "A4B3C2D1A2"

print("Decompressed:", decompress_rle(compressed))
