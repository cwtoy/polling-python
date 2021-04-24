class Voter:

    def __init__(self, firstName, lastName, birthday, phone, address, ssn):
        #Voter information
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
        self.phone = phone
        self.address = address
        self.SSN = ssn

        #Voting Center information
        self.registered = False
        self.voted = False
        self.votingCenter = None
        self.ballot = None

    def setBallot(self, ballot):
        self.ballot = ballot

    def getSSN(self):
        return self.SSN

    def hasRegistered(self):
        return self.registered

    def hasVoted(self):
        return self.voted

    def registerVotingCenter(self, centerID):
        if self.votingCenter is None:
            self.votingCenter = centerID

