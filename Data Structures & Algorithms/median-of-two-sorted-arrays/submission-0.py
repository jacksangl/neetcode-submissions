class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        l, r, = 0, len(A) - 1
        while True:
            mA = (l+r) // 2
            mB = half - mA - 2

            left_A = A[mA] if mA >= 0 else -float('inf')
            right_A = A[mA+1] if mA+1 < len(A) else float('inf')
            left_B = B[mB] if mB >= 0 else -float('inf')
            right_B = B[mB+1] if mB+1 < len(B) else float('inf')

            if left_A <= right_B and left_B <= right_A:
                # even
                if total % 2 == 0:
                    return ((max(left_A, left_B) + min(right_A, right_B)) / 2)
                # odd
                else:
                    return min(right_A, right_B)
            
            elif left_A > right_B:
                r = mA - 1
            else:
                l = mA + 1
            