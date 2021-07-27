#Bryan Prichard's HTTPS server
#Useful Link https://stackoverflow.com/questions/32237379/python-flask-redirect-to-https-from-http

from flask import request, redirect

@app.before_request
def before_request():
    if app.env == "developement":
        return
    if request.is_secure:
        return

    url = request.url.replace("http://", "https://", 1)
    code = 301
    return redirect(url, code=code)