from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band



def hello(request):
    bands = Band.objects.all()
    print(bands)
    
    
    return HttpResponse(f"""<h1>Hello Django!</h1>
                        <p> mes paragraphe prefere :</p>
                        <ul> 
                            <li>{bands[0].name}</li>
                            <li>{bands[1].name}</li>
                         </ul>
                         <p> les titres : {bands[2].title}</p>
                         <p> les titres : {bands[3].title}</p>""")

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact_us(request):
    return HttpResponse("<input type = 'email'  id= 'email'> <label for='email'> email </label>")