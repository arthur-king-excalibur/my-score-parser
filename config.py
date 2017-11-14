import os

DOMAIN = 'http://www.myscore.ua'
TYPE_SPORT = '/soccer'
COUNTY = '/england'
LEAGE = '/league-one-2014-2015'
END = '/results/'
# START_URL = DOMAIN + TYPE_SPORT + COUNTY + LEAGE + END
START_URL = 'https://www.myscore.ua/soccer/england/premier-league-2016-2017/results/'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_NAME = 'premier_league_2016_2017'

if __name__ == '__main__':
    print(BASE_DIR)
