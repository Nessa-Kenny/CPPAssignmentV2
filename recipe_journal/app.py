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

#add_recipe
@app.route("/add_recipe")
def add_recipe():
    return render_template('add_recipe.html')
    
@app.route("/jtest")
def jtest():
    return render_template('jtest.html')    

#File download   
@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)
#Indexpage 1
@app.route("/indexpage")
def indexpage():
    return render_template('indexpage.html')

#Index page 2
@app.route("/index")
def index():
    contents = list_files("nkrecipe1234")
    return render_template('index.html', contents=contents)

#login page
@app.route("/login")
def login():
    return render_template('login.html')
   
#profile page
@app.route("/profile")
def profile():
    return render_template('profile.html')

#search_recipe page
@app.route("/search")
def search():
    return render_template('search.html')  

#upload file
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

@app.route("/upload1", methods=['POST'])
def upload1():
    fh = open ( "test.txt", "w")
    upload_file("test.txt", BUCKET)
    return redirect("/index")
    
#add recipe - read in form and create text file   
@app.route("/add_rec", methods=['POST'])
def add_rec():
    title = request.form['r_title']
    tit = title + '.html'
    fh = open (title,  "w")
    
    ing = request.form['r_ing']
    fh.write('Ingredients: \n\n')
    fh.write(ing + '\n\n\n')
    
    meth = request.form['r_method']
    fh.write('Method: \n\n')
    fh.write(meth + '\n\n\n')
    
    notes = request.form['r_notes']
    fh.write('Notes: \n\n')
    fh.write(notes + '\n\n\n')
    
    kw = request.form['r_key']
    fh.write('Keywords: \n\n')
    fh.write(kw)
    
    fh.close()
    upload_file(title, BUCKET)
    return redirect("/index")    
        
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)