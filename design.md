
# Overview
 `Vote 50!?` is a web-based application developed with Python, HTML, CSS, and JavaScript. The main modules used to develop `Vote 50!?` is Flask (https://palletsprojects.com/p/flask/) and CS50 Library for Python (https://cs50.readthedocs.io/libraries/cs50/python/), while the database engine used in `Vote 50!?` is SQLite (https://www.sqlite.org/index.html). The application is free for use and is available in https://github.com/code50/148388805/tree/main/project.

Link to the video: https://youtu.be/kyvYevfsqpA?si=Ql3naQlcTd_W25Nm

# Database Schema
The database is designed to minimize data redundancy and maintain normalization rules. There are three main entities prepared : administrator, user, candidate, and counting vote. Foreign key constraint is used to keep the database integrity by ensuring the relationships between tables are preserved.

`administrator` table: to control the amount of voters, the counting vote and the candidates, referenced by the `id`.

    CREATE TABLE admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        );

`candidates` table: to store the candidates profiles in the voting. It is related to `user`, `admin` `election_result` and `votes`.

    CREATE TABLE candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        party TEXT NOT NULL,
        manifesto TEXT NOT NULL,
        image_url TEXT NOT NULL
        );

`users` table: to store voters account

    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
        );

`election_results_backup` table: to store the election result after a user voted

    CREATE TABLE election_results_backup (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        backup_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        results_data TEXT
        );

`votes` table: to process the counting vote.
    CREATE TABLE votes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        candidate_id INTEGER NOT NULL,
        has_voted INTEGER DEFAULT 0,
        is_backup INTEGER DEFAULT 0,
        UNIQUE(user_id, is_backup),
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE
        );


# Structure
![website structure](https://github.com/code50/148388805/tree/main/project)

All the assets and resources used in this application are located inside the `images` folder. Meanwhile `templates` keep all the HTML files which renders results returned by `app.py`.
The backbone of `Vote 50?` is in `app.py`, where records from the database are retrieved and modified, user inputs are processed, and results are rendered to the templates.
