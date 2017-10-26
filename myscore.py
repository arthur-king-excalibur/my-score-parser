import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# from ipdb import set_trace
import re
from time import sleep
from pprint import pprint


BASE_URL = 'http://www.myscore.ua'
TYPE_SPORT = '/soccer'
COUNTY = '/england'
LEAGE = '/league-one-2016-2017'
END = '/results/'
URL = BASE_URL + TYPE_SPORT + COUNTY + LEAGE + END


class Bot():
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.url = url
        self.navigate()
        self.load_script_data()

    def navigate(self):
        self.driver.get(self.url)

    def html_page_load_js(self):
        return self.driver.page_source

    def load_script_data(self):
        error = None
        xpath = (
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[7]/table/tbody/tr/td/a'
        )
        res = self.driver.find_element_by_xpath(xpath)
        while not error:
            try:
                res.click()
                sleep(1.5)
            except BaseException:
                error = True
                print('=' * 80)
                print('load script data')


def main():
    url = URL
    bot = Bot(url)
    # response = requests.get(url)
    response = str(bot.html_page_load_js())
    soup = BeautifulSoup(response, 'html.parser')

    match_ids = get_match_ids(soup)
    pprint(convert_match_ids_to_url(match_ids))

    return soup, bot 	# for debug
    # tornament_id = get_tornament_id(soup)
    # print(tornament_id)


def get_match_ids(soup):
    filter_list = soup.find_all('tr')

    regex = r'id="[0-9a-zA-Z_]*"'
    regex = re.compile(regex)

    def clear_data(data):
        if data:
            return data[0].split('"')[1][4:]

    result_list = []
    for i in filter_list:
        find_id = regex.findall(str(i))
        if find_id:
            result_list.append(clear_data(find_id))

    return result_list


def convert_match_ids_to_url(match_ids):
    # mask1 http://www.myscore.ua/match/ERvOvns4/#match-summary
    # mask2 http://www.myscore.ua/match/ERvOvns4/#odds-comparison;1x2-odds;full-time
    result_list = []

    for match_id in match_ids:

        url_1 = '{}/match/{}/#match-summary'.format(
            BASE_URL,
            match_id
        )

        url_2 = '{}/match/{}/#odds-comparison;1x2-odds;full-time'.format(
            BASE_URL,
            match_id
        )

        result_list.append((url_1, url_2))

    return result_list


# ------------ Not used! ----------------
def get_tornament_id(soup):
    full_table = soup.find_all('script', {'type': 'text/javascript'})
    search = "tournament_id = '"
    len_search = len(search)

    for i in full_table:
        i = str(i)
        x = i.find(search)
        if x != -1:
            res = i[x + len_search: x + len_search + 20]
            return res[: res.find("'")]



if __name__ == '__main__':
    main()
    # bot = Bot(URL)

    # set_trace()
    # https://duckduckgo.com/?q=beautify+html&t=lm&ia=answer
    # scrapy calback! scrapy hub - google?
    # print(dir(webdriver.Firefox))
    # pythex.org тестим регулярные выражения

    '''
    https://losst.ru/ustanovka-docker-na-ubuntu-16-04
    обязательно перед hello-world выполнить !!!
    sudo service docker stop
    sudo service docker start
    '''
