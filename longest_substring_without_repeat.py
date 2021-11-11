class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        
        begin = 0
        end = 0
        longest_substr = ""
        longest_len = 0
        
        while (begin != len(s)):
            end = begin
            substr_len = 0
            substr = ""
            
            while end < len(s) and s[end] not in chars:
                chars[s[end]] = 1
                substr += s[end]
                substr_len += 1
                end += 1
            if (substr_len > longest_len):
                longest_len = substr_len
                longest_substr = substr
                
            begin += 1
            chars.clear()
            
        return longest_len
                
            
            
            
        
