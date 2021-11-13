from flask import Flask, render_template, request   
from werkzeug.utils import secure_filename
import os
import converter

app = Flask(__name__)

# Creating the upload folder
upload_folder = "uploads/"
if not os.path.exists(upload_folder):
   os.mkdir(upload_folder)

# Configuring the upload folder
app.config['UPLOAD_FOLDER'] = upload_folder

# configuring the allowed extensions
allowed_extensions = ['json']

def convert(filename):
    
    json_list = []
    converted_list = []
    
    for i in lst:
        df_json = pd.read_json(i)
        converted_list = df_json.to_excel(i)
    return (converted_list)

@app.get('/')
def home():
    return render_template ("home.html")


	

@app.route('/about')
def about():
    return render_template ("about.html")

@app.route('/contact')
def contact():
    return render_template ("contact.html")

if __name__=="__main__":
    app.run(debug=True)

