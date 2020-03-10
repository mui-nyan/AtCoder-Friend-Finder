from flask import request, session
import tweepy
import os
import logging

log = logging.getLogger("app")

CONSUMER_KEY = os.environ['API_KEY']
CONSUMER_SECRET = os.environ['API_SECRET_KEY']

IS_STUB = os.environ.get("STUB", None)

def get_auth_url():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth_url = auth.get_authorization_url()
    # 認証後に必要な request_token を session に保存
    session['request_token'] = auth.request_token
    return auth_url

def verify():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    token = session.pop('request_token', None)
    verifier = request.args.get('oauth_verifier', None)

    if token is None or verifier is None:
        log.info("token or verifier is None")
        return False

    auth.request_token = token

    try:
        auth.get_access_token(verifier)
        session['access_token'] = auth.access_token
        session['access_token_secret'] = auth.access_token_secret
    except Exception as e:
        log.warn(e)
        return False

    return True

def authorized():
    if "access_token" not in session or "access_token_secret" not in session:
        return False

    return True

def get_api():
    if "access_token" not in session or "access_token_secret" not in session:
        return False
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(session["access_token"], session["access_token_secret"])
    return tweepy.API(auth)

def get_user_timeline():
    """ user の timeline のリストを取得 """

    api = get_api()

    if not api:
        return False

    # user の timeline 内のツイートのリストを最大20件取得して返す
    return api.user_timeline(count=20)

def get_friend_users():
    api = get_api()

    if not api:
        return False

    friends_ids = []
    # フォローした人のIDを全取得
    # Cursor使うとすべて取ってきてくれるが,配列ではなくなるので配列に入れる
    for friend_id in tweepy.Cursor(api.friends_ids).items():
        friends_ids.append(friend_id)

    # 100IDsずつに詳細取得
    users = []
    for i in range(0, len(friends_ids), 100):
        for user in api.lookup_users(user_ids=friends_ids[i:i+100]):
            users.append({
                "id": user.screen_name,
                "name": user.name
            })

    users.sort(key=lambda user: user["id"])

    return users
