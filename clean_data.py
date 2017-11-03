import re


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

# res = soup.find_all('span', {'class': 'odds-wrap'}) 
# for i in res: print(i.get('eu'))
