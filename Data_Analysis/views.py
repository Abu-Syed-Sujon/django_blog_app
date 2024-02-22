'This is Data analysis views'
from django.shortcuts import render

# Create your views here.

def data_analysis(request):
    'This will call html file'
    return render (request,"data_analysis/data_analysis.html")
