import unittest
from dz_2_t import Runner, Tournament

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)
        print(self.all_results)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[max(results.keys())] == "Ник")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj = Runner('Васёк')
        for _ in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)
    
    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj = Runner('Санёк')
        for _ in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)
    
    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challange(self):
        obj_1 = Runner('Аля')
        obj_2 = Runner('Абдурозик')
        
        for _ in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)
        
        
class TestSuite:
    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
        self.suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = TestSuite()
    runner.run(test_suite.suite)
