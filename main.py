from bs4 import BeautifulSoup

# imports from my files
from bot import Bot
from config import START_URL, PROJECT_NAME

from convert_data import *
from clean_data import *
from general import *
from models import get_db, insert_html_db


# ВРЕМЕННО
from pprint import pprint




def create_url_list(bot):

    response = str(bot.start_bot())

    soup = BeautifulSoup(response, 'html.parser')

    match_ids = get_match_ids(soup)
    pair_urls = convert_match_ids_to_url(match_ids)

    for pair in pair_urls:
        for url in pair:
            append_data_to_file(bot.queue_file, url)

    bot.queue = file_to_list(bot.queue_file)

    return soup, bot 	# for debug



def html_to_db(bot):
    print('BOT NUMBER: ', bot.COUNT)
    global x
    for _ in range(38):
        if x <= x_len:
            res = bot.crawl_page(bot.queue[x])
            res_1 = bot.crawl_page(bot.queue[x + 1])
            print(bot.queue[x])

            res = {'html': {
                'match-summary': res,
                'odds-comparison': res_1}
            }

            db = get_db()
            insert_html_db(db, res)
            print('{} успешно записанно в базу | выполнено {} %'.format(
                x, x / x_len * 100)
            )
            x += 2
        else:
            print('Все завершено успешно!')
            break
            # sys.exit
    return True


def create_new_bot(bot):
    bot.turn_off_bot()
    for _ in range(20):
        _bot = Bot.new_bot()
        print('------CREATE---BOT----')
        html_to_db(_bot)
        _bot.turn_off_bot()
        print('--------DIE----BOT----')
    return True


if __name__ == '__main__':
    bot = Bot(START_URL, PROJECT_NAME)
    # ss, bb = create_url_list(bot)

    # x, x_len = 1, len(bot.queue)
    # print('x_len: ', x_len)
    # create_new_bot(bot)

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
