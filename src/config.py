import os
import re

def get_current_project_folder(url):
    '''get name for current project folder from start url'''
    regex = re.compile(r'[a-z0-9]*-[0-9]*')

    return ''.join(regex.findall(url)).replace('-', '_')

# -------change param-------------
# mask 'https://www.myscore.ua/soccer/{some-info}/{some-info}/results/'
START_URL = 'https://www.myscore.ua/soccer/england/premier-league-2015-2016/results/'
DEMO_LEN = lambda x: x[:4]  # parse only 4 matches
BOT_LIVES = 50
CURRENT_PROJECT_FOLDER = get_current_project_folder(START_URL)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALL_PROJECT_DIR = 'projects'
PROJECT_NAME = os.path.join(ALL_PROJECT_DIR, CURRENT_PROJECT_FOLDER)


if __name__ == '__main__':
    print(BASE_DIR)
    print(PROJECT_NAME)
    print(get_current_project_folder(START_URL))