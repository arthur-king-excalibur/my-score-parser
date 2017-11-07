from selenium import webdriver
from time import sleep
from random import choice

from general import (
    create_project_dir,
    create_data_files,
    file_to_list,
    param_change_agent,
)

class Bot():

    COUNT = 0

    start_url = ''
    queue_file = ''
    crawled_file = ''
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

        self.boot()

    def setup_bot(self):
        # http://www.seleniumhq.org/docs/03_webdriver.jsp
        # http://www.seleniumhq.org/docs/04_webdriver_advanced.jsp
        # https://stackoverflow.com/questions/2887978/webdriver-and-proxy-server-for-firefox#5166310

        proxy, user_agents, resolutions = param_change_agent()
        resolutions = [
            list(map(lambda x: int(x), i.split(','))) for i in resolutions
        ]

        profile = webdriver.FirefoxProfile()
        profile.set_preference(
            "general.useragent.override",
            choice(user_agents)
        )

        # profile.set_preference("network.proxy.type", 1)
        # profile.set_preference("network.proxy.http", "85.90.199.59")
        # profile.set_preference("network.proxy.http_port", 53281)

        driver = webdriver.Firefox(profile)
        print(*choice(resolutions))

        driver.set_window_size( *choice(resolutions) )

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
                sleep(0.5)
            except BaseException:
                error = True
                print('=' * 80)
                print('load script data')


    def html_page_load_js(self):
        return self.driver.page_source

    @staticmethod
    def boot():
        create_project_dir(Bot.project_name)
        create_data_files(Bot.project_name, Bot.start_url)
        Bot.queue = file_to_list(Bot.queue_file)
        Bot.crawled = file_to_list(Bot.crawled_file)

    def crawl_page(self, url):
        self.driver.get(url)
        sleep(0.5)
        return self.driver.page_source

    def turn_off_bot(self):
        self.driver.quit()

    # Создание класа бот другим способом
    @classmethod
    def new_bot(cls):
        return cls(Bot.start_url, Bot.project_name)

# bb.crawl_page(bb,'http://www.myscore.ua/match/OxCVYego/#odds-comparison;1x2-odds;full-time')
