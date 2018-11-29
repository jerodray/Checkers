import model
import view


class SingleMove:

    def __init__(self, friendly, friendly_color, enemy, enemy_color):
        self.board = model.board
        self.checkers = model.checkers
        self.buildGame(friendly, friendly_color, enemy, enemy_color)
        self.view(view.win1)
        view.runAI(True)
        # print("(click once on the left checkerboard to close the application)")
        # click1 = view.win1.getMouse()
        input("Press Enter to close application...")

    def buildGame(self, friendly, friendly_color, enemy, enemy_color):
        # Init Board ("Pieces" = Squares on the board)
        for x in range(0, 8):
            for y in range(0, 8):
                self.board[x, y] = model.Piece(x * 62.5, y * 62.5)
        # Set checker color correctly
        view.color_ai = friendly_color
        view.color_opponent = enemy_color
        # Place Checkers ("Checkers" = Circular Plastic Guys)
        for f in friendly:
            self.addChecker(f[0], f[1], f[2], True)
        for e in enemy:
            self.addChecker(e[0], e[1], e[2], False)

    def view(self, window):
        view.drawBoard(window)
        view.drawCheckers(window)

    def addChecker(self, x, y, is_king, is_friendly):
        checker = model.Checker()
        checker.id = (x, y)
        checker.index = x * 8 + (y + 1)
        checker.black = is_friendly
        checker.x = x
        checker.y = y
        checker.king = is_king
        self.board[x, y].checker = checker
        self.checkers.append(checker)
