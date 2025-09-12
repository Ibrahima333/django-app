from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band



def hello(request):
    bands = Band.objects.all()
    # return HttpResponse("listings/hello.html")
    return render(request, 'listings/hello.html',
                            {'band' : bands })

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact_us(request):
    return HttpResponse("<input type = 'email'  id= 'email'> <label for='email'> email </label>")