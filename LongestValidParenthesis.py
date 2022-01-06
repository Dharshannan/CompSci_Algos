s = "()(()"
stack = [-1]
maxlen = 0
for i in range(0,len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()
    
    if stack == []:
        stack.append(i)
        
    else:
        maxlen = max(maxlen, i - stack[-1])
    print(stack)
        
print(maxlen)
        
    
            
                
            
    