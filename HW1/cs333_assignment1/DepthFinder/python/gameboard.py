import random
import math


class GameBoard:
    def __init__(self, boardsize):
        self.size = boardsize
        self._queries_remaining = 3 * math.ceil(math.log(self.size, 2))
        self._board = [0 for i in range(self.size)]
        self._board[0] = 1
        self._board[1] = 2
        self._board[-1] = 3
        self._board[-2] = 4
        self._minlocation = random.randrange(2, boardsize-2)
        self._minvalue = random.randint(10, self.size**3)

    def __str__(self):
        s = "["
        for d in self._board:
            if d > 0:
                s += str(d) + ","
            else:
                s += "??,"
        return s + "]"


    def ping(self, location):
        self._queries_remaining -= 1
        if self._queries_remaining < 0:
            print("out of queries")
            return 0
        if self._board[location] > 0:
            return self._board[location]
        if location == self._minlocation:
            self._board[location] = self._minvalue
            return self._board[location]
        pinged_left = 1
        for i in range(len(self._board)):
            depth = self._board[i]
            if i < location and depth > 0:
                pinged_left = i
        pinged_right = self.size-2
        for i in range(len(self._board) - 1, -1, -1):
            depth = self._board[i]
            if i > location and depth > 0:
                pinged_right = i
        if location < self._minlocation:
            if pinged_right > self._minlocation:
                self._board[location] = (self._board[pinged_left] + self._minvalue) / 2
            else:
                self._board[location] = (self._board[pinged_left] + self._board[pinged_right]) / 2
        elif location > self._minlocation:
            if pinged_left < self._minlocation:
                self._board[location] = (self._board[pinged_right] + self._minvalue) / 2
            else:
                self._board[location] = (self._board[pinged_left] + self._board[pinged_right]) / 2
        return self._board[location]

    def final_answer(self, location):
        if (self._queries_remaining < 0):
            print("out of pings")
        elif (self._board[location - 1] <= 0) or (self._board[location] <= 0) or (
                self._board[location + 1] <= 0):
            print("neighbors not queried")
        elif (self._board[location - 1] < self._board[location] > self._board[location + 1]):
            print("trench found!")
        else:
            print("not a trench")
