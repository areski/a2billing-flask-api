from auth import auth
from app import app


@app.route('/')
def homepage():
    return 'Welcome to A2B Restful API!'


@app.route('/private/')
@auth.login_required
def private_view():
    # user = auth.get_logged_in_user()
    return 'This is private!'
