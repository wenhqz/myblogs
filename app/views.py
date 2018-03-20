from flask import render_template,flash,redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname' : 'xxx' }
	posts = [
		{
			'author' : {'nickname' : "yyy"},
			'body' : "哈哈哈哈哈哈哈"
		},
		{
			'author' : {'nickname' : "lll"},
			'body' : "呜啦啦啦啦啦啦啦啦"
		}
	]
	return render_template("index.html" , title = 'Home' , user = user , posts = posts)

@app.route('/login',methods = ['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data + '",remember_me' + str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html',title = '登录' , form = form , providers = app.config['OPENID_PROVIDERS'])