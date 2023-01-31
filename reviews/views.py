from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NameForm
# Create your views here.

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