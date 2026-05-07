from django.shortcuts import render
import requests  # <--- THIS IS THE MISSING LINE

def index(request):
    weather_key = "cecf7f448d8dc1b0a94f741c315f923b"
    news_key = "22fd676e10474879942f4f2a1421b95a"
    
    # Weather
    w_url = f"http://api.openweathermap.org/data/2.5/weather?q=Patna&appid={weather_key}&units=metric"
    w_res = requests.get(w_url)
    w_data = w_res.json()

    # News (Added headers to prevent 403 errors)
    n_url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_key}"
    n_res = requests.get(n_url, headers={'User-Agent': 'Mozilla/5.0'})
    n_data = n_res.json()

    context = {
        'weather': {
            'city': w_data.get('name', f"Error: {w_data.get('message', 'Patna')}") ,
            'temp': w_data.get('main', {}).get('temp', 0),
            'description': w_data.get('weather', [{}])[0].get('description', 'No connection')
        },
        'news': n_data.get('articles', [])[:5]
    }
    return render(request, 'index.html', context)
