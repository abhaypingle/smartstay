from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from extensions import db
from models import User, OwnerProfile, Property, Room, PropertyImage, Amenity, PropertyAmenity, Favorite, VisitRequest, Report
app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://smartstay_user:smartstay_pass@127.0.0.1:5433/smartstay_db'
db.init_app(app)
migrate = Migrate(app, db)

from models import User

@app.route('/')
def home():
    return {"message": "SmartStay backend is running!"}

@app.route('/api/properties')
def get_properties():
    sample_properties = [
        {"id": 1, "title": "2BHK near City Center", "rent": 12000, "city": "Hyderabad"},
        {"id": 2, "title": "PG for Students", "rent": 6000, "city": "Nizamabad"},
        {"id": 3, "title": "1BHK Furnished Flat", "rent": 9000, "city": "Hyderabad"}
    ]
    return {"properties": sample_properties}

if __name__ == '__main__':
    app.run(debug=True)