##week13-5.py leetcode 2542
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        a = [(n2, n1) for n1, n2 in zip(nums1, nums2)]
        a.sort(reverse=True)
        heap = [a[i][1] for i in range(k)]
        heapify(heap)
        total = sum(heap)
        ans = total * a[k - 1][0]
        for i in range(k, len(nums2)):
            n2, n1 = a[i]
            heappush(heap, n1)
            total += n1 - heappop(heap)
            ans = max(ans, total * n2)
        return ans

