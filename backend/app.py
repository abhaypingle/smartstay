from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

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