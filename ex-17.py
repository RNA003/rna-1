def solve(exp,x):
    if isinstance(exp,int):
        return exp
    elif exp[0]== 'x':
        return x
    else:
        operator = exp[0]
        left=solve(exp[1],x)
        right=solve(exp[2],x)
        if operator == 'x'
            return left+right
        elif operator =='-':
            return left-right
        elif operator =='*':
            return left*right
        elif operator =='/':
            return left/right
        