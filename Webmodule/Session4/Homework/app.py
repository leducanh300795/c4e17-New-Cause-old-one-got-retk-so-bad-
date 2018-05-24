from flask import *
import mlab
from module.service import Service
# from mongoengine import StringField,IntField,BooleanField,Document
from mongoengine import *
from module.user import *
from random import *
app = Flask(__name__)

app.secret_key = "A super damn sercet key"

mlab.connect()

@app.route('/deleteall')
def delete_all():
    Service.objects().delete()
    return "Service have been deleted"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    all_service = Service.objects()
    return render_template('search.html',
                            all_service = all_service)


@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service = all_service )




@app.route ('/login', methods= ["GET", "POST"])
def login():
    list_user=[]
    list_password=[]
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form ['Username']
        password = form ['Password']
        all_user = User.objects()
        for index, user in enumerate(all_user):
            a = user['idsignin']
            list_user.append(a)


        all_user_password = User.objects(idsignin=username)
        for index, user_password in enumerate(all_user_password):
            b= user_password['password']
            list_password.append(b)

        if username in list_user and password in list_password:
            session['loggedin'] = True
            return redirect(url_for('service'))
        else:
            return "Permission denied. Go away!!"

@app.route('/detail/<service_id>')
def detail_id(service_id):
    if "loggedin" in session:
        service = Service.objects.with_id(service_id)
        return render_template('detail.html', service = service )
    else:
        return redirect(url_for("login"))


@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

@app.route('/service')
def service():
    all_services = Service.objects()
    return render_template('service.html', all_services=all_services)

@app.route ('/logout')
def logout():
    if 'loggedin' in session:
        del session['loggedin']
        return redirect(url_for('service'))
    else:
        return render_template('logoutagain.html')


@app.route('/sign-in', methods = ["GET","POST"])
def signin():
    if request.method == "GET":
        return render_template('signin.html')
    elif request.method == "POST":
        form = request.form
        name = form['Name']
        email = form['Email']
        idsignin = form['Idsignin']
        password= form['Password']
        user = User(    name= name,
                        email = email,
                        idsignin = idsignin,
                        password= password)
        user.save()

        return redirect(url_for('login'))




if __name__ == '__main__':
  app.run( debug=True)
