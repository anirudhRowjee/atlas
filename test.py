import unittest

from modules.rcir import InstantRunoff, Candidate, Voter, CandidateManager, VoteManager, ElectionManager


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
        new_candidate = Candidate("sample_name")
        self.assertEqual(new_candidate.name, "sample_name")
        self.assertEqual(new_candidate.votes, 0)
        self.assertEqual(new_candidate.eliminated, False)

    def test_add_vote(self):
        """
        test that we are able to register a vote for a candidate
        """
        new_candidate = Candidate("john")
        new_candidate.add_vote()
        self.assertEqual(new_candidate.votes, 1)

        # test error handling
        with self.assertRaises(Exception):
            new_candidate.votes = -1
            new_candidate.add_vote()

    def test_eliminate(self):
        """
        test that we are able to eliminiate a candidate
        """
        new_candidate = Candidate("amy")
        new_candidate.eliminate()
        self.assertEqual(new_candidate.eliminated, True)

        with self.assertRaises(Exception):
            new_candidate.eliminate()


class CandidateManagerTests(unittest.TestCase):
    """
    Manager to manipulate Candidate Objects, instance to be passed as an
    argument to anything that needs data from it
    """

    def test_init(self):


class VoterTests(unittest.TestCase):
    """
    Base testing class for a Voter in an Instant Runoff Election

    Must Contain -
    1. Name
    2. Unique Identifier
    3. Array of Preferences
    """

    pass


class InstantRunoffTests(unittest.TestCase):
    """
    Base testing class for Ranked Choice Instant Runoff Module
    """

    pass


if __name__ == "__main__":
    unittest.main()
