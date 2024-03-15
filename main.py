import pyrebase

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyCEwGMvPa62SW3-7rxS-acoQko5TsWt9qk",
    "authDomain": "test-49a7b.firebaseapp.com",
    "databaseURL": "https://test-49a7b-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "test-49a7b",
    "storageBucket": "test-49a7b.appspot.com",
    "messagingSenderId": "285207762548",
    "appId": "1:285207762548:web:2bb304869cea9987926321",
    "measurementId": "G-NVC73RLNFS"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Example sensor data
sensor_data = {
    "temperature": 25,
    "humidity": 50
}

# Push data to Firebase
db.child("sensors").push(sensor_data)
