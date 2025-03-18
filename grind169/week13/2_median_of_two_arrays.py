from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        total = n + m
        median_idx = total // 2
        n_idx = 0
        m_idx = 0
        checked = 0
        merged = []
        while n_idx < n and m_idx < m and checked <= median_idx + (0 if total % 2 else 1):
            if nums1[n_idx] < nums2[m_idx]:
                merged.append(nums1[n_idx])
                n_idx += 1
            else:
                merged.append(nums2[m_idx])
                m_idx += 1
            checked += 1

        while checked <= median_idx + (0 if total % 2 else 1):
            if n_idx < n:
                merged.append(nums1[n_idx])
                n_idx += 1
            if m_idx < m:
                merged.append(nums2[m_idx])
                m_idx += 1
            checked += 1

        if total % 2:
            return merged[median_idx]
        else:
            return (merged[median_idx] + merged[median_idx - 1]) / 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
    print(solution.findMedianSortedArrays([1, 3, 4, 5, 6, 7], [2]))
