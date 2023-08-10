class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        length = len(nums1) + len(nums2)
        half = length//2
        if len(b)<len(a):
            a, b = nums2, nums1
        L, R = 0, len(a)-1
        while True:
            mid = (L+R)//2
            w = half-mid-2
            Aleft = a[mid] if mid>=0 else float("-infinity")
            Aright = a[mid+1] if (mid+1)<len(a) else float("infinity")
            Bleft = b[w] if w>=0 else float("-infinity")
            Bright = b[w+1] if (w + 1)<len(b) else float("infinity")
            if Aleft>Bright:
                R = mid-1
            elif Bleft > Aright:
                L = mid+1
            else:
                if length%2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2


