from flask import Flask,redirect,url_for,render_template,request,flash
from func import DBserver,Crm,Product

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html',welcome="欢迎来到crm软件")
@app.route('/customermain')
def customermain():
    return render_template('customermain.html')
@app.route('/ordermain')
def ordermain():
    return render_template('ordermain.html')
@app.route('/prouductmain')
def prouductmain():
    return render_template('prouductmain.html')
@app.route('/employeemain')
def employeemain():
    return render_template('employeemain.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

