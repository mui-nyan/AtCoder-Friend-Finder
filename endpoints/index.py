from flask import request, render_template, session
from services.twitter import get_friend_users, verify, authorized
from services.matching import matching
from repositories.atcoder_user import load_atcoder_users

def get():

    users = None

    if verify() or authorized():
        friends = get_friend_users()
        atcoder_users = list(load_atcoder_users())
        users = matching(friends, atcoder_users)

    return render_template('index.html', users=users, authorized=authorized())
