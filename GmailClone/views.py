from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def display(request):
    n = request.GET['tbname']
    e = request.GET['tbemail']
    data={'n':n,'e':e}
    return render(request,'display.html',data)