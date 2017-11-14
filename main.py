from bs4 import BeautifulSoup

# imports from my files
from src.bot import Bot
from src.config import START_URL, PROJECT_NAME
from src.clean_data import get_match_ids, union_parse_pages
from src.models import get_db, insert_html_db, insert_to_football_db
from src.log import logger

from src.general import *


def create_match_ids_list(bot):
    response = str(bot.start_bot())

    soup = BeautifulSoup(response, 'html.parser')

    bot.queue = get_match_ids(soup)

    return True


def get_soup(bot, url):
    response = bot.crawl_page(url)
    return BeautifulSoup(str(response), 'html.parser')


def url_mask(_id):
    mask = (
        'http://www.myscore.ua/match/{}/#match-summary'.format(_id),
        'http://www.myscore.ua/match/{}/#odds-comparison;1x2-odds;full-time'.format(_id)
    )
    return mask


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


def new_bot_soups(bot, _id):
    res = url_mask(_id)

    return (
        get_soup(bot, res[0]),
        get_soup(bot, res[1])
    )


def main(bot):

    NUM = bot.queue[:2]
    LEN_NUM = len(NUM)
    BOT_LIVES = 50
    logger.debug('all pair_urls:', LEN_NUM)

    try:
        for i, _id in enumerate(NUM):
            if i % BOT_LIVES == 0:
                logger.debug(bot)
                bot.turn_off_bot()
                logger.debug('DIE BOT')
                bot = Bot.new_bot()
                logger.debug('NEW {}'.format(bot))

            bot_soups = new_bot_soups(bot, _id)
            data_to_db = union_parse_pages(*bot_soups)
            data_to_db.update({'myscore_id': _id})
            append_data_to_file(bot.crawled_file, _id)

            logger.info('crawl_url: \n{}, \n{}'.format(*url_mask(_id)))
            logger.info('complite on: {} %'.format((i + 1) / LEN_NUM * 100))

            # write data to db
            db = get_db()
            insert_to_football_db(db, data_to_db)
            logger.info('data write to db')
        bot.turn_off_bot()
    except AttributeError as e:
        logger.exception(e)
        logger.info('error match_id:', _id)

        create_restore_file(
            path_queue_file=bot.queue_file,
            path_crawled_file=bot.crawled_file,
            path_restore_file=bot.restore_file
        )

        restore_main(bot)
    finally:
        create_restore_file(
            path_queue_file=bot.queue_file,
            path_crawled_file=bot.crawled_file,
            path_restore_file=bot.restore_file
        )


def restore_main(bot):
    global COUNT_RESTARTS
    COUNT_RESTARTS += 1
    logger.debug('restart:', COUNT_RESTARTS)
    bot.queue = file_to_list(bot.restore_file)
    main(bot)


if __name__ == '__main__':
    COUNT_RESTARTS = 0
    bot = Bot(START_URL, PROJECT_NAME)
    create_match_ids_list(bot)    # bot.queue '\/'
    append_list_to_file(bot.queue_file, bot.queue)   # write ids to file
    main(bot)
    # restore_main(bot)

    # from ipdb import set_trace; set_trace()

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
