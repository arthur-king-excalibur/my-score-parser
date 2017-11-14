import os

DOMAIN = 'http://www.myscore.ua'
TYPE_SPORT = '/soccer'
COUNTY = '/england'
LEAGE = '/league-one-2014-2015'
END = '/results/'
# START_URL = DOMAIN + TYPE_SPORT + COUNTY + LEAGE + END
START_URL = 'https://www.myscore.ua/soccer/england/premier-league-2015-2016/results/'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALL_PROJECT_DIR = 'projects/'
PROJECT_NAME = ALL_PROJECT_DIR + 'premier_league_2015_2016'

if __name__ == '__main__':
    print(BASE_DIR)
