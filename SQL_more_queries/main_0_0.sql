-- Holberton: TV shows database dump
CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
USE hbtn_0d_tvshows;

-- Cədvəllər

CREATE TABLE IF NOT EXISTS tv_genres (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS tv_shows (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(256) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS tv_show_genres (
    show_id INT NOT NULL,
    genre_id INT NOT NULL,
    KEY (show_id),
    KEY (genre_id)
);

-- Məlumatların əlavə edilməsi

INSERT INTO tv_genres VALUES
(1,'Drama'),(2,'Mystery'),(3,'Adventure'),(4,'Fantasy'),
(5,'Comedy'),(6,'Crime'),(7,'Suspense'),(8,'Thriller');

INSERT INTO tv_shows VALUES
(1,'House'),(2,'Game of Thrones'),(3,'The Big Bang Theory'),
(4,'New Girl'),(5,'Silicon Valley'),(6,'Breaking Bad'),
(7,'Better Call Saul'),(8,'Dexter'),(9,'Homeland'),(10,'The Last Man on Earth');

INSERT INTO tv_show_genres VALUES
(1,1),(1,2),(2,3),(2,1),(2,4),(3,5),(4,5),(5,5),
(6,6),(6,1),(6,7),(6,8),(8,6),(8,1),(8,2),(8,7),
(8,8),(10,5),(10,1);
