from __future__ import annotations

import sqlite3

DB_PATH = 'twitter.db'


def create_db(db_path: str) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        bio TEXT
    );

    CREATE TABLE IF NOT EXISTS tweet (
        id INTEGER PRIMARY KEY,
        content TEXT,
        user_id INTEGER,
        retweet_from TEXT,
        FOREIGN KEY (user_id) REFERENCES user(id),
        FOREIGN KEY (retweet_from) REFERENCES user(username)
    )
    """

    cur.executescript(sql)

    con.commit()


class User:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, username: str, password: str, bio: str = '', user_id: int = 0):
        self.username = username
        self.password = password
        self.bio = bio
        self.user_id = user_id
        logged = True

    def save(self) -> None:
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute(
            'INSERT INTO user(id,username,password,bio) VALUES (?,?,?,?)',
            (self.user_id, self.username, self.password, self.bio),
        )
        con.commit()
        self.id = cur.lastrowid
        con.close()

    def login(self, password: str) -> None:
        con = sqlite3.connect(DB_PATH)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        sql = 'SELECT * FROM user WHERE username = ?'
        result = cur.execute(sql, (self.username,))
        row = result.fetchone()
        if row:
            if row['password'] == self.password:
                self.password = row['password']
                self.bio = row['bio']
                self.user_id = row['user_id']

    def tweet(self, content: str) -> Tweet:
        pass

    def retweet(self, tweet_id: int) -> Tweet:
        pass

    def tweets(self):
        pass


class Tweet:
    con = sqlite3.connect(DB_PATH)
    con_rows = sqlite3.Row
    cur = con.cursor()

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
    con = sqlite3.connect(DB_PATH)
    con_rows = sqlite3.Row
    cur = con.cursor()

    def add_user(self, username: str, password: str, bio: str = '') -> User:
        pass

    def get_user(self, user_id: int) -> User:
        pass


class TwitterError:
    pass
