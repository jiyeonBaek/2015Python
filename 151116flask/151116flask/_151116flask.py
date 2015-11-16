from flask import Flask,url_for,redirect
app = Flask(__name__)

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile : '+username

@app.route('/hello')
def hello_world():
    #return 'hello world!'
    return redirect(url_for('login'))

@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message_id : %d'%message_id

#with app.test_request_context():
#    print(url_for('get_profile',username='greenjoa'))

@app.route('/login')
def login():
    return 'login'

#@app.route('/profile/', methods=['POST','GET'])
#def profile(username=None):
#    error=None
#    if request.method == 'POST':
#        username = request.form['username']
#        email = request.form['email']
#        if not username and not email:
#            return add_profile(request.form)
#        else:
#            error = 'Invalide username or email'
#        return render_template('profile.html', error=error)


if __name__ == '__main__':    app.run()
    #app.debug=True #소스 변경과 디버거 제공 , 에러 원인 다 보여줌    #app.run(host="203.252.166.31")