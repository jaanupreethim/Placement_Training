def compress_rle(text):
    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    compressed += text[-1] + str(count)
    return compressed


data = "AAAABBBCCDAA"
compressed = compress_rle(data)

print("Original:", data)
print("Compressed:", compressed)
