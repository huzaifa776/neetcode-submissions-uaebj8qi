class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        highest_number = -1
        for index in range(len(arr) -1, -1, -1):
            current_number = arr[index]
            arr[index] =  highest_number
            if current_number > highest_number:
                highest_number = current_number    
        return arr