class Solution(object):
    def isValid(self, s):
        bracket_list = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in bracket_map:
                #Verify if the bracket_list is empty and the last element of the bracket list corespond to char element in bracket_map
                if bracket_list and bracket_list[-1] == bracket_map[char]:
                    bracket_list.pop()
                else:
                    return False
            else:
                bracket_list.append(char)


        return not bracket_list

solution = Solution()
print(solution.isValid("(]"))

     
