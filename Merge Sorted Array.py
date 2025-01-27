class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # i = 0
        # j = 0
        # index = 0
        # while index < m + n:
        #     if i < m and i < len(nums1) and j < len(nums2) and nums1[i] <= nums2[j] :
        #         nums1[index] = nums1[i]
        #         print("here1", nums1, "i", i)
        #         index += 1
        #         i += 1
        #     elif j < n and i < len(nums1) and j < len(nums2) and nums2[j] < nums1[i]:
        #         nums1[index] = nums2[j]
        #         print("here2", nums1, "j", j)
        #         index += 1
        #         j += 1
        #     elif i == m and j < n:
        #         nums1[index] = nums2[j]
        #         print("here3", nums1, "j", j)
        #         index += 1
        #         j += 1
        #     elif j == n and i < m:
        #         nums1[index] = nums1[i]
        #         print("here4", nums1, "i", i)
        #         index += 1
        #         i += 1
        nums2 = nums1[:m] + nums2[:n]
        nums2.sort()
        for i in range(n + m):
            nums1[i] = nums2[i]
        # print(nums2)
        
