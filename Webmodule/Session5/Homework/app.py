from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bai1')
def ex1():
    return render_template('bai1.html')

@app.route('/bai2')
def ex2():
    return render_template('bai2.html')

@app.route('/bai3')
def ex3():
    return render_template('bai3.html')

if __name__ == '__main__':
  app.run(debug=True)
