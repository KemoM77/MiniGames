import turtle

def gameBoardDrawer():
    for i in range(2):
        myPen.penup()
        myPen.goto(-300,100-200*i)
        myPen.pendown()
        myPen.forward(600)
   

    myPen.right(90)
    for i in range(2):
      myPen.penup()
      myPen.goto(100 - 200*i ,300)
      myPen.pendown()
      myPen.forward(600)

    num = 1 
    for i in range(3):
        for j in range(3):
            myPen.penup()
            myPen.goto(-290+j*200,275 - 200*i)
            myPen.write(num,font = ("Arial",11))
            num+=1


    board.update()

def shapeX(x,y):
    myPen.color("Black")
    myPen.penup()
    myPen.goto(x,y)
    myPen.setheading(60)
    myPen.pendown()
    for i in range(2):
        myPen.forward(75)
        myPen.backward(150)
        myPen.forward(75)
        myPen.setheading(120)

    board.update()

def shapeO(x,y):

    myPen.color("Black")
    myPen.penup()
    myPen.goto(x-90,y-130)
    myPen.pendown()
    myPen.write("O", font = ("Arial",170))
    board.update()


def putX(row,col):
    if gameBoard[row][col] != "  ":
        notifier.penup()
        notifier.goto(-200,0)
        notifier.write("This spot is already filled in!", font = ("Arial" , 30))
    else:
        notifier.clear()
        shapeX(-200 +200*col,200 -200 * row)
        gameBoard[row][col] = "x"
        

        if isWon("x") :
            notifier.goto(-100,0)
            notifier.write("You Won !", font=("Arial",40))
            disAssign()
                        
        else:
            isDraw()
            putO()
            if isWon("o") :
              notifier.goto(-100,0)
              notifier.write("You Lost !", font=("Arial",40))
              disAssign()
                
    board.update()


def isDraw():
 xCount = 0
 for i in range(3):
        for j in range(3):
            if gameBoard[i][j] == "x":
                xCount+=1
 if xCount == 5 :
     notifier.goto(-100,0)
     notifier.write("This is a draw !",font=("Arial",40))
     disAssign()




def putO():
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j] == "  ":
                gameBoard[i][j] = "o"
                if(isWon("o")):
                    shapeO(-200 + 200 * j , 200 -200 * i)
                    return
                gameBoard[i][j] = "  "
    
    for i in range(3):
      for j in range(3):    
          if gameBoard[i][j] == "  ":
                 gameBoard[i][j] = "x" 
                 if isWon("x"):
                     gameBoard[i][j] = "o"
                     shapeO(-200 + 200 * j , 200 -200 * i)
                     return
                 gameBoard[i][j] = "  "
                 
    for i in range(0,3,2):
        for j in range(0,3,2):
            if  gameBoard[i][j] == "  ":
                  gameBoard[i][j] = "o"
                  shapeO(-200 + 200 * j , 200 -200 * i)
                  return
            
    for i in range(3):
     for j in range(3):    
          if gameBoard[i][j] == "  ":
                gameBoard[i][j] = "o"
                shapeO(-200 + 200 * j , 200 -200 * i)
                return



def  isWon(c):
    for i in range(3):
        if gameBoard[i][0] == gameBoard[i][1]  and gameBoard[i][1] == gameBoard[i][2] and gameBoard[i][2] == c:
             return True
        if gameBoard[0][i] == gameBoard[1][i]  and gameBoard[1][i] == gameBoard[2][i] and gameBoard[2][i] == c:
             return True
    if gameBoard[0][0] == gameBoard[1][1]  and gameBoard[1][1] == gameBoard[2][2] and gameBoard[2][2] == c:
             return True
    if gameBoard[0][2] == gameBoard[1][1]  and gameBoard[1][1] == gameBoard[2][0] and gameBoard[2][0] == c:
             return True
    
    return False


def spot1():
    putX(0, 0)

def spot2():
    putX(0, 1)

def spot3():
    putX(0, 2)

def spot4():
    putX(1, 0)

def spot5():
    putX(1, 1)
def spot6():
    putX(1, 2)

def spot7():
    putX(2, 0)

def spot8():
    putX(2, 1)

def spot9():
    putX(2, 2)

def assignSpotsOnKey():
    for i in range(9):
        board.onkey(spots[i], str(i+1))


def disAssign():
    for i in range(9):
        board.onkey(None, str(i+1))






spots = [spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9]

notifier = turtle.Turtle()
notifier.ht()
notifier.color("Red")


myPen = turtle.Turtle()

myPen.pensize(11)
myPen.color("Blue")
myPen.hideturtle()

board = turtle.Screen()
board.tracer(0)
gameBoardDrawer()


gameBoard = []
for i in range(3):
    row = []
    for j in range(3):
        row.append("  ")
    gameBoard.append(row)





assignSpotsOnKey()

board.listen()

board.mainloop()