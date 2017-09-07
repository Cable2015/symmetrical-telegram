from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, "first_app/index.html")

def blog(request):
    return render(request, "first_app/blogs.html")


print "TEST In APPS VIEWS"
