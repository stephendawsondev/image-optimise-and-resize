from django.shortcuts import render

# add view for index


def index(request):
    return render(request, 'index.html')
