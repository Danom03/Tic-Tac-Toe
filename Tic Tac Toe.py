def board(l):               #this function prints board
    count1 = 0
    for i in l:
        count1 +=1
        count2 = 0
        for j in i:
            count2 +=1
            if count2 < 3:
                print(j + "|", end = '')
            else:
                print(j, end = '')
        print()
        if count1 > 2:
            break
        else:
            print("------")

def move(l,player):                 #this function is use for movements
    print("Your move?")
    i = int(input())
    if i < 4:
        if l[2][i-1] == ' ':
            l[2][i-1] = player
        else:
            return("Error!")
    elif i > 3 and i < 7:
        if l[1][i-4] == ' ':
            l[1][i-4] = player
        else:
            return("Error!")
    elif i > 6 and i < 10:
        if l[0][i-7] == ' ':
            l[0][i-7] = player
        else:
            return("Error!")
    else:
        return("Error!")

def winner(l,player):           #this function is used to check winner
    count = 0
    for i in range(3):
        if l[i][0] == player:
            if l[i][1] == player:
                if l[i][2] == player:
                    if player == 'X':
                        return "Player 1 is winner!"
                    else:
                        return "Player 2 is winner!"
    for j in range(3):
        if l[0][j] == player:
            if l[1][j] == player:
                if l[2][j] == player:
                    if player == 'X':
                        return "Player 1 is winner!"
                    else:
                        return "Player 2 is winner!"
    for k in range(3):
        if l[k][k] == player:
            count +=1
    if count == 3:
        if player == 'X':
            return "Player 1 is winner!"
        else:
            return ("Player 2 is winner!")
    count = 0
    for m in range(0,3):
        if l[m][2-m] == player:
            count +=1
    if count == 3:
        if player == 'X':
            return ("Player 1 is winner!")
        else:
            return ("Player 2 is winner!")

l = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
board(l)
#instructions
print("Player1 is 'X'. \nPlayer2 is 'O'.")
print("Use positions of number on numpad for moves.")
p1 = 'X'
p2 = 'O'
s = None

for i in range(9):
    if i % 2 == 0:
        foo = move(l,p1)
        while foo == "Error!":
            print(foo)
            foo = move(l,p1)
        board(l)
        s = winner(l,p1)
        if s != None:
            print(s)
            break
    else:
        foo = move(l,p2)
        while foo == "Error!":
            print(foo)
            foo = move(l,p2)
        board(l)
        s = winner(l,p2)
        if s != None:
            print(s)
            break
else:
    print("Match Draw!!")
