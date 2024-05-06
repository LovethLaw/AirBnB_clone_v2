-- creating a dabase setup for testing
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

USE mysql; -- Switch to the mysql system database

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
