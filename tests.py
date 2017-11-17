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

    def test_get_1_x_2_odds(self):
        res = get_1_x_2_odds(self.page_1_soup)
        self.assertEqual(res, {
            '1_x_2_odds': {
                '1': {'open_odd': '1.53', 'close_odd': '1.39'},
                '2': {'open_odd': '6.25', 'close_odd': '7.50'},
                'x': {'open_odd': '4.00', 'close_odd': '5.50'}
            }
        })

    def test_get_over_under_odds(self):
        res = get_over_under_odds(self.page_2_soup)
        self.assertEqual(res, {
            'over_under_odds': {
                'odds_ou_0_5': {'over': {'close_odd': '1.01', 'open_odd': '1.02'}, 'under': {'close_odd': '26.00', 'open_odd': '19.00'}},
                'odds_ou_1_5': {'over': {'close_odd': '1.10', 'open_odd': '1.12'}, 'under': {'close_odd': '7.00', 'open_odd': '6.00'}},
                'odds_ou_2_5': {'over': {'close_odd': '1.33', 'open_odd': '1.47'}, 'under': {'close_odd': '3.39', 'open_odd': '2.60'}},
                'odds_ou_3_5': {'over': {'close_odd': '1.83', 'open_odd': '2.10'}, 'under': {'close_odd': '1.83', 'open_odd': '1.66'}},
                'odds_ou_4_5': {'over': {'close_odd': '2.75', 'open_odd': '3.75'}, 'under': {'close_odd': '1.39', 'open_odd': '1.25'}},
                'odds_ou_5_5': {'over': {'close_odd': '5.00', 'open_odd': '6.50'}, 'under': {'close_odd': '1.16', 'open_odd': '1.11'}}
            }
        })

    def test_get_asian_handicap_odds(self):
        res = get_asian_handicap_odds(self.page_2_soup)
        self.assertEqual(res, {
            'asian_handicaps': {
                    'odds_ah_-0_25': {'team1': {'close_odd': '1.60', 'open_odd': '1.60'},
                                       'team2': {'close_odd': '2.22', 'open_odd': '2.22'}},
                     'odds_ah_-0_5': {'team1': {'close_odd': '1.80', 'open_odd': '1.80'},
                                      'team2': {'close_odd': '1.91', 'open_odd': '1.87'}},
                     'odds_ah_-0_75': {'team1': {'close_odd': '1.83', 'open_odd': '2.05'},
                                       'team2': {'close_odd': '1.95', 'open_odd': '1.67'}},
                     'odds_ah_-1': {'team1': {'close_odd': '1.55', 'open_odd': '1.85'},
                                    'team2': {'close_odd': '2.37', 'open_odd': '1.95'}},
                     'odds_ah_-1_25': {'team1': {'close_odd': '1.75', 'open_odd': '2.07'},
                                       'team2': {'close_odd': '2.04', 'open_odd': '1.72'}},
                     'odds_ah_-1_5': {'team1': {'close_odd': '2.03', 'open_odd': '2.35'},
                                      'team2': {'close_odd': '1.90', 'open_odd': '1.57'}},
                     'odds_ah_-1_75': {'team1': {'close_odd': '2.14', 'open_odd': '2.67'},
                                       'team2': {'close_odd': '1.67', 'open_odd': '1.44'}},
                     'odds_ah_-2': {'team1': {'close_odd': '2.50', 'open_odd': '3.45'},
                                    'team2': {'close_odd': '1.50', 'open_odd': '1.30'}},
                     'odds_ah_-2_25': {'team1': {'close_odd': '2.85', 'open_odd': '3.70'},
                                       'team2': {'close_odd': '1.39', 'open_odd': '1.26'}},
                     'odds_ah_-2_5': {'team1': {'close_odd': '3.10', 'open_odd': '4.09'},
                                      'team2': {'close_odd': '1.35', 'open_odd': '1.22'}},
                     'odds_ah_-2_75': {'team1': {'close_odd': '3.79', 'open_odd': '5.25'},
                                       'team2': {'close_odd': '1.25', 'open_odd': '1.15'}},
                     'odds_ah_-3': {'team1': {'close_odd': '5.25', 'open_odd': '7.00'},
                                    'team2': {'close_odd': '1.15', 'open_odd': '1.10'}},
                     'odds_ah_-3_25': {'team1': {'close_odd': '5.50', 'open_odd': '7.00'},
                                       'team2': {'close_odd': '1.14', 'open_odd': '1.10'}},
                     'odds_ah_-3_5': {'team1': {'close_odd': '5.90', 'open_odd': '5.90'},
                                      'team2': {'close_odd': '1.12', 'open_odd': '1.12'}},
                     'odds_ah_-3_75': {'team1': {'close_odd': '9.00', 'open_odd': '12.00'},
                                       'team2': {'close_odd': '1.09', 'open_odd': '1.06'}},
                     'odds_ah_-4': {'team1': {'close_odd': '9.50', 'open_odd': '9.70'},
                                    'team2': {'close_odd': '1.02', 'open_odd': '1.02'}},
                     'odds_ah_-4_5': {'team1': {'close_odd': '12.00', 'open_odd': '8.00'},
                                      'team2': {'close_odd': '1.03', 'open_odd': '1.05'}},
                     'odds_ah_0': {'team1': {'close_odd': '1.13', 'open_odd': '1.20'},
                                   'team2': {'close_odd': '5.75', 'open_odd': '4.25'}},
                     'odds_ah_0_25': {'team1': {'close_odd': '1.12', 'open_odd': '1.16'},
                                      'team2': {'close_odd': '6.00', 'open_odd': '5.00'}},
                     'odds_ah_0_5': {'team1': {'close_odd': '1.11', 'open_odd': '1.14'},
                                     'team2': {'close_odd': '6.59', 'open_odd': '5.50'}},
                     'odds_ah_0_75': {'team1': {'close_odd': '1.10', 'open_odd': '1.10'},
                                      'team2': {'close_odd': '7.00', 'open_odd': '6.79'}},
                     'odds_ah_1': {'team1': {'close_odd': '1.02', 'open_odd': '1.07'},
                                   'team2': {'close_odd': '11.00', 'open_odd': '8.60'}},
                     'odds_ah_1_5': {'team1': {'close_odd': '1.03', 'open_odd': '1.05'},
                                     'team2': {'close_odd': '12.50', 'open_odd': '9.60'}}
            }
        })

if __name__ == '__main__':
    unittest.main()
