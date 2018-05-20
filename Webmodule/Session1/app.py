from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
        "title" : "Thơ con cóc",
        "content" : "Bốn Câu trắc nghiệm còn sai. Thì tìm ra ai giữa bảy tỉ người",
        "author" : "Lê Đức Anh",
        "gender" : 0
        },
        {
        "title" : "Thơ con chó",
        "content" : "Vợ người bên ta những vào lúc khó khắn, sẵn sàng chặt đầu ta khi ta mắc sai lầm",
        "author" : "Lê Đức Anh",
        "gender" : 1
        },
        {
        "title" : "Thơ con cóc",
        "content" : "Bốn Câu trắc nghiệm còn sai. Thì tìm ra ai giữa bảy tỉ người",
        "author" : "Lê Đức Anh",
        "gender" : 0
        }
        ]

    return render_template("index.html", posts = posts)

@app.route('/c4e')
def sayhi():
    return "Hi C4E 17"

@app.route('/sayhi/<name>/<age>')
def sayhinextdoor(name,age):
    return "Hello {0}, you are {1} year olds ".format(name,age)

# @app.route('/sum/<a>/<b>')
# def sum(a,b):
#     c = a+b
#     return c

# @app.route('/add/<int_list:values>')
# def add(values):
#     return str(sum(values))

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return str(a+b)

if __name__ == '__main__':
  app.run(debug=True)
