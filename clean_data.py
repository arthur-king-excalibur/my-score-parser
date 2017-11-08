import re
from functools import reduce


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


def get_test_data(name):
    with open(name) as f:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(f.read(), 'html.parser')
        return soup


def get_time_macth(soup):
    pass


def get_name_lig(soup):
    name_lig = soup.find('div', {'class': 'fleft'}).text
    regex = re.compile(r'[А-яіІ:0-9-^ ]+')
    str_name_lig = str(reduce(lambda x, y: x + y, regex.findall(name_lig)))

    country = str_name_lig.split(':')[0]
    leage = str_name_lig.split(':')[1].split('-')[0].strip()
    round_ = str_name_lig.split(':')[1].split('-')[1].strip()

    return country, leage, round_


def get_team_name(soup):
    names = soup.find_all('span', {'class': 'tname'})
    return [name.text.strip() for name in names]


def get_match_live_event(soup):
    # results is table with live event
    results = soup.find('table', {'id': 'parts'}).find_all('div', {'class': 'wrapper'})

    def find_event(key):
        '''main parse func live event'''
        res = result.find('div', {'class': key})
        if res:
            res = res.find_parent()
            event_time = res.find(
                'div',
                {'class': re.compile(r'time-box[-a-z]*')}
            )
            event_time = event_time.text.replace("\\'", '')
            name = res.find('span', {'class': 'participant-name'}).find('a').text

            return event_time, name

    key_goal = 'icon-box soccer-ball'
    key_own_goal = 'icon-box soccer-ball-own'
    key_yellow_card = re.compile(r'y.?-card+')
    key_red_card = 'icon-box r-card'
    key_penalty_missed = 'icon-box penalty-missed'

    def check_team():
        team1 = True
        team2 = False
        if not i % 2 == 0:
            team1 = False
            team2 = True
        return team1, team2

    events, event = [], None
    for i, result in enumerate(results):
        if find_event(key_goal):
            event = {
                'goal': {
                    'time': find_event(key_goal)[0],
                    'own_goal': False,
                    'name': find_event(key_goal)[1],
                    'team1': check_team()[0],
                    'team2': check_team()[1]
                }
            }

        elif find_event(key_own_goal):
            event = {
                'goal': {
                    'time': find_event(key_own_goal)[0],
                    'own_goal': True,
                    'name': find_event(key_own_goal)[1],
                    'team1': check_team()[0],
                    'team2': check_team()[1]
                }
            }

        elif find_event(key_yellow_card):
            event = {
                'card': {
                    'time': find_event(key_yellow_card)[0],
                    'type': 'yellow',
                    'name': find_event(key_yellow_card)[1],
                    'team1': check_team()[0],
                    'team2': check_team()[1]
                }
            }

        elif find_event(key_red_card):
            event = {
                'card': {
                    'time': find_event(key_red_card)[0],
                    'type': 'red',
                    'name': find_event(key_red_card)[1],
                    'team1': check_team()[0],
                    'team2': check_team()[1]
                }
            }

        else:
            event = None

        if event:
            events.append(event)

    return events

    # {'event': {
    #     'goal': {
    #         'time': 72,
    #         'own_goal': True,
    #         'is_penalty': False,
    #         'name': 'NAME',
    #         'team1': True,
    #         'team2': False}
    #     'card': {
    #         'type': 'yellow'
    #         'time': 33,
    #         'name': 'NAME',
    #         'team1': True,
    #         'team2': False}
    #     }
    # }

# https://www.myscore.ua/match/dA8vrGYR/#match-summary
# https://www.myscore.ua/match/ruM6bx0E/#match-summary - автогол
# https://www.myscore.ua/match/EoqJGsfr/#match-summary - не реализованный пеналь
# https://www.myscore.ua/match/4Yrkjlp8/#match-summary - красная карточка

def get_1_x_2_odds(soup):
    odds = soup.find_all('span', {'class': 'odds-wrap'})
    regex = re.compile(r'[0-9.]+')
    key = ['1', 'x', '2']
    odds_list = []

    for odd in odds:
        res = odd.get('eu')
        if res:
            res = regex.findall(res)    # -> ['2.05', '1.95']
            if len(res) == 2:
                res = {
                    'open_odd': res[0],
                    'close_odd': res[1]
                }
            else:
                res = {
                    'open_odd': res[0],
                    'close_odd': res[0]
                }

            odds_list.append(res)

    return dict(zip(key, odds_list))

if __name__ == '__main__':

    soups = [
        get_test_data('summary_test.html'),
        get_test_data('summary_test1.html'),
    ]
    # get_name_lig(soup)
    for soup in soups:
        print(get_match_live_event(soup))
        get_1_x_2_odds(soup)
        print('~' * 80)

    # from ipdb import set_trace; set_trace()
