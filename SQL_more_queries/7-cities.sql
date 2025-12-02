-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use this database
USE hbtn_0d_usa;

-- Create cities table if not exists
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
