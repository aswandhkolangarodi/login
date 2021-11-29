from django.shortcuts import render

# Create your views here.
def loginfn(req):
    return render(req,'login.html')

