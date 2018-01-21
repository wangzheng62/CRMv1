from flask import Flask,redirect,url_for,render_template,request,flash
from func import DBserver,Crm,Product,Orderlist,Employee,Customer

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
#客户页功能
@app.route('/customeradd')
def customeradd():
    res=Customer.desc()
    print(res)
    return render_template('customermain.html',addform=res,bindurl="addcustomer")
@app.route('/addcustomer',methods=["post"])
def addcustomer():
    res=request.form.to_dict()
    print(res)
    res["__employee_Id"]="123"
    l=Customer(**res)
    l.save()
    return  render_template('customermain.html')
@app.route('/customersearch')
def customersearch():
    res=Customer.fetchall()
    res.insert(0,Customer.colnames())
    return render_template('customermain.html',addlist=res)


    return  render_template('customermain.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

