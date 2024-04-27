# Download PostgreSQL if it isn't here and create user for DB

# sudo apt update
# sudo apt -y install postgresql-14

sudo -i -u postgres psql -c "createuser -s -d cs_labworks"
