from flask import Flask ,render_template , request
import requests

app = Flask(__name__)
Api_KEY='YourAPIKey'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            url = f'http://api.weatherapi.com/v1/current.json?key={Api_KEY}&q={city}&aqi=no'
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                print(weather_data)  # Print the weather data to see its structure
                if 'error' in weather_data:
                    error_message = 'Weather data not available for this location.'
            else:
                error_message = 'Error fetching weather data. Please try again later.'

    return render_template('index.html', weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
