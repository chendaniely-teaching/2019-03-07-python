sudo apt -y update
sudo apt -y upgrade
sudo apt install -y postgresql postgresql-contrib
sudo apt install -y apache2 php php-pgsql libapache2-mod-php phppgadmin pgadmin3
cd /var/www/html && wget -O index.php https://www.adminer.org/latest.php


# create postgres users
sudo -u postgres psql postgres
CREATE ROLE mck1 LOGIN PASSWORD 'mck123!';

# create databases
CREATE DATABASE class_database TEMPLATE = template0;
GRANT ALL PRIVILEGES ON DATABASE class_database TO dan;
GRANT ALL PRIVILEGES ON DATABASE class_database TO mck1;
