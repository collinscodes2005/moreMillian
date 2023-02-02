from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NameForm
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

'''function that creates the file for us '''
def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
       

class CreateProfileView(View):
    def get(self, request):
        return render(request, "feedback/file-upload.html")

    #the post function 
    def post(self, request):
        store_file(request.FILES["image"])
        return HttpResponseRedirect("/file-upload")


def index(request):

    if request.method == "POST":

        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
        
        else:
            form = NameForm(0)

    return render(request, "feedback/index.html", {'form' : NameForm})


def thanks(request):
    return HttpResponse("Thanks for filling ")

def upload(request):
    return render(request, "feedback/file-upload.html")