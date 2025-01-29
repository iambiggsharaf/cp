def can_be_sorted_to_abc(s):
    # Check if the string is either 'bca' or 'cab'
    if s == 'bca' or s == 'cab':
        return "NO"
    else:
        return "YES"

# Read number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    s = input().strip()
    result = can_be_sorted_to_abc(s)
    print(result)
