import os

from flask import Flask, render_template, request, redirect, send_file, url_for
#import upload,download data from s3_files.py file
from s3_files import list_files, download_file, upload_file


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
DOWNLOAD_FOLDER = "downloads"
#existing bucket in s3
BUCKET = "nkrecipe1234"

@app.route('/')
def entry_point():
    return 'My Recipe Journal!'

@app.route("/indexpage")
def indexpage():
    return render_template('indexpage.html')

@app.route("/index")
def index():
    contents = list_files("nkrecipe1234")
    return render_template('index.html', contents=contents)

@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        upload_file(f"{f.filename}", BUCKET)
        
        return redirect("/index")
        #return custom_response({'message': 'file / image uploaded'}, 200)
        #msg = "Upload Complete!"
        #return redirect("/index", msg =msg)




    
@app.route("/search")
def search():
    return render_template('search.html')  
    
@app.route("/profile")
def profile():
    return render_template('profile.html')
    
@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)