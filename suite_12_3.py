from unittest import TestSuite, TestLoader, TextTestRunner
from test_12_3 import RunnerTest, TournamentTest


testRunner = TestSuite()
testRunner.addTest(TestLoader().loadTestsFromTestCase(RunnerTest))
testRunner.addTest(TestLoader().loadTestsFromTestCase(TournamentTest))


runner = TextTestRunner(verbosity=2)
runner.run(testRunner)

