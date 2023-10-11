class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        if len(arr) == 1:
            return True
        temp = dict()
        for item in arr:
            if item not in temp.keys():
                temp[item] = 1
            else:
                temp[item] += 1
        return len(temp.values()) == len(set(temp.values()))

    def unique_phone_num(self, num):
        arr = []
        for n, item in enumerate(str(num)):
            if item not in arr:
                arr.append(item)
        return len(arr) == 10


arr = [1, 2, 2, 1, 1, 3]
sol = Solution()
# print(sol.uniqueOccurrences(arr))
# print(sol.uniqueOccurrences([1,2]))
print(sol.unique_phone_num(1232567890))
