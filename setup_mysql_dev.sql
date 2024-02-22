-- Create project development database with the name `hbnb_dev_db`
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user `hbnb_dev` with the password `hbnb_dev_pwd` if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to the new user on the `hbnb_dev_db`
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Grant the SELECT privilege for the user `hbnb_dev` in the `performance_schema` database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges again to apply the changes
FLUSH PRIVILEGES;
