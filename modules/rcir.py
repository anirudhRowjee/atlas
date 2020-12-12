"""
RCIR Module

Conduct an RCIR Election

These are the constraints - 
1. Candidates must be unique (either by ID or name)
2. Voters can have any ordering of candidates (or none), as long as there is no
    repeat of a candidate
3. In a very rare occurrance of a tie, the program will halt.

Representations - 
1. Candidate Object (Unique ID, Name/Title, Eliminated Status, Votes)
2. Voter (Unique ID, Prefernence List of Candidate Unique IDs)

Candidates will be stored in a hashmap/dictionary, while voters and their
preferences will be stored in an array to make iteration easier

** Algorithm

let there be a list of all voters with their preferences, and a hashmap of
candidates

function tabulate -> 

    iterate over voter's list
        let v be voter in list
            iterate over v preferences (let preferences be p, preference N be p*)
            while p* is eliminated
                p* = next preference in p
            register vote for p
        if iteration has ended (i.e. current candidate is last)
            check if a candidate has a majority (>50% votes)
                if majority:
                    break, report winner as candidate with majority
                else:
                    find candidate with least votes and mark them as eliminated


main routine ->

while there is no winner,
    call tabulate

There are some basic constraints within which this implementation works.
1. All Candidates are Unique
2. All Voters are Unique
3. Each Voter can order their preferences
"""
from uuid import uuid4


class Candidate:
    """
    Candidate Class - holds all information of every candidate in the election
    @param name: string - name of the candidate
    @param id: string - UUID4
    @param votes: integer - number of votes
    @param eliminated: boolean - elimination status of the candidate
    """

    def __init__(self, name):
        self.id = uuid4().hex
        self.name = name
        self.votes = 0
        self.eliminated = False


class Voter:
    def __init__(self, name, preferences_list):
        """
        Voter class - holds all information of every voter, along with the
        preference lists
        @param id: string - UUID4
        @param name: string - name of voter
        @param preferences_list: List[Voter] - ordered preference list of voters
        """
        self.id = uuid4().hex
        self.name = name
        self.preferences_list = preferences_list


class Election:
    """
    Election Class->

    # TODO dubious terminology
    @data winner: Candidate - Candidate who wins the election
    @param voters: List[Voter] - list of all voters in the election
    @param candidates: List[Candidate] - list of all candidates in the election

    @method tabulate() -> None
        * Iterate through the list of the candidates to find the latest
        candidate in each voters' preference list that has not been eliminated.
        Add a vote to this candidate
    @method addvote(candidate: Candidate) -> None
        * Add a vote to the candidate.
    @method eliminate(candidate: Candidate) -> None
        * eliminiate a candidate after they recieve the lowest votes.
    """

    def __init__(self, voters, candidates):
        """
        constructor
        @param voters - list of voters with their preference lists
        @param candidates - list of all candidates with their statuses
        """
        self.voters = voters
        self.candidates = candidates
        self.winner = None

    def eliminate(candidate):
        # eliminate a voter
        # TODO
        pass

    def addvote(candidate):
        # add a vote to a candidate
        # TODO
        pass

    def tabulate():
        # tabulate the election results
        # TODO
        pass

    def run():
        while not self.winner:
            self.tabulate()
        print(self.winner.name)
