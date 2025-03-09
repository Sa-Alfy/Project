# Prayer Times & Weather App

![Prayer Times & Weather App](path/to/screenshot.png)

A Flask-based web application that provides Islamic prayer times and real-time weather information, optimized for both desktop and mobile devices.

## Features

- **Islamic Prayer Times**: Get prayer times for any city worldwide.
- **Ramadan Timings**: Display Sehri and Iftar times during Ramadan.
- **Real-time Weather Information**: Fetch current weather details for any location.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **Live Analog and Digital Clock**: Display current time in both formats.
- **Dark Theme Interface**: User-friendly dark mode for better visibility.

## Setup

Follow these steps to set up and run the application:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Sa-Alfy/Project.git
    cd Flask
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file with your credentials:**
    ```
    FLASK_SECRET_KEY=your-secret-key
    OPENWEATHERMAP_API_KEY=your-api-key
    ```

5. **Run the application:**
    ```bash
    python Main.py
    ```

## Access on Mobile

1. Ensure your phone is connected to the same WiFi network as your computer.
2. Find your computer's local IP address (printed when running the app).
3. On your phone's browser, enter: `http://<your-computer-ip>:5000`.

## Default Login

- **Username**: Admin
- **Password**: 102030


## Developer

- **Name**: Shariar Ahamed
- **Email**: [saaulfy@gmail.com](mailto:saaulfy@gmail.com)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## Acknowledgements

- [Aladhan API](https://aladhan.com/prayer-times-api) for providing prayer times.
- [OpenWeatherMap API](https://openweathermap.org/api) for weather information.
- [Font Awesome](https://fontawesome.com) for icons.

git clone https://github.com/Sa-Alfy/Project.git
