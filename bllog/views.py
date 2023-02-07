from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    allposts = Blogpost.objects.all()
    return render(request, "bllog/main.html", {"myposts":allposts})

def blogpost(request, id):
    posts = Blogpost.objects.filter(post_id=id)[0]
    # print(posts)
    return render(request, "bllog/blogposts.html", {"apost":posts})