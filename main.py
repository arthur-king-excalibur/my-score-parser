from bs4 import BeautifulSoup

# imports from my files
from bot import Bot
from config import START_URL, PROJECT_NAME

from convert_data import *
from clean_data import *
from general import *


# ВРЕМЕННО
from pprint import pprint

bot = Bot(START_URL, PROJECT_NAME)

def create_url_list(bot):

    response = str(bot.start_bot())

    soup = BeautifulSoup(response, 'html.parser')

    match_ids = get_match_ids(soup)
    pair_urls = convert_match_ids_to_url(match_ids)

    for pair in pair_urls:
        for url in pair:
            append_data_to_file(bot.queue_file, url)

    bot.queue = file_to_list(bot.queue_file)

    # pprint(convert_match_ids_to_url(match_ids))

    return soup, bot 	# for debug
    # tornament_id = get_tornament_id(soup)
    # print(tornament_id)

def get_html(soup, response):
    pass


if __name__ == '__main__':
    ss, bb = create_url_list(bot)
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

    with update = true

    user aget -> 1 bot 
    new crawl -> new random ip
    '''
