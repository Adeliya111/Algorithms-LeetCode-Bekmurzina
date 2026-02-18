class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(a):
            if len(a) <= 1:
                return a

            mid = len(a) // 2
            left = merge_sort(a[:mid])
            right = merge_sort(a[mid:])

            i = j = 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            res.extend(left[i:]) # добавление элементов в список
            res.extend(right[j:])
            return res

        return merge_sort(nums)


