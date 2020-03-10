from flask import request, render_template, session,redirect
from services.twitter import get_friend_users, verify, authorized
from services.matching import matching
from repositories.atcoder_user import load_atcoder_users

def get():

    if verify():
        return redirect("/")

    return render_template('index.html', authorized=authorized())
