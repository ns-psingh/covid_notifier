import covid_data as cd
import unittest

class TestCovid(unittest.TestCase):
    """ Class to test covid class """

    def setUp(self):
        self.cd = cd.CovidData()

    def test_retreive(self):
        self.cd.retreive()