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
from typing import List, Dict, Tuple


class Candidate:
    """
    Candidate Class - holds all information of every candidate in the election
    @param name: string - name of the candidate
    @param id: string - UUID4
    @param votes: integer - number of votes
    @param eliminated: boolean - elimination status of the candidate

    @mtethod eliminate - eliminates the candidate
    """

    def __init__(self, name: str) -> None:
        self.id: str = uuid4().hex
        self.name: str = name
        self.votes: int = 0
        self.eliminated: bool = False

    def eliminate(self) -> None:
        # method to eliminate self
        if self.eliminated:
            raise Exception("Candidate is already eliminated")
        else:
            self.eliminated = True

    def addVote(self) -> None:
        # add a vote to the candidate
        self.votes += 1


class Voter:
    """
    Voter class - holds all information of every voter, along with the
    preference lists
    @param id: string - UUID4
    @param name: string - name of voter
    @param preferences_list: List[Voter] - ordered preference list of voters
    """

    def __init__(self, name: str, preferences_list: List[Candidate]) -> None:
        self.id: str = uuid4().hex
        self.name: str = name
        self.preferences_list: List[Candidate] = preferences_list


class Election:
    """
    Election Class->

    #TODO dubious terminology
    @data winner: Candidate - Candidate who wins the election
    @data majority: int - number of votes required to be considered a victor
    @param voters: List[Voter] - list of all voters in the election
    @param candidates: List[Candidate] - list of all candidates in the election

    @method tabulate() -> None
        * Iterate through the list of the candidates to find the latest
        candidate in each voters' preference list that has not been eliminated.
        Add a vote to this candidate
    """

    def __init__(self, voters: List[Voter], candidates: List[Candidate]) -> None:
        """
        constructor
        @param voters - list of voters with their preference lists
        @param candidates - list of all candidates with their statuses
        """
        self.voters: List[Voter] = voters
        # make this a dict so it's easier to lookup candidates to add voters or
        # eliminate candidates - this lookup is constant time
        self.candidates: Dict[str, Candidate] = {x.id: x for x in candidates}
        self.winner: Candidate = None
        # majority count - 50% + 1
        self.majority: int = int(len(self.voters) / 2) + 1

    def get_polar_candidates(self) -> List[str]:
        # return the id's of the candidates with the lowest number of votes and
        # highest number of votes
        # there might be a better way to do this
        # TODO optimize
        candidates_and_votes: List[List[str, int]] = [
            [candidate.id, candidate.votes] for candidate in self.candidates
        ]
        # sort this list by the number of votes
        candidates_and_votes.sort(key=lambda x: x[1])

        # find the number of candidates with the lowest number of votes
        lowest_votes_candidate: Candidate = candidates_and_votes[0]
        highest_votes_candidate: Candidate = candidates_and_votes[-1]

        # return the required IDs
        return (lowest_votes_candidate.id, highest_votes_candidate.id)

    def add_vote_to_candidate(self, candidate_id: str) -> None:
        # add a vote to the candidate by ID
        try:
            candidate: Candidate = self.candidates[candidate_id]
            candidate.addVote()
        except KeyError:
            print(f"Candidate with ID {candidate_id} does not exist")
            exit()

    def eliminate_candidate(self, candidate_id: str) -> None:
        # eliminate a candidate by id
        try:
            candidate: Candidate = self.candidates[candidate_id]
            candidate.eliminate()
        except KeyError:
            print(f"Candidate with ID {candidate_id} does not exist")
            exit()

    def tabulate(self, candidate_id: str) -> None:
        # tabulate the election results

        for voter in self.voters:
            # parse the preferences of the voter until we find the first valid
            # (non-eliminated) candidate, who will be counted as the choice
            # break at the first candidate who isn't eliminated
            choice: Candidate = None
            # using for over while here as failing is easier, given we are
            # allowing voters to also have no choices
            for preference in voter.preferences_list:
                # set the current choice
                choice = preference
                if not preference.eliminated:
                    # since we have found a valid candidate, we break
                    break
                else:
                    # the hunt goes on
                    continue
            # register a vote for the candidate in Choice
            # sanity check for no votes registered
            if choice == None:
                print("no vote registered")
                pass
            else:
                choice.addVote()

        # find the candidates with max and min votes
        highest_votes_candidate_id: str
        lowest_votes_candidate_id: str
        (
            highest_votes_candidate_id,
            lowest_votes_candidate_id,
        ) = self.get_polar_candidates()

        # not checking for existance here as the origin of IDs is the single
        # source of truth for all the candidate data
        highest_votes_candidate: Candidate = self.candidates[highest_votes_candidate_id]
        lowest_votes_candidate: Candidate = self.candidates[lowest_votes_candidate_id]

        if highest_votes_candidate.votes >= self.majority:
            # this candidate has won
            this.winner = highest_votes_candidate
        else:
            # drop the lowest candidate
            self.eliminate_candidate(lowest_votes_candidate_id)
            print(f"Eliminated candidate {lowest_votes_candidate}")

    def run(self) -> Candidate:
        while not self.winner:
            self.tabulate()
        print(self.winner.name)
        return self.winner
