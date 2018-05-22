def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.PARSER
    return db


def insert_html_db(db, dict_):
    db.html.insert(dict_)


def get_football_data(db):
    query = db.football_data.find()
    return query


def delete_html_db(db):
    db.html.remove()


def insert_to_football_db(db, dict_):
    db.football_data.insert(dict_)


def delete_data_football_db(db):
    db.football_data.remove()

if __name__ == "__main__":
    db = get_db()
