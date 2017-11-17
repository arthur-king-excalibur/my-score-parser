import unittest
from src.clean_data import *


class Test_clean_data(unittest.TestCase):

    def setUp(self):
        with open('test/match_1_page_1.html') as f:
            self.page_1 = f.read()
        with open('test/match_1_page_2.html') as f:
            self.page_2 = f.read()

        from bs4 import BeautifulSoup
        self.page_1_soup = BeautifulSoup(self.page_1, 'html.parser')
        self.page_2_soup = BeautifulSoup(self.page_2, 'html.parser')

    def tearDown(self):
        pass

    def test_get_time_match(self):
        import datetime
        res = get_time_match(self.page_1_soup)
        self.assertEqual(res, {'time_match': datetime.datetime(2017, 11, 5, 16, 15)})

    def test_get_name_league(self):
        res = get_name_league(self.page_1_soup)
        self.assertEqual(res, {
            'league': {
                'league_name': "Прем'єр-ліга",
                'round': 'Раунд 11',
                'country': 'АНГЛІЯ'}
        })

    def test_get_team_name(self):
        res = get_team_name(self.page_1_soup)
        self.assertEqual(res, {
            'team_names': {
                'away_team': 'Арсенал',
                'home_team': 'Манчестер Сіті'}
        })

if __name__ == '__main__':
    unittest.main()
