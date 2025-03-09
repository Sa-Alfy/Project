# Prayer Times & Weather App

A Flask-based web application that provides prayer times and weather information, optimized for both desktop and mobile devices.

## Features

- Islamic prayer times for any city
- Ramadan timings (Sehri and Iftar)
- Real-time weather information
- Responsive design for mobile devices
- Live analog and digital clock
- Dark theme interface

## Setup

1. Clone the repository
```bash
git clone <(https://github.com/Sa-Alfy/Project.git)>
cd Flask
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create .env file with your credentials
```
FLASK_SECRET_KEY=your-secret-key
OPENWEATHERMAP_API_KEY=your-api-key
```

5. Run the application
```bash
python Main.py
```

## Access on Mobile

1. Make sure your phone is connected to the same WiFi network as your computer
2. Find your computer's local IP address (printed when running the app)
3. On your phone's browser, enter: `http://<your-computer-ip>:5000`

## Default Login

- Username: Admin
- Password: 102030

## Developer

- Name: Shariar Ahamed
- Email: www.saaulfy@gmail.com
