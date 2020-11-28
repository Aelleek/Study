import os
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template

from flask_wtf.csrf import CSRFProtect

app=Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():

    img = request.files('imgfile')

    print(request.files)

    return render_template('respage.html', resImg = img)

# /127.0.0.1 '/'
@app.route('/')
def hello():

    return render_template('mainpage.html')

if __name__ == "__main__":

    basedir=os.path.abspath(os.path.dirname(__file__))
    print('basedir:{}'.format(basedir))

    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SECRET_KEY']='dkssudgktpdy'  #임의의 문자열 넣는다.
    #
    # csrf = CSRFProtect()
    # csrf.init_app(app)

    app.run(host='127.0.0.1', port=5000, debug=True)




# @app.route('/login', methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['userid'] = form.data.get('userid')
#         print("login_sumit")
#         return redirect('/')
#
#     return render_template('login.html', form=form)

