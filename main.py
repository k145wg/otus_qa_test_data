import json
from csv import reader


def gen_book(books):
    for book in books:
        yield book


def gen_user(users):
    user_count = len(users)
    index = -1
    while True:
        index += 1
        yield users[index % user_count]


if __name__ == '__main__':
    with open("src_data/users.json", "r") as f:
        users = json.loads(f.read())
    new_users = [
        {"name": user["name"], "gender": user["gender"], "address": user["address"], "age": user["age"], "books": []}
        for user in users]

    with open('src_data/books.csv', mode='r') as f:
        reader = reader(f)
        next(reader, None)
        header = {"title", "author", "pages", "genre"}
        books = [dict(zip(header, [row[0], row[1], row[3], row[2]])) for row in reader]

    generator = gen_user(new_users)
    for book in books:
        user = (next(generator))['books'].append(book)

    with open("result.json", "w") as f:
        s = json.dumps(new_users, indent=4)
