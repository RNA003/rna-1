def isit(board,row,col):
    for i in range (row):
        if board[i][col]==1:
            return False
    for i,j in zip(range(row,-1,-1)),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    for i,j in zip(range(row,-1,-1)),range(col,8)):
        if board[i][j] == 1:
            return False
        return True

def queen(board,row):
    if row==N:
        print(board)
        return True
    for col in range(N):
        if isit(board,row,col):
            board[row][col]=1
            if queen(board,row+1):
                return True
            board[row][col]=0
        return False

N=8
board=[[0 for _ in range(N)] for _ in range(N)]
queen(board,0)

