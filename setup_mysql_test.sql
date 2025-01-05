-- Create a database if it doesn't exist
-- Create user 'test' with password
-- Grant the user all priviledges to the database
-- Grant SELECT priviledges on 'performance_schema' to e user
-- Apply changes made to the user privileges

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;