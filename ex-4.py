def dec_to_bin(n):
#base_case:
    if n==0:
        return " "
    else:
        return dec_to_bin(n // 2) + str(n% 2)