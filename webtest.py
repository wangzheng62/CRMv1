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
@app.route('/getform',methods=["get","post"])
def getform():
    a=request.form
    l=Product(**a)
    print(l.info)
    if l.save():
        flash("提交成功")
    else:
        flash("提交失败")
    return redirect(url_for("form01"))
@app.route('/search',methods=["get","post"])
def search():
    a=request.form
    l=Product(**a)
    res=l.search()
    names=l.colnames()
    if res==[]:
        flash('没有查到结果')
    res.insert(0,names)
    return render_template('search01.html',formdata=names, listdata=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

