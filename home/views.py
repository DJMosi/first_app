from django.shortcuts import render
#from django.http import HttpResponse
from .forms import StudentForm
# Create your views here.

def index(request):
    print(request.POST  )
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "hello_message": "Hello Moringa",
        "form": form
    }
    return render(request, 'index.html', context)



