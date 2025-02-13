def max_points(n, numbers):
    # Подсчитываем количество чётных и нечётных чисел
    count_even = sum(1 for x in numbers if x % 2 == 0)
    count_odd = n - count_even

    # Если есть хотя бы одно чётное число, то выгодно использовать его на первой операции
    if count_even > 0:
        return 1 + count_odd  # 1 балл за чётное на первом шаге + баллы за каждое нечётное число после
    else:
        # Если чётных нет, то первая операция (с нечётным) не даёт балл, а каждая последующая — даёт
        return max(0, count_odd - 1)

def main():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        numbers = list(map(int, input_data[index:index+n]))
        index += n
        results.append(str(max_points(n, numbers)))
    
    print("\n".join(results))

if __name__ == '__main__':
    main()
