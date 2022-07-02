stack = []
  #Add elements to the stack.
  for letter in s:
    if letter == '(':
        stack.append(')')
        continue
    if letter == '[':
        stack.append(']')
        continue
    if letter == '{':
        stack.append('}')
        continue
    #Remove elements of the stack
    if len(stack) != 0 and stack[-1] == letter:
        stack.pop()
        
    else:
        return False
        
if (not stack):
    return True
else:return False
