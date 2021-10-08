from django.shortcuts import render,redirect
from django.http import HttpResponse
import urllib.request
import json

# Create your views here.
def index(request):
    if request.method == 'POST' :
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather? q=' + city + '&units=metrics&appid=ba3f48a1cf01dcd1912d4803ff8a3cad').read()

        List_of_data = json.loads(source)

        data = {
            "country_code": str(List_of_data['sys']['country']),
            "coordinate": str(List_of_data['coord']['lon']) + ',' + str(List_of_data['coord']['lat']),
            "temp": str(List_of_data['main']['temp']) + 'C',
            "pressure": str(List_of_data['main']['pressure']),
            "humidity": str(List_of_data['main']['humidity']),
            "main": str(List_of_data['weather'][0]['main']),
            "description": str(List_of_data['weather'][0]['description']),
            "icon": str(List_of_data['weather'][0]['icon']),
        }
        print(data)
    else:
        data = {}

    return render(request, 'index.html', data)