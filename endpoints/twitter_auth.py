from flask import request, redirect
from services.twitter import get_auth_url

def get():
    return redirect(get_auth_url())
