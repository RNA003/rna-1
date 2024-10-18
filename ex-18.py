def isdup(s):
    if len(s)==0:
        return True
    for i in range(1,len(s)//2+1):
        if s[:i] *2==s:
            return True
    return isdup(s[1:])