from flask import Flask, request, redirect, session, render_template
import tweepy
import os
import sys
from endpoints import index as index_page
from endpoints import twitter_auth as twitter_auth_redirect

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

CONSUMER_KEY = os.environ['API_KEY']
CONSUMER_SECRET = os.environ['API_SECRET_KEY']

@app.route('/')
def index():
    return index_page.get()

@app.route('/twitter_auth', methods=['GET'])
def twitter_auth():
    return twitter_auth_redirect.get()
