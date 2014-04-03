from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/choose/', methods=["GET"])
def choose():
    """Display a form where users can choose their destination and emotion"""
    return render_template('choose.html')

@app.route('/madlibs/', methods=["GET"])
def madlibs():
    """Display the madlibs fill-ins for the given place and emotion"""
    place = request.args.get('place', '')
    emotion = request.args.get('emotion', '')
    return render_template('madlibs.html', place=place, emotion=emotion)

if __name__ == '__main__':
    app.run(debug=True)
