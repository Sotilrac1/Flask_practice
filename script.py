from flask import Flask, render_template, request, url_for   
from werkzeug.utils import redirect, secure_filename
import os
import converter
import pandas as pd

app = Flask(__name__)

def convert(x):
    
    json_list = []
    converted_list = []
    
    for i in filename:
        df_json = pd.read_json(i)
        converted_list = df_json.to_excel(i.filename)
    return (print(converted_list))

@app.route('/')
def home():
    return render_template ("home.html")

@app.route("/home", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        jfile = request.form["nm"]
        return redirect(url_for("convert", json_file=jfile))
    else:
        return render_template ("home.html")

@app.route("/convert", methods=["POST", "GET"])
def convert(json_file):
    return print(json_file)










@app.route('/about')
def about():
    return render_template ("about.html")

@app.route('/contact')
def contact():
    return render_template ("contact.html")






if __name__=="__main__":
    app.run(debug=True)

