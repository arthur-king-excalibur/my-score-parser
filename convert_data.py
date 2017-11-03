from config import DOMAIN


def convert_match_ids_to_url(match_ids):
    # mask1 http://www.myscore.ua/match/ERvOvns4/#match-summary
    # mask2 http://www.myscore.ua/match/ERvOvns4/#odds-comparison;1x2-odds;full-time
    result_list = []

    for match_id in match_ids:

        url_1 = '{}/match/{}/#match-summary'.format(
            DOMAIN,
            match_id
        )

        url_2 = '{}/match/{}/#odds-comparison;1x2-odds;full-time'.format(
            DOMAIN,
            match_id
        )

        result_list.append((url_1, url_2))

    return result_list