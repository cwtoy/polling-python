#class definition for Voter
class Voter:
    str firstName
    str lastName
    str birthday
    str phone
    str address
    #assigned by Voter Registration Center
    #int voterNum
    #going with social security number instead
    str social
    bool registered = False
    bool voted = True

#getters and setters
    def getFirstName(self):
        return self.firstName

    def setFirstName(self, name):
        self.firstName = name

    def getLastName(self):
        return self.lastName

    def setLastName(self, name):
        self.lastName = name

    def getBirthday(self):
        return self.birthday

    def setBirthday(self, birthday):
        self.birthday = birthday

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getVoterNum(self):
        return self.voterNum

    def setVoterNum(self, num):
        self.voterNum = num

    def getRegistered(self):
        return self.registered

    def setRegistered(self, registered):
        self.registered = registered

    def getVoted(self):
        return self.voted

    def setVoted(self, voted):
        self.voted = voted

#class definition for Voter Registration Center
class VRC:
    #holds list of all instantiated voters
    Voter voterList = []
    #number designating which VRC this is
    centerNum = -1

    #I dont remember what I was doing with the registered flag but I'll figure it out later
    #registers an instance of the voter class with the system
    def registerVoter(self, voter):
        int registeredFlag = 0
        for v in voterList:
            if v.social == voter.social && voter.registered == false:
                registeredFlag = 1
        if registeredFlag = 0:
            voterList.append(voter)
            voter.setRegistered(True)

    
            
    
