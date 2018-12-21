def find_word(sboard, word):
    al=len(board)
    vl=len(board[0])
    for arr in range(al):
        for value in range(vl):  
            if board[arr][value]==word[0]:
                if len(word)==1:
                    return True
                board[arr][value]='_'
                if search(board,word,arr,value,1):
                    board[arr][value]=word[0]
                    return True
                else:
                    board[arr][value]=word[0]
    return False



def search(board,word,row,col,index):
    al=len(board)
    vl=len(board[0])
    w=word[index]
    for i in range(3):
        for j in range(3):
            if row-1+i>=0 and row-1+i<al and col-1+j>=0 and col-1+j<vl and board[row-1+i][col-1+j]==w:
                if index+1==len(word):
                    return True
                else:
                    board[row-1+i][col-1+j]='_'
                    if search(board,word,row-1+i,col-1+j,index+1):
                        board[row-1+i][col-1+j]=w
                        return True
                    else:
                        board[row-1+i][col-1+j]=w
                break
    return False
    
testBoard = [
      ["E","A","R","A"],
      ["N","L","E","C"],
      ["I","A","I","S"],
      ["B","Y","O","R"]
    ]

find_word(testBoard,'RSCAREIOYBAILNEA')