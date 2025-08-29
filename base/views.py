from django.shortcuts import render
from .models import Room   



# rooms = [
#     {'id': 1, 'name': 'Let\'s learn Python!'},
#     {'id': 2, 'name': 'Design with me'},    
#     {'id': 3, 'name': 'Frontend Developers'},
#     {'id': 4, 'name': 'Backend Developers'},
#     {'id': 5, 'name': 'Fullstack Developers'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}   
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
