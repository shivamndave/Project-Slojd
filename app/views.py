from flask import render_template, flash, redirect, Flask
from app import app
# from .forms import LoginForm
from random import randint
import sys
import glob
import errno
import os
import HaikuMod
import HaikuTest

# index view function suppressed for brevity

@app.route('/')
@app.route('/index')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for OpenID="%s", remember_me=%s' %
#               (form.openid.data, str(form.remember_me.data)))
#         return redirect('/index')
#     return render_template('login.html', 
#                            title='Sign In',
#                            form=form,
#                            providers=app.config['OPENID_PROVIDERS'])


# This is the index, the main page, you can specify what you want passed into the index html
def index():
	# This is sample for test
  user = {'nickname': 'yoFace'}  # fake user
  posts = [  # fake array of posts
      { 
          'author': {'nickname': 'John'}, 
          'body': 'Beautiful day in Portland!' 
      },
      { 
          'author': {'nickname': 'Susan'}, 
          'body': 'The Avengers movie was so cool!' 
      }
  ]
  blah = randomness(5)
  blah2 = HaikuTest.makeHaiku1()
  # Make sure all variables you want passed goes inside here!
  return render_template("index.html",
                         title='Home',
                         user=user,
                         posts=posts,
                         blah=blah,
                         blah2=blah2)

#This is another def that leads to another page, remember to specify the routes  
@app.route('/betterHaiku')
def betterHaiku():
  blah2 = HaikuTest.haikuType2()
  return render_template("betterHaiku.html",
                         title='Home',
                         blah2=blah2)

def randomness (n):
	line = ""
	while (n > 0):
		temp = randint(1, n)
		line = line + str(temp)
		n-=temp
	return line