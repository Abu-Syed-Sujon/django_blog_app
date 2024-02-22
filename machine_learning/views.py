'This is views file for all functions!'
from django.shortcuts import render

# Create your views here.

def machine_learning(request):
    'this is machine learning function'
    
    offering={'what':'machine learning'}
    return render(request, "machine_learning/ml.html", context=offering)

def dtree(request):
    'this is decission tree views'
    return render(request, "machine_learning/dt.html")

def random(request):
    'this is random forest views'
    return render(request, "machine_learning/random.html")

def k_nearest(request):
    'this is k knn views'
    return render(request, "machine_learning/knn.html")

# Ensure there is an empty line below this comment
