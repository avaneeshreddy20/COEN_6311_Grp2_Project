import os
from flask import Flask
from flask import Request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class  trip (db.Model):
    __tablename__ = 'trip'    
    id = db.Column(db.Integer, primary_key= True)
    origin = db.Column(db.Text)
    destination = db.Column(db.Text)
    
    

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def __repr__(self):
        return (f"{self.origin}+{self.destination}")

################################################################################



from flask import Flask, render_template, request, url_for


app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('webpage1.html')

@app.route('/search_request')
def search_request():
    return render_template('search_request.html')


@app.route('/About')
def About():
    return render_template('About.html')

db = SQLAlchemy(app)
migrate= Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)