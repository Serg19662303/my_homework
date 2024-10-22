import logging
from rt_with_exceptions import Runner
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(levelname)s \ %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_list_walk = [5, -3, 10, 4, -16]
        for speed in test_list_walk:
            try:
                t = Runner('Jim', speed)
                t.walk()
                logging.info('"test_walk" выполнен успешно')
            except ValueError as err:
                logging.error('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        test_list_runner = [5, "Вася", "Федя", 4, "Ваня"]
        for name_runner in test_list_runner:
            try:
                t = Runner(name_runner, 5)
                t.run()
                logging.info('"test_run" выполнен успешно')
            except TypeError as err:
                logging.error('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    unittest.main()
