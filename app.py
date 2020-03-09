from flask import Flask, request, redirect, session, render_template
import tweepy
import os
import sys

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

CONSUMER_KEY = os.environ['API_KEY']
CONSUMER_SECRET = os.environ['API_SECRET_KEY']

@app.route('/')
def index():
    sys.stderr.write("*** root *** start ***\n")
    """ root ページの表示 """
    # 連携アプリ認証済みなら user の timeline を取得
    timeline = user_timeline()

    # templates/index.html を使ってレンダリング.
    return render_template('index.html', timeline=timeline)

@app.route('/twitter_auth', methods=['GET'])
def twitter_auth():
    redirect_url = ""
    """ 連携アプリ認証用URLにリダイレクト """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    try:
        # 連携アプリ認証用の URL を取得
        redirect_url = auth.get_authorization_url()
        # 認証後に必要な request_token を session に保存
        session['request_token'] = auth.request_token
    except Exception as ee:
        app.logger().warning(str(ee) + "\n")

    # リダイレクト
    sys.stderr.write("*** twitter_auth *** end ***\n")
    return redirect(redirect_url)

def user_timeline():
    """ user の timeline のリストを取得 """
    # request_token と oauth_verifier のチェック
    token = session.pop('request_token', None)
    verifier = request.args.get('oauth_verifier')
    if token is None or verifier is None:
        return False  # 未認証ならFalseを返す

    # tweepy でアプリのOAuth認証を行う
#
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    # Access token, Access token secret を取得.
    auth.request_token = token
    try:
        auth.get_access_token(verifier)
    except Exception as ee:
        app.logger().warning(str(ee))
        return {}

    # tweepy で Twitter API にアクセス
    api = tweepy.API(auth)

    # user の timeline 内のツイートのリストを最大20件取得して返す
    return api.user_timeline(count=20)
