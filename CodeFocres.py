def decode_borze(code):
    decoded = []
    i = 0
    while i < len(code):
        if code[i] == '.':
            decoded.append('0')
            i += 1
        elif code[i] == '-':
            if i + 1 < len(code) and code[i + 1] == '.':
                decoded.append('1')
                i += 2
            elif i + 1 < len(code) and code[i + 1] == '-':
                decoded.append('2')
                i += 2
    return ''.join(decoded)

# Пример использования:
borze_code = input().strip()
print(decode_borze(borze_code))
