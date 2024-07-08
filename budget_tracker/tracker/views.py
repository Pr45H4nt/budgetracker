from django.shortcuts import render
from .forms import *
from django.db.models import Sum

# Create your views here.

def indexview(request):
    total_income = Income.objects.aggregate(total = Sum('amount'))['total'] or 0

    context = {'total_income':total_income}
    return render(request,'index.html', context)


def addview(request, formtype):
    if request.method == "POST":
        form = formtype(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = formtype()
    context = {'form': form}
    return render(request , 'add.html', context)

