from selenium import webdriver
from time import sleep
from random import choice

from src.general import (
    create_project_dir,
    create_data_files,
    param_change_agent,
)
from src.log import logger


class Bot():

    COUNT = 0
    start_url = ''
    queue_file = ''
    crawled_file = ''
    restore_file = ''
    queue = ''
    crawled = ''

    def __init__(self, start_url, project_name):
        self.driver = self.setup_bot()
        self.start_url = start_url

        Bot.COUNT = Bot.COUNT + 1
        self.BOT_NAME = 'BOT_NAME_{}'.format(Bot.COUNT)

        Bot.start_url = start_url
        Bot.project_name = project_name
        Bot.queue_file = '{}{}'.format(Bot.project_name, '/queue.txt')
        Bot.crawled_file = '{}{}'.format(Bot.project_name, '/crawled.txt')
        Bot.restore_file = '{}{}'.format(Bot.project_name, '/restore.txt')

        self.boot()

    def __repr__(self):
        return 'Bot number: {}'.format(Bot.COUNT)

    def setup_bot(self):

        user_agents, resolutions = param_change_agent()
        resolutions = [
            list(map(lambda x: int(x), i.split(','))) for i in resolutions
        ]
        profile = webdriver.FirefoxProfile()
        profile.set_preference(
            'general.useragent.override',
            choice(user_agents)
        )
        driver = webdriver.Firefox(profile)
        driver.set_window_size(*choice(resolutions))

        return driver

    def start_bot(self):
        self.driver.get(self.start_url)
        self.load_script_data()
        return self.html_page_load_js()

    def load_script_data(self):
        error = None
        xpath = (
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[7]/table/tbody/tr/td/a'
        )
        res = self.driver.find_element_by_xpath(xpath)
        while not error:
            try:
                res.click()
                sleep(1)
            except BaseException:
                logger.exception('i know about it!')
                error = True
                logger.debug('load script data')

    def html_page_load_js(self):
        sleep(1)
        return self.driver.page_source

    @staticmethod
    def boot():
        create_project_dir(Bot.project_name)
        create_data_files(Bot.project_name)

    def crawl_page(self, url):
        self.driver.get(url)
        sleep(1.5)
        return self.driver.page_source

    def turn_off_bot(self):
        self.driver.quit()

    # The other way of creating bot
    @classmethod
    def new_bot(cls):
        return cls(Bot.start_url, Bot.project_name)
