CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL NOT NULL PRIMARY KEY,
    user_name TEXT NOT NULL,
    age INT NOT NULL,
    gender TEXT NOT NULL,
    nationality TEXT NOT NULL
);