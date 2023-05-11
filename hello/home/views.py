from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable': 'Harry is great',
        'variable2' : "i am the best"
    }
    return render(request,template_name='index.html', context=context)

def about(request):
    return render(request,template_name='about.html')
    
    # return HttpResponse(f"this is about page ")

def services(request):
    return render(request,template_name='services.html')

    # return HttpResponse(f"this is services page")

def contact(request):
    return render(request,template_name='contact.html')

    # return HttpResponse(f"Contact me at 9351548226")