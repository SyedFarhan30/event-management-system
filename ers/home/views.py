from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) :
    # return HttpResponse("This is home page")
    context = {
        "variable" : "this is testing  a variable."
    }
    return render(request, "index.html", context)

def viewEvents(request):
    # return HttpResponse("This is view events page")
    return render(request, "viewEvents.html")

def carnival(request):
    return render(request, "carnival.html")

def home(request):
    return render(request, "home.html")