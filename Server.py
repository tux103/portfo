# note need to use $env:FLASK_APP = "Server.py"  not set "FLASK_APP=hello.py" then run flask run

# to run webstie need to 1 c:\Taraka\python\venv 2 set FLASK_APP= Server.py 3 $env:FLASK_APP = "Server.py" 4 flask run### then go to http://127.0.0.1:5000/


# @app.route('/works.html')
# def works():
#     return render_template('works.html') # note when using render template it looks for folder talled 'templates' this pulls the Html file

# @app.route('/index.html')
# def my_hone_1():
#     return render_template('index.html') # note when using render template it looks for folder talled 'templates' this pulls the Html file

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html') # note when using render template it looks for folder talled 'templates' this pulls the Html file

# @app.route('/components.html')
# def components():
#     return render_template('components.html') # note when using render template it looks for folder talled 'templates' this pulls the Html file

# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs'

# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'this is my dog'





import re
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import csv # this is lesson 273 to write to a CSV file  # https://docs.python.org/3/library/csv.html CSV documentation
 

@app.route('/')
def my_hone():
    return render_template('index.html') # note when using render template it looks for folder talled 'templates' this pulls the Html file


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name) #This dynamically make page name change 


# lesson 269

## @app.route('/submit_form', methods=['POST', 'GET'])
## def submit_form():
##     if request.method =='POST':
##        data = request.form.to_dict() # this transfer data to python app via a distionary 
##        print(data)
##        return redirect('/Thanyou.html')
##     else:
##         return'someting went wrong try again!'

# # lesson 272 Finish this 
# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email =data['email']
#         subject =data['subject']
#         message = data['message']
#         file = database.write(f'\n{email},{subject},{message}')


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method =='POST':
#        data = request.form.to_dict() # this transfer data to python app via a distionary 
#        write_to_file(data)
#        return redirect('/Thanyou.html')
#     else:
#         return'someting went wrong try again!'


# lesson 273 -- There seems to be an error in the CSV file not the code 
def write_to_csv(data):
    with open('database.csv',  newline='',mode='a',) as database2: # note error in vidoe newline''must be in open not on csv_writer on row 57 as per video
        email =data['email']
        subject =data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter =',', quotechar='"', quoting=csv.QUOTE_MINIMAL) # this configures how the data will be written to a file 
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
     if request.method =='POST':
        try:
            data = request.form.to_dict() # this transfer data to python app via a distionary 
            write_to_csv(data)
            return redirect('/Thanyou.html')
        except:
            return 'did not save to database'
     else:
         return'someting went wrong try again!'

