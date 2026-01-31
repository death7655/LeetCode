from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_characters = Counter(s)
        
        smallest_key = min(unique_characters, key=unique_characters.get)
        
        if min(unique_characters.values()) > 1:
            return -1
        
        return s.index(smallest_key) 
        
        