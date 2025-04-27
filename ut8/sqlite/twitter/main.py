from __future__ import annotations

import sqlite3

DB_PATH = 'twitter.db'
MAX_LENGHT_CHARS = 280


def create_db(db_path: str) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        self.logged = True

    def save(self) -> None:
        sql = 'INSERT INTO user(username, password, bio) VALUES (?, ?, ?)'
        User.cur.execute(
            sql,
            (self.username, self.password, self.bio),
        )
        User.con.commit()
        self.id = User.cur.lastrowid

    def login(self, password: str) -> None:
        sql = 'SELECT * FROM user WHERE username = ?, password = ?'
        result = User.cur.execute(sql, (self.username, password))
        row = result.fetchone()
        if row:
            if row['password'] == self.password:
                self.password = row['password']
                self.bio = row['bio']
                self.user_id = row['id']

    def tweet(self, content: str) -> Tweet:
        self.content = content
        if not self.logged:
            raise TwitterError(f'User {self.username} is not logged in')
        if len(self.content) > MAX_LENGHT_CHARS:
            raise TwitterError('Tweet has more than 280 chars!')
        new_tweet = Tweet(content=self.content, tweet_id=0, retweet_from=0)
        self.save(new_tweet)
        return new_tweet

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

    @property
    def content(self) -> str:
        pass

    def save(self, user: User) -> None:
        sql = 'INSERT INTO tweet(content, user_id, retweet_from) VALUES (?, ?, ?)'
        result = Tweet.cur.execute(sql, (self.content, self.tweet_id, self.retweet_from))
        row = result.fetchall

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


class TwitterError(Exception):
    pass
