class BallotCount:

    def __init__(self):
        self.allCandidates = []
        self.candidate1 = 0
        self.candidate2 = 0
        self.candidate3 = 0
        self.candidate4 = 0
        self.candidate5 = 0
        self.candidate6 = 0

    def appendCandidates(self):
        self.allCandidates.append(self.candidate1)
        self.allCandidates.append(self.candidate2)
        self.allCandidates.append(self.candidate3)
        self.allCandidates.append(self.candidate4)
        self.allCandidates.append(self.candidate5)
        self.allCandidates.append(self.candidate6)

    def countVote(self, value):
        if value == 1:
            self.candidate1 += 1
        elif value == 2:
            self.candidate2 += 1
        elif value == 3:
            self.candidate3 += 1
        elif value == 4:
            self.candidate4 += 1
        elif value == 5:
            self.candidate5 += 1
        elif value == 6:
            self.candidate6 += 1
        else:
            pass

    def getWinner(self):
        winner = None
        idx = 0
        #loop ends at idx 2nd to last compared to idx last
        while idx < len(self.allCandidates) - 1:
            if winner:
                if winner < self.allCandidates[idx]:
                    winner = self.allCandidates[idx]
            else:
                winner = self.allCandidates[idx]
            idx += 1

        return winner
