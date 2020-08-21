from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tutorial_channelapp2/index.html')

def room(request, room_name):
    return render(request, 'tutorial_channelapp2/room.html', {
        'room_name': room_name
    })


