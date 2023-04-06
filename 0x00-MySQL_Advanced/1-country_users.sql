-- This script creates a table named "users" with four columns
-- id column is an integer, never null, autoincrement, and primary key
-- email column is a string (255 characters), never null and unique
-- name column is a string (255 characters)
-- country is an enumeration of countires("US", "CO", "TN"), never null default "US"

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
