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
* The Heroku CLI installed on your computer
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

Ok welcome back! Now lets run `brew install python3` in our terminal.

After that installs. CONGRATS!!! You can now work with Python3!

Now, if you are looking for a guide like this odds are you already know some python, and you are looking to just move on to the next level. However, I wanted to include these steps, because, with all the ways we can now work with code online (https://repl.it/languages, as an example, https://aws.amazon.com/cloud9/, as another), It is quite possible that some one may find this guide and not work on their own local machine.

With that in mind I included at least how to set up on your local machine. Now that, that is done. I am not going to do "Hello world" or anthing like that, I am moving forward at this point with the assumption you know at least some python.

Lets now create our project!

Access your terminal, and navigate to where you would like to create your app!

Once you are there lets create a folder to hold your project!

On a mac run `mkdir python_heroku_api` Now you can name this file what ever you like, it really does not matter. I chose the name just to keep things simple and apparent. I am going to try and when ever possible name things very simply to try and reduce possible confusion.

Lets now go into our new app root folder `cd python_heroku_api`

Ok, now lets create our main app file `touch app.py` will create a new python file for us to play with.

Now that we have a base directory and a file, lets set up our coding enviroment.

Lets start by getting our enviroment package.
Now python3 now includes pip by default,so we do not need to install that, (or should not need to)

We do however need to install pipenv. We are going to use Homebrew again, so in your terminal, inside of your root directory, run `brew install pipenv` 

If you do not want to use Homebrew you can run `pip3 install pipenv`

Now that we have pipenv, lets set it up for our project.

run `pipenv install` in the terminal.

We are now going to use pipenv to install all of the packages we will need for this program.

* `pipenv install psycopg2`  "Allows us to work with postgrsql"
* `pipenv install Flask-SQLAlchemy` "helps us work with python and connecting to our database"
* `pipenv install gunicorn` "Helps us connect to Heroku"
* `pipenv install Flask-Heroku` "Is our connection between Flask and our hosting platform heroku"

You will see we have a `Pipfile`, and a `Pipfile.lock` added to our program.

We can work with our enviroment by running `pipenv shell` in our terminal.

Now that we are within our enviroment, let start putting our project together.

We have our Project folder, and we have our app.py.

Now lets start putting some code into our app.py, insert the following code block. (I have added comments on what everything is doing, so take a few min to see what our code is doing.)

```
# We import the tools/libraries that we plan on using at the top of our file
# For now we are just importing flask.
from flask import Flask

# Setting up the connection to flask,
app = Flask(__name__)


# Set "homepage" route
@app.route('/')
def home():
    return "<h1>Welcome to my page!</h1>"

# Setting up the code that will allow our app to run, once we call the file.
# We could just put app.run() with no if statement, but this is considered a better practice. For more information here is a link, https://docs.python.org/3/library/__main__.html

if __name__ == '__main__':
    app.debug = True
    app.run()
```



(Starting pointfor next entry)







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



