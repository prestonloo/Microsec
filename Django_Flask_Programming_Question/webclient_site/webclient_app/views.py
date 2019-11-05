from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def loadPage(request):
     title = "Temperature Sensor"
     message = "The list of temperatures is shown below in Degree Celsius.<p>Date Time | Temperature"
     return render(request, 'webclient_app.html', {'title': title, 'message': message})