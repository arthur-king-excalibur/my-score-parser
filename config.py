import os

DOMAIN = 'http://www.myscore.ua'
TYPE_SPORT = '/soccer'
COUNTY = '/england'
LEAGE = '/league-one-2014-2015'
END = '/results/'
START_URL = DOMAIN + TYPE_SPORT + COUNTY + LEAGE + END

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_NAME = 'PARSER'

if __name__ == '__main__':
    print(BASE_DIR)
