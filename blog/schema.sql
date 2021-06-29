DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
    user_id TEXT PRIMARY KEY,
    user_pw TEXT NOT NULL
);

CREATE TABLE post (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    repository TEXT NOT NULL,
    content TEXT NOT NULL,
    date DATETIME NOT NULL,
    writer TEXT NOT NULL,
    FOREIGN KEY (writer) REFERENCES user(user_id)
);

