from selenium import webdriver

from time import sleep


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
                sleep(0.5)
            except BaseException:
                error = True
                print('=' * 80)
                print('load script data')

    def go_next(self, url):
        self.driver.get(url)
        sleep(0.5)
        return self.driver.page_source