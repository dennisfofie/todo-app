from flask import Flask
from flask_marshmallow import  Marshmallow
from flask_sqlalchemy import SQLAlchemy

# instantiate flask app
app = Flask(__name__)

# configure app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# configure db
db = SQLAlchemy(app)

# configure schema
ma = Marshmallow(app)

if __name__ == '__main__':
    app.run(debug=True)