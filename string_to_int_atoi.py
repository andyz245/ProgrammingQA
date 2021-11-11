class Solution:
    def myAtoi(self, s: str) -> int:
        
        fil_str = ""
        it = 0
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        # remove whitespace
        s = s.strip()

        # s is only whitespace
        if (s == ''):
            return 0

        # negative
        if (s[0] == '-'):
            fil_str += s[0]
            it += 1

        # positive
        if (s[0] == '+'):
            it += 1

        # iterate through digits
        while it < len(s) and s[it] in digits:
            fil_str += s[it]
            it += 1

        # no digits found
        if (fil_str == '-' or fil_str == ''):
            return 0
        else:
            res = int(fil_str)

        # out of bounds
        if res > 2**31 - 1:
            res = 2**31 - 1
            
        if res < 2**31 * -1:
            res = 2**31 * -1
            
        return res
        
        
