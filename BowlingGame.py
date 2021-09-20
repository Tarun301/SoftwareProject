class BowlingGame:
    def __init__(self):
        self.rolls = []

    # This method checks the Number of rolls and pins knocked down by a player
    def roll(self, pins):
        self.rolls.append(pins)

    # This method checks the score as per the frame Index.
    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    # This method checks the game as per the pins knocked down by a player is that a strike game.
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    # This method checks the game with the no of pins kocked down by the rolls as per the frame Index to check
    # is that a Spare Game.
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10

    # This method checks the Strike Game Score
    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex+1] + self.rolls[rollIndex+2]

    # This method checks the Spare Game Score
    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex+2]

    # This method checks the Frame Score
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]



