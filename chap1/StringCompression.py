"""
If we use str += str, it will copy the object multiple times to fit the new longer string. Thus, we can use a list to append it, then join together.
"""
def compress(s):
    ans = []
    counter = 0
    for i, c in enumerate(s):
        counter += 1
        if i + 1 >= len(s) or s[i+1] != c:
            ans.append(c)
            ans.append(str(counter))
            counter = 0
    ans = ''.join(ans)
    if len(s) <= len(ans):
        return s
    else:
        return ans

test = 'aaabbcccssdde'
print(compress(test))
