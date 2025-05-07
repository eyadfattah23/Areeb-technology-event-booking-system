CREATE DATABASE IF NOT EXISTS areeb_event_sys_dev_db;

CREATE USER IF NOT EXISTS 'areeb_event_sys_dev'@'localhost' IDENTIFIED BY 'Areeb_event_sys_dev_pwd123';

GRANT ALL PRIVILEGES ON `areeb_event_sys_dev_db`.* TO 'areeb_event_sys_dev'@'localhost';

GRANT SELECT ON `performance_schema`.* TO 'areeb_event_sys_dev'@'localhost';

FLUSH PRIVILEGES;
