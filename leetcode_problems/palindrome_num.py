

def isPalindrome(x: int) -> bool:
    pass

def convert_int_to_arr(num) -> list:
    if num < 10:
        return [num]
    output = []
    multiplier = 10
    while int(num / multiplier) > 0:
        output.append(num % multiplier)
        multiplier *= 10
    return output


print(convert_int_to_arr(124))