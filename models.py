def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.PARSER
    return db


def insert_html_db(db, dict_):
    db.html.insert(dict_)


def get_html_db(db):
    for k, i in enumerate(db.html.find()):    # find_one
        print(i)
        print('*' * 80)
        print('*' * 80)
    print(k)

    return True


def delete_data_db(db):
    db.html.remove()


if __name__ == "__main__":

    db = get_db()
    # delete_data_db(db)
    print(get_html_db(db))
