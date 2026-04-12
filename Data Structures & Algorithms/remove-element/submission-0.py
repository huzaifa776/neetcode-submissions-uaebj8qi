class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        safe_position = 0

        for current_number in nums:
            if current_number != val:

                nums[safe_position] = current_number
                
                safe_position = safe_position + 1
                
        return safe_position