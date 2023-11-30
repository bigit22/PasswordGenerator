from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!"£$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    the_password = ''

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})
