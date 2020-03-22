from django.shortcuts import render
from pprint import pprint
# Create your views here.


def main_entry_point(request):
    return render(request, 'index.html', { })
    
def suppliers(request):
    return render(request, 'suppliers.html', { })

def points(request):
    return render(request, 'points.html', { })    

def new_supplier(request):
    if request.method == "POST":
        print(request.POST['login'])

#pprint(request.POST)
    else:
        pass    
    return render(request, 'new_sup.html', {})