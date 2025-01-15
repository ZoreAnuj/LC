class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: 
            return 0
        
        left_max, right_max = height[0], height[-1]
        l, r = 1, len(height)-1
        total_water = 0

        while l <= r:
            # Use current max heights (before updating) to determine which side to process
            if left_max <= right_max:
                # If current height is less than left_max, we can trap water here
                if height[l] < left_max:
                    total_water += left_max - height[l]
                # Update left_max after water calculation
                left_max = max(left_max, height[l])
                l += 1
            else:
                # If current height is less than right_max, we can trap water here
                if height[r] < right_max:
                    total_water += right_max - height[r]
                # Update right_max after water calculation
                right_max = max(right_max, height[r])
                r -= 1

        return total_water
