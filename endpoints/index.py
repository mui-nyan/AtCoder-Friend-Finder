from flask import request, render_template, session,redirect
from services.twitter import verify, authorized

def get():

    if verify():
        return redirect("/")

    return render_template('index.html', authorized=authorized())
