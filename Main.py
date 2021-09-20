import unittest
import BowlingGame


class TestBowlingGame(unittest.TestCase):

    # This is the Testing function of the Bowling Game that tests the test cases as self.
    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    # This is the testing function of the Gutter Game, When a player rolls the ball & no pins are knocked down
    # That results in a score of zero, is called a Gutter Game.
    def testGutterGame(self):
        self.rollMany(0, 20)
        self.assertEqual(0, self.game.score())

    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(20, self.game.score())

    # This is the testing function of one spare game roll, when a player got a spare in a frame Index.
    def testOneSpare(self):
        self.rollSpare()
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(23, self.game.score())

    def testTwoSpare(self):
        self.rollSpare()
        self.rollSpare()
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(46, self.game.score())

    def testThreeSpare(self):
        self.rollSpare()
        self.rollSpare()
        self.rollSpare()
        self.game.roll(2)
        self.rollMany(0, 18)
        self.assertEqual(67, self.game.score())

    # This is testing function of a one strike game played by a player.
    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(24, self.game.score())

    # If a player knocks down all 10 pins in the tenth frame, the player is allowed to throw 3 balls for that frame.
    # This allows for a potential of 12 strikes in a single game
    # and A maximum score of 300 points, is called a Perfect Game.
    def testPerfectGame(self):
        self.rollMany(10, 12)
        self.assertEqual(300, self.game.score())

    # This function checks here is all the spare games played by the players
    # When a player knocks down all the ten pins with the two balls of a frame then it is called a Spare
    def testAllSpares(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150

    def test_simple_game(self):
        for pins in [1, 4, 4, 5, 6, 4, 5, 5,
                     10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]:
            self.game.roll(pins)
        self.assertEqual(133, self.game.score())

    # When a player knocks down all the ten pins with their first ball, then it results in a Strike.
    def testAllStrikes(self):
        self.rollMany(6, 31)
        self.assertEqual(120, self.game.score())

    # This is the testing function for of rolling the many balls by a player.
    def rollMany(self, pins, num):
        for i in range(num):
            self.game.roll(pins)

    # This function checks the spare balls by a player in the frames.
    def rollSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(5)



