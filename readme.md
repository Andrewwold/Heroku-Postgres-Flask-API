
install postgresql
(create desired database)

install pip3,

pip3 install virtualenv

virtualenv venv (to start virtual enviroment)


mkdir static
mkdir templates
touch app.py
touch .gitignore


pip3 install Flask
pip3 install psycopg2
pip3 install Flask-SQLAlchemy



to create database 

python
>>> from app import db
>>> db.create_all()
>>> exit()