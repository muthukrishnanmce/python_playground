def two_sum(nums: list, target: int) -> list[int]:
    dictionary = dict()
    for i, num in enumerate(nums):
        dictionary[num] = i

    for i, num in enumerate(nums):
        diff = target - num
        diff_pos = dictionary.get(diff)
        if diff_pos and diff_pos != i:
            return [i, dictionary.get(diff)]
    return []

input_value = [3,3]
target = 6
output = two_sum(input_value, target)
print(output)