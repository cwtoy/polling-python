from VotingCenter import VotingCenter
from Ballot import Ballot
from NewVoter import Voter

sam = Voter("Sam", "Goodin", "09/12", "3179912791", "123 Memory Lane", "1234567890")

VotingCenter1 = VotingCenter(415)

ballotChoices = ["firstOption", "secondOption", "thirdOption"]
ballot = Ballot(ballotChoices)
