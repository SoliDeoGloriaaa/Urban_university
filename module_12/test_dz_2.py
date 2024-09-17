import unittest
from dz_2_t import Runner, Tournament

class TournamentTest(unittest.TestCase):
    
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

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[max(results.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()
