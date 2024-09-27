import flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#Initialize Flask
app = Flask(__name__)

#Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin123@localhost/staff_management' #rootname,password,local host and database name
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

#initialize Database
db=SQLAlchemy(app)


#Define Staff Model
class staff(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    designation = db.Column(db.String(100),nullable = False)
    dept = db.Column(db.String(100),nullable = False)
    salary = db.Column(db.Float(10,2),nullable = True)


    def __str__(self) -> str:
        return super().__str__()


#Route for Home Page
@app.route('/')
def home():
    staffData = staff.query.all()
    return render_template ('index.html',sData = staffData)

#Route for Profile Page
@app.route('/profile')
def profile():
    return render_template ('profile.html')

#Route for Contact Page
@app.route('/contact')
def contact():
    return render_template ('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
