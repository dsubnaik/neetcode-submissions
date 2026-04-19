class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for i in range(len(s)):
            if s[i] in pairs:          # opening bracket
                stack.append(pairs[s[i]])  # push expected closing bracket
            else:                       # closing bracket
                if not stack or stack.pop() != s[i]:
                    return False

        return not stack