from runner_and_tournament import Runner, Tournament
import unittest
from pprint import pprint


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = []

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    def test_tournament1(self):
        tt = Tournament(90, self.runner1, self.runner3)
        all_results.append(tt.start())

    def test_tournament2(self):
        tt = Tournament(90, self.runner2, self.runner3)
        all_results.append(tt.start())

    def test_tournament3(self):
        tt = Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results.append(tt.start())


    @classmethod
    def tearDownClass(cls):
        for test in all_results:
            print('{', end='')
            for key, value in test.items():
                print(f'{key}: {value}, ', end='')
            print('}')


if __name__ == '__main__':
    unittest.main()
