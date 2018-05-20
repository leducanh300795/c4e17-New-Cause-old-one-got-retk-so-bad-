from flask import Flask
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def index(weight,height):

    height = height/100
    b = weight/(height*height)
    if b < 16:
        return "Severy underweight"
    elif b >= 16 and b <18.5:
        return "Underweight"
    elif b >= 18.5 and b < 25:
        return "Normal"
    elif b >= 25 and b < 30:
        return "Over Weight"
    else:
        return "Obese"


if __name__ == '__main__':
  app.run(debug=True)
