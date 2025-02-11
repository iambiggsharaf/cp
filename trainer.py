def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        # Считываем силы спортсменов и сортируем их
        strengths = list(map(int, input_data[index:index+n]))
        index += n
        strengths.sort()
        
        # Ищем минимальную разницу между соседними элементами
        min_diff = float('inf')
        for i in range(1, n):
            diff = strengths[i] - strengths[i - 1]
            if diff < min_diff:
                min_diff = diff
        
        results.append(str(min_diff))
    
    sys.stdout.write("\n".join(results))
    
if __name__ == "__main__":
    solve()
