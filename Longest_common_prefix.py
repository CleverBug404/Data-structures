strs = ['gatro','perro','gatp']

prefix = ''

if len(strs) == 0:
    print("")
if len(strs) == 1:
    print(strs[0])

smallest_word = min(strs, key=len)
strs.remove(smallest_word)

for i in range(len(smallest_word)):
    for s in strs:
        if smallest_word[i] != s[i]:
            return prefix
            
    prefix += smallest_word[i]
return prefix
