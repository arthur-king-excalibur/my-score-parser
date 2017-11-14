def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.PARSER
    return db


def insert_html_db(db, dict_):
    db.html.insert(dict_)


def get_football_data(db):
    from pprint import pprint
    for k, i in enumerate(db.football_data.find()):    # find_one
        pprint(i)
    print(k)

    return True


def delete_html_db(db):
    db.html.remove()


def insert_to_football_db(db, dict_):
    db.football_data.insert(dict_)


def delete_data_football_db(db):
    db.football_data.remove()

if __name__ == "__main__":

    db = get_db()
    # print(get_html_db(db))

    get_football_data(db)
    # delete_data_football_db(db)
