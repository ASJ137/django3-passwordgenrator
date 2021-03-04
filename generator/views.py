from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,"generator/home.html")

def password(request):
    thepassword = ""
    Characters = list("abcdefghijklmnopqrstuvwxyz")
    length = int(request.GET.get("length",12))

    if request.GET.get("uppercase"):
        Characters.extend(list("ABCDEFGHIJKLMNOPQRTUVWXYZ"))

    if request.GET.get("special"):
        Characters.extend(list("!@#$^*_-"))

    if request.GET.get("number"):
        Characters.extend(list("0123456789"))


    for x in range(length):
        thepassword += random.choice(Characters)

    return render(request,"generator/password.html",{"password":thepassword})


def about(request):
    return render(request,"generator/about.html")
