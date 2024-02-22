'This is Deep learning views'
from django.shortcuts import render

# Create your views here.

def deep_learning(request):
    'this will call html file'
    return render (request,"deep_learning/deep_learning.html")
