class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            m = (l + r) // 2
            h = half - m - 2

            Aleft = A[m] if m >= 0 else float("-infinity")
            Aright = A[m + 1] if (m + 1) < len(A) else float("infinity")
            Bleft = B[h] if h >= 0 else float("-infinity")
            Bright = B[h + 1] if (h + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1
