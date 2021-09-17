import unittest
import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        self.rollMany(0, 20)
        self.assertEqual(0, self.game.score())

    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(20, self.game.score())

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

    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(24, self.game.score())

    def testPerfectGame(self):
        self.rollMany(10, 12)
        self.assertEqual(300, self.game.score())

    def testAllSpares(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150

    def test_simple_game(self):
        for pins in [1, 4, 4, 5, 6, 4, 5, 5,
                     10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]:
            self.game.roll(pins)
        self.assertEqual(133, self.game.score())

    def testAllStrikes(self):
        self.rollMany(6, 31)
        self.assertEquals(120, self.game.score())

    def rollMany(self, pins, num):
        for i in range(num):
            self.game.roll(pins)

    def rollSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(5)



