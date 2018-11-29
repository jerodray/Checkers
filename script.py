from SingleMove import SingleMove
import numpy as np

friendly = np.array([(1, 0, False), (3, 0, False), (5, 0, False), (7, 0, False),
                     (0, 1, False), (2, 1, False), (4, 1, False), (6, 1, False),
                     (1, 2, False), (3, 2, False), (5, 2, False), (7, 2, False)])
enemy = np.array([(0, 7, False), (2, 7, False), (4, 7, False), (6, 7, False),
                  (1, 6, False), (3, 6, False), (5, 6, False), (7, 6, False),
                  (0, 5, False), (2, 5, False), (4, 5, False), (6, 5, False)])
# friendly = np.array([(1, 7, True)])
# enemy = np.array([(4, 4, False)])

checkers = SingleMove(friendly, "red", enemy, "black")
