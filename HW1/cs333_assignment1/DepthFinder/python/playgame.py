from gameplayer import *
from gameboard import *

boardsize = int(input())
gb = GameBoard(boardsize)
trench = playgame_dc(gb, 0, gb.size-1)
print(gb)
gb.final_answer(trench)
