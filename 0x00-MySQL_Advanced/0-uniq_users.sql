-- This script creates a table named "users" with three columns
-- id column is an integer, never null, autoincrement and primary key
-- email column is a string (255 characters), never null and unique
-- name column is a string (255 characters)

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
