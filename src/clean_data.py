import re
from functools import reduce
from datetime import datetime

from src.log import logger


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


def get_test_data(name):
    with open(name) as f:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(f.read(), 'html.parser')
        return soup


def get_time_match(soup):
    str_time = soup.find('td', {'id': 'utime'}).text
    regex = re.compile(r'[0-9]+')
    list_int_time = list(map(lambda x: int(x), regex.findall(str_time)))

    time_ = datetime(
        year=list_int_time[2],
        month=list_int_time[1],
        day=list_int_time[0],
        hour=list_int_time[3],
        minute=list_int_time[4]
    )

    return {'time_match': time_}


def get_name_league(soup):
    name_leag = soup.find('div', {'class': 'fleft'}).text
    regex = re.compile(r"[А-яіІ'єЄ:0-9-^ ]*")
    str_name_lig = str(reduce(lambda x, y: x + y, regex.findall(name_leag)))
    country = str_name_lig.split(':')[0]
    league = str_name_lig.split(':')[1].split(' - ')[0].strip()
    round_ = str_name_lig.split(':')[1].split(' - ')[1].strip()

    return {'league': {
            'country': country,
            'league_name': league,
            'round': round_
                }
            }


def get_team_name(soup):
    names = soup.find_all('span', {'class': 'tname'})
    key_ = ['home_team', 'away_team']
    value_ = [name.text.strip() for name in names]
    return {'team_names': dict(zip(key_, value_))}


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

    return {'events': events}


def split_odds(result, regex=re.compile(r'[0-9.]+')):
    result = regex.findall(result)    # -> ['2.05', '1.95']

    try:
        if len(result) == 2:
            result = {
                'open_odd': result[0],
                'close_odd': result[1]
            }
        else:
            result = {
                'open_odd': result[0],
                'close_odd': result[0]
            }
    except IndexError as e:
        logger.exception('ERROR func split_odds {}'.format(e))
        result = {
            'open_odd': 'not_data',
            'close_odd': 'not_data'
        }

    return result


def get_1_x_2_odds(soup):
    odds = soup.find_all('span', {'class': 'odds-wrap'})
    key = ['1', 'x', '2']
    odds_list = []

    for odd in odds:
        res = odd.get('eu')
        if res:
            odds_list.append(split_odds(res))

    return {'1_x_2_odds': dict(zip(key, odds_list))}


def union_to_dict(update_dict_from_tupl):

    result_dict = {}
    for _dict in update_dict_from_tupl:
        result_dict.update(_dict)

    return result_dict


def get_over_under_odds(soup):

    full_table = soup.find('div', {'id': 'block-under-over-ft'})
    keys = ("odds_ou_{}".format(i / 10) for i in range(5, 65, 10))

    def find_odds_by_key(key, table):
        odds = table.find('table', {'id': key}).find('tbody').find('tr')
        odds_list = odds.find_all('span')

        result_list = []
        for odd in odds_list:
            res = odd.get('eu')
            if res:
                dict_ = split_odds(res)
                result_list.append(dict_)
        return dict(zip(('over', 'under'), result_list))
    # map(find_odds_by_key, keys)
    return {
        'over_under_odds': {key.replace('.', '_'): find_odds_by_key(key, full_table) for key in keys}
    }


def get_asian_handicap_odds(soup):
    list_table = soup.find_all('table', {'id': re.compile(r'odds_ah')})

    gen_key = (table.get('id').replace('.', '_') for table in list_table)
    # print(list(gen_key))

    # generator
    gen_doble_spans = (table.find('tr', {'class': 'odd'}).find_all(
        'span', {'class': re.compile(r'odds-wrap')}
    ) for table in list_table)

    # spans = ((i for i in d_span) for d_span in gen_doble_spans)
    # for d_span in spans:
    #     for i in d_span:
    #         print(i)

    def clean_d_span(doble_span):
        gen_span = (i for i in doble_span)

        def clean_span(span):
            span = span.get('eu')
            if span:
                dict_ = split_odds(span)
                # result_list.append(dict_)
            return dict_

        return dict(zip(('team1', 'team2'), map(clean_span, gen_span)))

    return {
        'asian_handicaps': dict(zip(gen_key, (map(clean_d_span, gen_doble_spans))))
    }


def union_parse_pages(soup_1_page, soup_2_page):

    update_tupl = (
        get_time_match(soup_1_page),
        get_name_league(soup_1_page),
        get_team_name(soup_1_page),
        get_match_live_event(soup_1_page),
        get_1_x_2_odds(soup_1_page),

        get_over_under_odds(soup_2_page),
        get_asian_handicap_odds(soup_2_page)
    )

    return union_to_dict(update_tupl)


if __name__ == '__main__':

    from pprint import pprint

    soup1 = get_test_data('test/match_1_page_1.html')
    soup2 = get_test_data('test/match_1_page_2.html')

    pprint(get_time_match(soup1))
    pprint(get_name_league(soup1))
