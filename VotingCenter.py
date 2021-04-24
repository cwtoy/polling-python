from BallotCounter import BallotCounter


class VotingCenter:

    def __init__(self, centerID):
        self.registeredVoters = []
        self.centerID = centerID
        self.ballotCounter = BallotCounter(self.centerID)

    def registerVoter(self, voter):
        self.registeredVoters.append(voter)

    def getCenterID(self):
        return self.centerID

    def sendOutBallots(self):
        #All registered voters get the ballot from the ballot counter
        for voter in self.registeredVoters:
            voter.ballot = self.ballotCounter.getBallot()
