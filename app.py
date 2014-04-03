from flask import Flask, request, redirect, url_for
from flask import render_template, request
from werkzeug.utils import secure_filename
import os
import commands
import random

from converter import convert_images

app = Flask(__name__)

BACKGROUND="./pyramids.jpg"

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = "%s" % random.randint(0, 0xffffffff)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            newfilename = convert_images("./uploads/%s" % filename, BACKGROUND)
            return redirect("/uploaded?filename=%s" % newfilename)
    return render_template('upload_form.html')
    

@app.route("/uploaded")
def uploaded_file():
    return "<img src='%s'>" % url_for('static', filename=request.args["filename"])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
