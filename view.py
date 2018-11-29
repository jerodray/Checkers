import ai
import time
import graphics
from graphics import Point
import model


width = 500
height = 500
offset_x = width / 8
offset_y = height / 8

win1 = graphics.GraphWin("Initial State", width, height)
win1.master.geometry('%dx%d+%d+%d' % (width, height, 20, 0))

win2 = graphics.GraphWin("Final State", width, height)
win2.master.geometry('%dx%d+%d+%d' % (width, height, 540, 0))

color_ai = "red"
color_opponent = "black"

def drawBoard(window):
    color_offset = False
    for x in range(0, 8):
        if x % 2 == 1:
            color_offset = True
        else:
            color_offset = False
        for y in range(0, 8):
            point = Point(x * offset_x, y * offset_y)
            box = graphics.Rectangle(point, Point(point.x + offset_x, point.y + offset_y))
            box.setFill("Gray")
            if color_offset:
                if x % 2 == 0 or y % 2 == 0:
                    box.setFill("#c2ab56")
            elif x % 2 == 1 or y % 2 == 1:
                box.setFill("#c2ab56")
            box.draw(window)


def drawCheckers(window):
    for piece in model.board.flat:
        if piece.checker is not None:
            # Hacky mirror board implementation, by Jerod Ray
            mirrored_center_x = 500 - piece.center[0]
            mirrored_center_y = 500 - piece.center[1]
            circle = graphics.Circle(Point(mirrored_center_x, mirrored_center_y), 15)
            # Original Implementation
            # circle = graphics.Circle(Point(piece.center[0], piece.center[1]), 15)
            if piece.checker.black:
                circle.setFill(color_ai)
            else:
                circle.setFill(color_opponent)
            circle.draw(window)


def findPiece(click):
    click_x = click.x/62.5
    click_y = click.y/62.5
    for x in range(0, 8):
        for y in range(0, 8):
            if (click_x > x and click_y > y) and (click_x < x+1 and click_y < y+1):
                return (x, y)
    return None





def redraw(window):
    for child in window.children:
        child.undraw()
    drawBoard(window)
    drawCheckers(window)


def runAI(color):
    t1 = time.time()
    ai_move = ai.minimax(0, color, model.board, float("-inf"), float("inf"))
    if ai_move is None:
        raise Exception("No Possible Moves")
    # print(ai_move.weight)
    t2 = time.time()
    # print(t2-t1)
    model.ttable.hashtable = {}

    alphabet = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    old_x = ai_move.checker.x
    old_y = ai_move.checker.y
    new_x = ai_move.piece.x / 62.5
    new_y = ai_move.piece.y / 62.5
    print("Your Move --> " + alphabet[old_x] + str(old_y+1) + " to " + alphabet[int(new_x)] + str(int(new_y+1)))
    
    ai_move.apply(model.board)
    redraw(win2)
    return ai_move


# def chooseDif():
#     difwin = graphics.GraphWin("Choose Difficulty")
#     difwin.focus()
#     entry = graphics.Entry(Point(100, 100), 20)
#     entry.setText("2")
#     entry.draw(difwin)
#     difwin.getMouse()
#     ai.DIFFICULTY = int(entry.getText())
#     difwin.close()

def playerTurn(color):
    while True:
        click1 = win1.getMouse()
        checker = findPiece(click1)
        if checker is None or model.board[int(checker[0]), int(checker[1])].checker is None or model.board[int(checker[0]), int(checker[1])].checker.black is not color:
            continue
        click2 = win1.getMouse()
        piece = findPiece(click2)
        if piece is None or (piece[0] == checker[0] and piece[1] == checker[1]):
            continue
        partial_move = ai.Move(model.board[int(checker[0]),int(checker[1])].checker, model.board[int(piece[0]),int(piece[1])], "?")
        partial_move.checker.x = checker[0]
        partial_move.checker.y = checker[1]
        move = model.getFullMove(partial_move)
        if move is None:
            continue
        else:
            move.apply(model.board)
            redraw(win1)
            return

# def draw():
#     drawBoard()
#     drawCheckers()
#     while model.hasWon(model.board) == 0:
#         sleep(0.01)
#         model.King(model.board)
#         playerTurn(False)
#         model.King(model.board)
#         win.update()
#         runAI(True)
#     winWindow = graphics.GraphWin("Game over")
#     if model.hasWon(model.board) == 1:
#         text = graphics.Text(Point(winWindow.width/2, winWindow.height/2), "You Won!!")
#         text.draw(winWindow)
#         sleep(3)
#     elif model.hasWon(model.board) == -1:
#         text = graphics.Text(Point(winWindow.width / 2, winWindow.height / 2), "You Lost :(")
#         text.draw(winWindow)
#         sleep(3)
#     return
