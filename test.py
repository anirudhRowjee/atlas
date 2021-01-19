import unittest

# from modules.rcir import InstantRunoff, Candidate, Voter, CandidateManager, VoteManager, ElectionManager


class CandidateTests(unittest.TestCase):
    """
    Base testing class for a Candidate in an Instant Runoff Election

    Must Contain -
    1. Name
    2. Votes
    3. Elimination Status
    """

    def test_init(self):
        """
        test that the Candidate class initializes correctly
        """
        pass

    def test_add_vote(self):
        """
        test that we are able to register a vote for a candidate
        """
        pass


    def test_eliminate(self):
        """
        test that we are able to eliminiate a candidate
        """
        pass





class VoterTests(unittest.TestCase):
    """
    Base testing class for a Voter in an Instant Runoff Election

    Must Contain -
    1. Name
    2. Unique Identifier
    3. Array of Preferences
    """

    pass


class ElectionTests(unittest.TestCase):
    """
    Base testing class for Ranked Choice Instant Runoff Module
    """

    pass


if __name__ == "__main__":
    unittest.main()
