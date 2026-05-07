from django.shortcuts import render
import requests

def index(request):
    # 1. Setup API Keys (Use your own keys here)
    weather_key = "YOUR_OPENWEATHER_API_KEY"
    news_key = "YOUR_NEWSAPI_KEY"
    
    # 2. Fetch Weather (Patna)
    w_url = f"http://api.openweathermap.org/data/2.5/weather?q=Patna&appid={weather_key}&units=metric"
    w_data = requests.get(w_url).json()

    # 3. Fetch News
    n_url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_key}"
    n_data = requests.get(n_url).json()

    # 4. Format data to match your HTML exactly
    context = {
        'weather': {
            'city': w_data.get('name', 'Patna'),
            'temp': round(w_data.get('main', {}).get('temp', 0)),
            'description': w_data.get('weather', [{}])[0].get('description', 'No data')
        },
        'news': n_data.get('articles', [])[:5] # Takes the top 5 articles
    }

    return render(request, 'index.html', context)
