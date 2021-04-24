from Ballot import Ballot


class BallotCounter:

    def __init__(self, centerID):
        self.ballot = None
        self.centerID = centerID

    def createBallot(self, ballotOptions):
        self.ballot = Ballot(self.centerID, ballotOptions)

    def getBallot(self):
        if self.ballot is not None:
            return self.ballot
        else:
            return None

    def countBallots(self):

