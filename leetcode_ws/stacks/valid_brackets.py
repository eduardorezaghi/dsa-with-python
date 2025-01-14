class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            # Validity check for opening brackets
            if char in ["(","[","{"]:
                stack.append(char)
            
            # Validity check for closing brackets
            elif char in [")","]","}"]:

                if not stack:
                    return False
                if char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False

        # if the stack is empty, it means we've seen all opening brackets.
        return not stack