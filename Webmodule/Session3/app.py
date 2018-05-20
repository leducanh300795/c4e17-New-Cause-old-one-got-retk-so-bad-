from flask import Flask, render_template, redirect, url_for,request
import mlab
from module.service import Service
# from mongoengine import StringField,IntField,BooleanField,Document
from mongoengine import *
app = Flask(__name__)

mlab.connect()

# # design database
# #creat collection
# class Service(Document):
#     name = StringField()
#     yob = IntField()
#     gender = IntField()
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()
#
# service = Service(name= "Kiều Anh",
#                     yob= 1996,
#                     gender=0,
#                     height=163,
#                     phone="01236556789",
#                     address="Hai Bà Trưng - Hà Nội",
#                     status=True)
#
# service.save()
# service = Service(name= "Ngân Búng",
#                     yob= 1992,
#                     gender=1,
#                     height=165,
#                     phone="01236556789",
#                     address="Câu Giấy - Hà Nội",
#                     status=False)
#
# service.save()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g, yob__lte=2000, address__iexact= "Hà Nội")
    return render_template('search.html',
                            all_service = all_service)
# @app.route('/searchage/<age>')
# def search(age):
#     all_service = Service.objects(yob__lte)
#     return render_template('searchage.html',
#                             all_service = all_service)

# @app.route('/<id>')
# def searchid(id):
#     id_to_find = Service.objects.get(id=id)
#     return id_to_find


@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html'
         ,all_service = all_service )

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

@app.route('/new-service', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form ['yob']

        new_service = Service (name=name, yob= yob)
        new_service.save()
        # 2 dòng này dùng để lưu vào database
        return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run( debug=True)
