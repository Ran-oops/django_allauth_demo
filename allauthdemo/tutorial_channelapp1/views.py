from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tutorial_channelapp1/index.html')