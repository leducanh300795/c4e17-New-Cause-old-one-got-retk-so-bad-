from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<username>')
def index(username):
    Users = {
        "lda":{
            "name":"Le Duc Anh",
            "age":23,
            "status":"Single",
            "hobbies":"Game"
        },
        "tung":{
            "name":"Tung",
            "age":20,
            "status":"Single",
            "hobbies":"Cloning"
        },
        "powerman":{
            "name":"Power man",
            "age":29,
            "status":"Married",
            "hobbies":"Book"
        }
    }
    if username in Users.keys():
        return render_template('index3.html', users = Users[username])
    else:
        return render_template('index4.html', user = username)


if __name__ == '__main__':
    app.run(debug=True)
