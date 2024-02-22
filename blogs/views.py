'this is blogs views'
from django.shortcuts import render
from .forms import TeacherRegistration

# Create your views here.

def blog1(request):
    'this will call html file'
    return render (request,"blogs/blog.html")


def showfromsdata(request):
    'this will call html file'
    if request.method=='POST':
        fm= TeacherRegistration(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['repassword'])
            print('This is Post Statement')
            
    else:
        print('This is GET Statement')
        fm=TeacherRegistration()
    return render (request,"blogs/forms.html", {'form':fm})
