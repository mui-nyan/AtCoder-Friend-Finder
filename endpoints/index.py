from flask import request, render_template, session,redirect
from services.twitter import verify, authorized, i_am

def get():

    if verify():
        return redirect("/")

    screen_name = None
    auth = authorized()
    if auth:
        screen_name = i_am()


    return render_template('index.html', authorized=authorized(), screen_name=screen_name)
