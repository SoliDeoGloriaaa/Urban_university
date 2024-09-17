import unittest
import logging
from dz_4 import Runner

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info('Логирование настроено успешно.')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            obj = Runner('Васёк', -5)  # Передаем отрицательное значение
            for _ in range(10):
                obj.walk()
            self.assertEqual(obj.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner: %s", err)

    def test_run(self):
        try:
            obj = Runner(123)  # Передаем число вместо строки
            for _ in range(10):
                obj.run()
            self.assertEqual(obj.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner: %s", err)

    def test_challange(self):
        obj_1 = Runner('Аля')
        obj_2 = Runner('Абдурозик')

        for _ in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)


if __name__ == '__main__':
    unittest.main()
