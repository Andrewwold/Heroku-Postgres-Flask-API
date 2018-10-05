# So We are going to create a Simple API using postgresql and host it on heroku.
All it is going to "Currently" do is let a user collect an email through a form, and provide an endpoint that will return those emails as a JSON object.

##### (This is an ongoing app, and will continue to develop more sections and build outs, my goal is to provide not just the code, but a clear walk through on how to create this on your own)

##### To that end I have included documentation links to all of the packages that will be used here. I encourage anyone that finds this walkthrough to also research the docs to understand more about what they are using and how to make it do what they need it to do.

Packages and software you will need with this app.

* postgresql (currently working with the mac postgres app.)
	https://www.postgresql.org/docs/
* pipenv
	https://pipenv.readthedocs.io/en/latest/
* pip3
	https://pip.pypa.io/en/stable/
* python 3.7
	https://docs.python.org/3/
* Flask
	http://flask.pocoo.org/docs/1.0/
* psycopg2
	http://initd.org/psycopg/docs/
* Flask-SQLAlchemy
	http://flask-sqlalchemy.pocoo.org/2.3/
* A Heroku Account
	https://devcenter.heroku.com/categories/reference
* gunicorn
	http://docs.gunicorn.org/en/stable/index.html
* Flask-Heroku
	(can not seem to find any docs I really like on this... It works with flask and heroku to help with hosting.)

## I recomend installing a virtual enviroment to help control your pip3 files etc. Though not technicaly a nessesity it is a good practice to isolate enviroments in my opinion, and so I will walk through how to do so on this app.

Lets first install python3.

* First here is the link to install python 3.7 https://www.python.org/downloads/

#### I am going to walk through how to install on a mac, but if you are working on a pc, or other os, etc, feel free to use the link, install, and then come back.

I am going to install python using Homebrew, (https://brew.sh/).

Before we install Homebrew we have to have install Apple's Xcode, if you do not have it already.

run `xcode-select --install` in your terminal, in may take a while to install.

So to get Homebrew I will go to the link and I will run the link they provide in my terminal.
 `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
 Above command is the one from the Hombrew site copied on OCT, 4th 2018.

Get Homebrew installed and we will continue!....

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



