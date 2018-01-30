import csv

from models import get_football_data, get_db


def write_f(name, rows):
    with open(name, 'w', newline='') as f:
        fieldnames = ['home_team', 'away_team', 'time_match', 'OH', 'OD', 'OA', 'CH', 'CD', 'CA']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=' ')

        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def dict_to_row(dict_):
    row = {
            'home_team': dict_['team_names']['home_team'],
            'away_team': dict_['team_names']['away_team'],
            'time_match': dict_['time_match'],
            'OH': dict_['1_x_2_odds']['1']['open_odd'],
            'OD': dict_['1_x_2_odds']['x']['open_odd'],
            'OA': dict_['1_x_2_odds']['2']['open_odd'],
            'CH': dict_['1_x_2_odds']['1']['close_odd'],
            'CD': dict_['1_x_2_odds']['x']['close_odd'],
            'CA': dict_['1_x_2_odds']['2']['close_odd'],            
    }
    return row

def write_time(fname, list_):
    with open(fname, 'w') as f:
        fieldnames = ['time_goal', 'own_goal']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=' ')

        writer.writeheader()
        for row in list_:
            writer.writerow(row)


# no used
def flattenjson( b, delim ):
    # to flat dict
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i], delim )
            for j in get.keys():
                val[ i + delim + j ] = get[j]
        else:
            val[i] = b[i]
    # print(val.keys())
    return val


def main():
    db = get_db()
    data = get_football_data(db)
    time_list = event_print(data)
    write_time('time.csv', time_list)
    # rows = [dict_to_row(i) for i in data]
    # print(rows)
    # write_f('test.csv', rows)


def event_print(query):
    # map(lambda x: print(x[field]), query)
    result = []
    for k,i in enumerate(query):
        for j in i['events']:
            # print(j)
            if 'goal' in j.keys():
                result.append({
                    'time_goal': j['goal']['time'],
                    'own_goal': j['goal']['own_goal'],
                    })
    # result = [i.replace("'", "") for i in result]
    print(k)
    return result




if __name__ == '__main__':
    main()

    # print(data)
    # db = get_db()
    # get_football_data(db)