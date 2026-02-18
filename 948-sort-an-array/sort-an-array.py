from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(a):
            if len(a) <= 1:
                return a

            mid = len(a) // 2
            left = merge_sort(a[:mid])
            right = merge_sort(a[mid:])

            i = j = 0
            result = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:]) # добавление элементов в список
            result.extend(right[j:])
            return result

        return merge_sort(nums)


