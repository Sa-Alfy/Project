from flask import Flask, render_template, request, redirect, url_for, session
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default-secret-key')

# Authentication credentials
User = 'Admin'
Pass = '102030'

# API Configuration
OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

# Helper Functions
def get_prayer_times(city, country):
    """Fetch prayer times from Aladhan API for given city and country."""
    today = datetime.now().strftime('%Y-%m-%d')
    url = f'https://api.aladhan.com/v1/timingsByCity/{today}?city={city}&country={country}'
    response = requests.get(url)
    data = response.json()
    timings = data['data']['timings']
    
    # Split into regular prayers and Ramadan timings
    prayer_times = {
        'Fajr': convert_to_12hr_format(timings['Fajr']),
        'Sunrise': convert_to_12hr_format(timings['Sunrise']),
        'Dhuhr': convert_to_12hr_format(timings['Dhuhr']),
        'Asr': convert_to_12hr_format(timings['Asr']),
        'Maghrib': convert_to_12hr_format(timings['Maghrib']),
        'Isha': convert_to_12hr_format(timings['Isha'])
    }
    
    ramadan_times = {
        'Sehri': convert_to_12hr_format(timings['Fajr']),  # Sehri ends at Fajr
        'Iftar': convert_to_12hr_format(timings['Maghrib'])  # Iftar starts at Maghrib
    }
    
    return prayer_times, ramadan_times

def get_weather(city):
    """Fetch weather information from OpenWeatherMap API for given city."""
    api_key = session.get('weather_api_key')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data['main']

def convert_to_12hr_format(time_str):
    """Convert 24-hour time format to 12-hour format."""
    try:
        time_obj = datetime.strptime(time_str, '%H:%M')
        return time_obj.strftime('%I:%M %p')
    except:
        return time_str

# Route Handlers
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        api_key = request.form.get('api_key')  # Optional API key
        
        if username == User and password == Pass:
            session['logged_in'] = True
            session['username'] = username
            if api_key:  # Only store API key if provided
                session['weather_api_key'] = api_key
            return redirect(url_for('home'))
        return "Invalid credentials. Please try again."
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Handle user logout."""
    session.clear()
    return redirect(url_for('login'))

@app.route('/about')
def about():
    """Render the about page."""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('about.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    """Render the home page and handle prayer times and weather information."""
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        city = request.form['city']
        country = request.form['country']
        prayer_times, ramadan_times = get_prayer_times(city, country)
        
        weather = None
        if session.get('weather_api_key'):
            try:
                weather_data = get_weather(city)
                weather = {
                    'temperature': weather_data['temp'],
                    'humidity': weather_data['humidity'],
                    'description': 'Weather information'
                }
            except:
                weather = None
        
        return render_template('index.html', 
                             prayer_times=prayer_times,
                             ramadan_times=ramadan_times,
                             weather=weather, 
                             city=city, 
                             country=country,
                             has_weather_api=bool(session.get('weather_api_key')))
    
    return render_template('index.html', has_weather_api=bool(session.get('weather_api_key')))

if __name__ == '__main__':
    # Get local IP address
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"\nAccess the app on your phone at: http://{local_ip}:5000\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
