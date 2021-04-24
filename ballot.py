class Ballot:

    def __init__(self, centerID, ballotOptions):
        self.ballotChoices = ballotOptions
        self.voterChoice = None
        self.centerID = centerID