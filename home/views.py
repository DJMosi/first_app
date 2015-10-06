from django.shortcuts import render
#from django.http import HttpResponse
from .forms import StudentForm
# Create your views here.

def index(request):
    print(request.POST  )
    form = StudentForm(request.POST or None)

     context = {
        "hello_message": "Register new student",
        "form": form
    }

    if form.is_valid():
        form.save()

     context = {
        "hello_message": "Student Saved",
        "form": form
    }
    return render(request, 'i ndex.html', context)



