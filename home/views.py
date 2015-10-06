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

        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')
        if full_name == "Jacob":
            full_name = "Developer"
        instance.full_name = full_name
        instance.save()
        context = {
        "hello_message": "Student Saved",

    }
    return render(request, 'index.html', context)



