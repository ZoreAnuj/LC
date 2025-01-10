class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start from the last position in nums1
        current_place = m + n - 1
        
        # Copy elements from back to front
        while n > 0:
            # If m is 0, just copy remaining nums2 elements
            if m == 0:
                nums1[current_place] = nums2[n-1]
                n -= 1
                current_place -= 1
                continue
                
            # Compare the last valid elements from both arrays
            if nums1[m-1] > nums2[n-1]:
                nums1[current_place] = nums1[m-1]
                m -= 1
            else:
                nums1[current_place] = nums2[n-1]
                n -= 1
            current_place -= 1

                
            
            


            


        
