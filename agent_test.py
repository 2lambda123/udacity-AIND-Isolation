"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload
from sample_players import open_move_score

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)


from game_agent import MinimaxPlayer, AlphaBetaPlayer
from sample_players import GreedyPlayer

def test1():
    player1 = AlphaBetaPlayer(search_depth=2, name='p1', score_fn=open_move_score)
    player2 = AlphaBetaPlayer(search_depth=2, name='p2', score_fn=open_move_score)
    game = isolation.Board(player1, player2, height=9, width=9)
    game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 60]
    game.play(time_limit=1000000000)

def test2():
    player1 = MinimaxPlayer(search_depth=1)
    player2 = MinimaxPlayer(search_depth=0)
    game = isolation.Board(player1, player2, height=4, width=4)
    game.apply_move((2, 0))
    game.apply_move((0, 1))
    game.apply_move((1, 2))
    game.apply_move((2, 2))
    game.apply_move((3, 1))
    print(game.to_string())
    print(player2.score(game, player1))
test1()



