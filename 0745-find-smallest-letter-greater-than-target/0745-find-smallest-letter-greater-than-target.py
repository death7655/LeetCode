class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        output = letters[0]
        n = len(letters)

        lower = 0
        upper = n-1
        current_output = output
        while(lower<=upper):
            middle = (upper + lower)//2
            if letters[middle] > target:
                current_output = letters[middle]
                upper = middle-1
            elif letters[middle] < target or letters[middle] == target:
                lower = middle+1
        
        return current_output


        