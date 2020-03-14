from flask import Flask, request, redirect, session, render_template, url_for
import tweepy
import os
import sys
from endpoints import index as index_page
from endpoints import twitter_auth as twitter_auth_redirect
from endpoints import find_friends as find_friends_api

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

CONSUMER_KEY = os.environ['API_KEY']
CONSUMER_SECRET = os.environ['API_SECRET_KEY']

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
def index():
    return index_page.get()

@app.route('/find_friends', methods=['GET'])
def find_friends():
    return find_friends_api.get()

@app.route('/twitter_auth', methods=['GET'])
def twitter_auth():
    return twitter_auth_redirect.get()

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))
