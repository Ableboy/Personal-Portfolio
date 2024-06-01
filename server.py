from flask import Flask, render_template, request, redirect # this is a framework for web and it module
import csv
app = Flask(__name__) # This is an object of the framework
print(__name__)


@app.route('/') # This changes the root of the code files
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') # This happens to be change to dynamic way of coding instead of the DRY implementation. we achieve that by using "variable tool."
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data): # This keeps storing user information on a database called txt file
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data): # This keeps storing user information on a database called csv file which is the best way to store datas.
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer_file = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer_file.writerow([email, subject, message])
        
@app.route('/submit_form', methods=['POST', 'GET']) # This allow server to receives and store/save user input data using (request)
def submit_form():
    if request.method == 'POST': # shows which method used
        try:
            data = request.form.to_dict() # grab the data and change it to dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            print('did not save to database')
    else:
        print('something went wrong, please try again.')