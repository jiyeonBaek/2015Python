from flask import Flask,url_for,redirect,render_template

app = Flask(__name__)

@app.route('/hello/')
#@app.route('/hello/<name>') # 경로 여러개에 함수 하나 매핑 가능
def hello():
    #return render_template('hello.html', name=name)
    data = [dict(href="http://www.naver.com",caption="네이버"), dict(href="http://www.google.com",caption="구글")]
    return render_template('hello.html',items=data)

@app.route('/')
def hello_world():
    data={
        'title' : 'Hello',
        'name' : 'greenjoa'
        }
    return render_template('first.html', **data)

@app.route('/main/')
def callMain():
    return render_template('main.html')

if __name__ == '__main__':
    app.debug=True
    app.run()