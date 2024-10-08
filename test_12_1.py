from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        t = Runner('objekt')
        for _ in range(10):
            t.walk()
        self.assertEqual(t.distance, 50)

    def test_run(self):
        t = Runner('objekt')
        for _ in range(10):
            t.run()
        self.assertEqual(t.distance, 100)

    def test_challenge(self):
        t1 = Runner('obj1')
        t2 = Runner('obj2')
        for _ in range(10):
            t1.run()
            t2.walk()
        self.assertNotEqual(t1.distance, t2.distance)