from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the main page for Phone Radar website")