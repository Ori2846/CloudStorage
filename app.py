try:

    from flask import Flask
    import os
    from flask import redirect, url_for, request, render_template, send_file
    from io import BytesIO

    from flask_wtf.file import FileField
    from wtforms import SubmitField
    from flask_wtf import Form
    import sqlite3
    from werkzeug.utils import secure_filename

    import os
    from datetime import datetime
    import shutil
    import ssl




    print("All Modules Loaded .... ")
except:
    print (" Some Module are missing ...... ")
path = "I:/"

# Get the disk usage statistics
# about the given path

stat = shutil.disk_usage(path)
GB_Left = str((round(int((shutil.disk_usage(path).free)/1000000000)))) + " GB Free"
print(GB_Left)
# Print disk usage statistics
print("Disk usage statistics:")
print(stat)
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
UPLOAD_FOLDER = 'I:\CloudStorage'
UPLOAD_FOLDER2 = r'I:\CloudStorage\UPLOAD!DOWNLOAD FOLDER'
#UPLOAD_FOLDER = r"C:\Users\hdo28\Desktop"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.errorhandler(500)
def internal_error(error):
    form = UploadForm()
    post2 = "76"
    GB_Free = str((round(int((shutil.disk_usage(path).free) / 1000000000)))) + " GB Free"
    GB_Total = str((round(int((shutil.disk_usage(path).total) / 1000000000)))) + " GB In total"
    percent = str(((round(int((shutil.disk_usage(path).free) / 100000000000)))/(round(int((shutil.disk_usage(path).total)) / 100000000000)))*100)
    print(str(percent) + " left")
    return render_template("index2.htmll", form=form, post2 = GB_Free, percent = percent)
@app.route('/', methods=["GET", "POST"])
def index():
    post2 = "5"
    form = UploadForm()
    GB_Free = str((round(int((shutil.disk_usage(path).free) / 1000000000)))) + " GB Free"
    GB_Total = str((round(int((shutil.disk_usage(path).total) / 1000000000)))) + " GB In total"
    percent = str(((round(int((shutil.disk_usage(path).free) / 100000000000)))/(round(int((shutil.disk_usage(path).total)) / 100000000000)))*100)
    return render_template("index2.html", form=form, post2=GB_Free, percent=percent)
@app.route("/upload", methods=["POST"])
def upload():
    form = UploadForm()
    post2 = "76"
    path = "I:/"
    GB_Free = str((round(int((shutil.disk_usage(path).free) / 1000000000)))) + " GB Free"
    GB_Total = str((round(int((shutil.disk_usage(path).total) / 1000000000)))) + " GB In total"
    percent = str(((round(int((shutil.disk_usage(path).free) / 100000000000)))/(round(int((shutil.disk_usage(path).total)) / 100000000000)))*100)
    print(str(percent) + " left")

    try:
        if request.method == 'POST':
            a = datetime.now()
            print("year =", a.year)
            print("month =", a.month)
            print("day =", a.day)
            print("hour =", a.hour)
            print("minute =", a.minute)
            directory = str(a.month) + "-" + str(a.day) + "-" + str(a.year) + "-" + str(a.hour) + "-" + str(a.minute) + "-" + str(a.second)
            #parent_dir = "E:/"
            parent_dir = "I:/CloudStorage"
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            print("Directory '% s' created" % directory)
            UPLOAD_FOLDER = path
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            uploaded_files = request.files.getlist("file[]")
            print (uploaded_files)
            for file in uploaded_files:
                print('no')
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return render_template("home.html", form=form, post2 = GB_Free, percent = percent)
    except:
        return render_template("index2.html", form=form, post2 = GB_Free, percent = percent)
@app.route("/upload2", methods=["POST"])
def upload2():
    form = UploadForm()
    post2 = "76"
    path = "I:/"
    GB_Free = str((round(int((shutil.disk_usage(path).free) / 1000000000)))) + " GB Free"
    GB_Total = str((round(int((shutil.disk_usage(path).total) / 1000000000)))) + " GB In total"
    percent = str(((round(int((shutil.disk_usage(path).free) / 100000000000)))/(round(int((shutil.disk_usage(path).total)) / 100000000000)))*100)
    print(str(percent) + " left")

    try:
        if request.method == 'POST':
            a = datetime.now()
            uploaded_files = request.files.getlist("file2[]")
            print (uploaded_files)
            for file in uploaded_files:
                print('no')
                file.save(os.path.join(UPLOAD_FOLDER2, secure_filename(file.filename)))
            return render_template("home.html", form=form, post2 = GB_Free, percent = percent)
    except:
        return render_template("index2.html", form=form, post2=GB_Free, percent=percent)

@app.route('/download2', methods=["GET", "POST"])
def download():

    form = UploadForm()

    if request.method == "POST":

        conn= sqlite3.connect("YTD.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  my_table """)

        for x in c.fetchall():
            name_v=x[0]
            data_v=x[1]
            break

        conn.commit()
        cursor.close()
        conn.close()

        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)


    return render_template("index2.html", form=form)




class UploadForm(Form):
    file = FileField()
    submit = SubmitField("submit")
    download = SubmitField("download")

def database(name, data):
    conn= sqlite3.connect("YTD.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS my_table (name TEXT,data BLOP) """)
    cursor.execute("""INSERT INTO my_table (name, data) VALUES (?,?) """,(name,data))

    conn.commit()
    cursor.close()
    conn.close()


@app.route('/download/<path:filename>')
def download2(filename):
    return send_file('I:/CloudStorage/UPLOAD!DOWNLOAD FOLDER/' + filename, as_attachment=True)
@app.route('/download', methods=["GET", "POST"])
def print_ul():
    options = os.listdir(r"I:/CloudStorage/UPLOAD!DOWNLOAD FOLDER")
    forward_message = "Moving Forward..."
    return render_template('home2.html', options = options,forward_message=forward_message)

def move_forward():
    #Moving forward code
    print("Moving Forward...")
def query():
        conn= sqlite3.connect("YTD.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  my_table """)

        for x in c.fetchall():
            name_v=x[0]
            data_v=x[1]
            break

        conn.commit()
        cursor.close()
        conn.close()

        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)


if __name__ == "__main__":
    #app.run(debug=True)
    from waitress import serve
    #app.run(ssl_context=('cert2.pem', 'key2.pem'))
    app.run(host='0.0.0.0',port=80)
    #host='0.0.0.0',port=80,
