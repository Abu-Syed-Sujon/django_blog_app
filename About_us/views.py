'this is about views'
# pylint: disable=no-member
from django.shortcuts import render
from About_us.models import Teacher

def about_us(request):
    'its call about.html'
    return render(request, "about_us/about.html")

def teachers_info(request):
    'models view'
    teachers = Teacher.objects.all()
    return render(request, "about_us/teachers.html", {'teachers': teachers})
    # Continue with the rest of your code...
