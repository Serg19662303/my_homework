from runner import Runner
from runner_and_tournament import Tournament, Runner1
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Временно не нужно тестировать')
    def test_walk(self):
        t = Runner('objekt')
        for _ in range(10):
            t.walk()
        self.assertEqual(t.distance, 50)

    @unittest.skipIf(is_frozen, 'Временно не нужно тестировать')
    def test_run(self):
        t = Runner('objekt')
        for _ in range(10):
            t.run()
        self.assertEqual(t.distance, 100)

    @unittest.skipIf(is_frozen, 'Временно не нужно тестировать')
    def test_challenge(self):
        t1 = Runner('obj1')
        t2 = Runner('obj2')
        for _ in range(10):
            t1.run()
            t2.walk()
        self.assertNotEqual(t1.distance, t2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = []

    def setUp(self):
        self.runner1 = Runner1('Усейн', 10)
        self.runner2 = Runner1('Андрей', 9)
        self.runner3 = Runner1('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        tt = Tournament(90, self.runner1, self.runner3)
        all_results.append(tt.start())

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        tt = Tournament(90, self.runner2, self.runner3)
        all_results.append(tt.start())

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        tt = Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results.append(tt.start())
