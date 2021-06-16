DROP TABLE IF EXISTS home;
DROP TABLE IF EXISTS frontend;
DROP TABLE IF EXISTS backend;
DROP TABLE IF EXISTS devops;
DROP TABLE IF EXISTS cs;

CREATE TABLE home (
    home_id INTEGER PRIMARY KEY AUTOINCREMENT,
    repository TEXT NOT NULL
);

CREATE TABLE frontend (
    frontend_id INTEGER PRIMARY KEY AUTOINCREMENT,
    home_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    repository TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (home_id) REFERENCES home (home_id)
);

CREATE TABLE backend (
    backend_id INTEGER PRIMARY KEY AUTOINCREMENT,
    home_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    repository TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (home_id) REFERENCES home (home_id)
);

CREATE TABLE devops (
    devops_id INTEGER PRIMARY KEY AUTOINCREMENT,
    home_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    repository TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (home_id) REFERENCES home (home_id)
);

CREATE TABLE cs (
    cs_id INTEGER PRIMARY KEY AUTOINCREMENT,
    home_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    repository TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (home_id) REFERENCES home (home_id)
);
