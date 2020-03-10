from flask import jsonify, abort
from services.twitter import get_friend_users, authorized
from services.matching import matching
from repositories.atcoder_user import load_atcoder_users

def get():

    if not authorized():
        abort(401, "Authorization Required.")

    twitter_friends = get_friend_users()
    atcoder_users = list(load_atcoder_users())
    users = matching(twitter_friends, atcoder_users)

    return jsonify({
        "size": len(users),
        "data": users
    })
