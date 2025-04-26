from __future__ import annotations

import sqlite3

DB_PATH = 'text.db'


def create_db(DB_PATH: str):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    sql_user = """CREATE TABLE user(
    id integer primary key
    username TEXT
    password TEXT
    bio TEXT)
"""

    sql_tuit = """CREATE TABLE tuit(
    id INTEGER PRIMARY KEY
    content TEXT
    user_id INTEGER FOREING KEY
    retweet_from TEXT FOREING KEY)
"""


class User:
    con = sqlite3.connect(DB_PATH)
    con_rows = sqlite3.Row
    cur = con.cursor()

    def __init__(self, username: str, password: str, bio: str = '', user_id: int = 0):
        self.username = username
        self.password = password
        self.bio = bio
        self.user_id = user_id
        logged = True

    def save(self) -> None:
        pass

    def login(self, password: str) -> None:
        pass

    def tweet(self, content: str) -> Tweet:
        pass

    def retweet(self, tweet_id: int) -> Tweet:
        pass

    def tweets(self):
        pass


class Tweet:
    con_tweet = sqlite3.connect(DB_PATH)
    con_rows_tweet = sqlite3.Row
    cur = con_tweet.cursor()

    def __init__(self, content: str = '', retweet_from: int = 0, tweet_id: int = 0):
        self.content = content
        self.retweet_from = retweet_from
        self.tweet_id = tweet_id

    def is_retweet(self) -> bool:
        pass

    def content(self) -> str:
        pass

    def save(self, user: User) -> None:
        pass

    def __repr__(self):
        pass

    def from_db_row(cls, row: sqlite3.Row) -> Tweet:
        pass


class Twitter:
    con_twitter = sqlite3.connect(DB_PATH)
    con_rows_twitter = sqlite3.Row
    cur = con_twitter.cursor()

    def add_user(self, username: str, password: str, bio: str = '') -> User:
        pass

    def get_user(self, user_id: int) -> User:
        pass


class TwitterError:
    pass
