DROP TABLE IF EXISTS post;

CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    repository TEXT NOT NULL,
    content TEXT NOT NULL,
    date DATETIME NOT NULL
);