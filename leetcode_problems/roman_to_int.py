def romanToInt(s: str) -> int:
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    n = len(s)
    for i in range(n):
        if i < n - 1 and mapping[s[i]] < mapping[s[i+1]]:
            sum -= mapping[s[i]]
        else:
            sum += mapping[s[i]]
    return sum

print(romanToInt("MCMXCIV"))
