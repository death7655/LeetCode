class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 -1
        output = 0
        negative = False
        
        if x < 0:
            x *= -1
            negative = True
        
        
        
        while x != 0:
            digit = x % 10
            x//=10
            output = (output * 10) + digit
            
        if negative:
            output *= -1
        
        if output > INT_MAX or output < INT_MIN:
            return 0
         
        return output
            
            
            
            
        
        
        