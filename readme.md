#So We are going to create a Simple API using postgresql and host it on heroku.
All it is going to do is let a user collect an email through a form, and provide an endpoint that will return those emails as a JSON object.

(This is an ongoing app, and will continue to develop more sections and build outs, my goal is to provide not just the code, but a clear walk through on how to create this on your own)


install postgresql
(create desired database)

install pip3,

pip3 install virtualenv

virtualenv venv (to start virtual enviroment)


mkdir static
mkdir templates
touch app.py
touch .gitignore

create index.html and success.html inside of templets


pip3 install Flask
pip3 install psycopg2
pip3 install Flask-SQLAlchemy



to create database table

python
>>> from app import db
>>> db.create_all()
>>> exit()


Create Heroku acount and install heroku tool belt


touch Procfile
add (web: gunicorn app:app) to Procfile (do not add the parens)
touch requirements.txt



pip3 install gunicorn
pip3 install Flask-Heroku
pip3 freeze > requirements.txt


git init
git add .
git commit -m "initial commit"
heroku create name-of-your-app

git push heroku master

Add heroku add-on for postgresql database.

update data connection using your heroku data

add

commit

push back up to heroku

heroku run python
>>> from app import db
>>> db.create_all()
>>> exit()



