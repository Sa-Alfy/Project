import requests
from datetime import datetime

def get_prayer_times(city, country):
    try:
        today = datetime.now().strftime('%Y-%m-%d')  # Changed from '%y-%m-%d' to '%Y-%m-%d'
        url = f'https://api.aladhan.com/v1/timingsByCity/{today}?city={city}&country={country}'
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        if 'data' in data and 'timings' in data['data']:
            timings = data['data']['timings']
            return {
                'Fajr': timings['Fajr'],
                'Sunrise': timings['Sunrise'],
                'Dhuhr': timings['Dhuhr'],
                'Asr': timings['Asr'],
                'Maghrib': timings['Maghrib'],
                'Isha': timings['Isha']
            }
        else:
            return "Unable to fetch prayer times: Invalid response format"
    except requests.RequestException as e:
        return f"Error fetching prayer times: {str(e)}"
    

if __name__ == "__main__":
    print(get_prayer_times('Dhaka', 'Bangladesh'))