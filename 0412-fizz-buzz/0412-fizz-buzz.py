class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(n):
            current_val = i+1
            if current_val % 5 == 0 and current_val % 3 == 0:
                output.append("FizzBuzz")
            elif current_val % 5 == 0:
                output.append("Buzz")
            elif current_val % 3 == 0:
                output.append("Fizz")
            else:
                output.append(str(current_val))
        
        return output
        