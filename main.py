from bs4 import BeautifulSoup

# imports from my files
from bot import Bot
from config import START_URL

from convert_data import *
from clean_data import *


# ВРЕМЕННО
from pprint import pprint


def main():
    url = START_URL
    bot = Bot(url)
    # response = requests.get(url)
    response = str(bot.html_page_load_js())
    soup = BeautifulSoup(response, 'html.parser')

    match_ids = get_match_ids(soup)
    pprint(convert_match_ids_to_url(match_ids)[:-5])

    return soup, bot 	# for debug
    # tornament_id = get_tornament_id(soup)
    # print(tornament_id)


if __name__ == '__main__':
    ss, bb = main()
    from bs4 import BeautifulSoup as bs

    from ipdb import set_trace; set_trace()

    # https://duckduckgo.com/?q=beautify+html&t=lm&ia=answer
    # scrapy calback! scrapy hub - google?
    # print(dir(webdriver.Firefox))
    # pythex.org тестим регулярные выражения
    # gekodirver cp /usr/local/bin
    # https://habrahabr.ru/post/235901/ sublime plugins

    '''
    https://losst.ru/ustanovka-docker-na-ubuntu-16-04
    обязательно перед hello-world выполнить !!!
    sudo service docker stop
    sudo service docker start
    '''