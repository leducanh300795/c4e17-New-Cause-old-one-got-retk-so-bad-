from flask import Flask, render_template,redirect

app = Flask(__name__)


@app.route('/aboutme')
def index():

    posts = [
            {
            "name" : " Lê Đức Anh",
            "work" : " Game mobile marketing at Funtap",
            "school" : " FTU",
            "hobbies" : " Poker",
            "dog" : " N/A"
            }
            ]

    return render_template("index2.html", posts = posts)



@app.route('/school')
def hello():
    return redirect("http://techkids.vn/", code=302)






if __name__ == '__main__':
    app.run(debug=True)
