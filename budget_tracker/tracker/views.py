from django.shortcuts import render
from .forms import *
from django.db.models import Sum
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone


# Create your views here.

def indexview(request):
    total_income = Income.objects.aggregate(total = Sum('amount'))['total'] or 0
    total_expense = Expense.objects.aggregate(total = Sum('amount'))['total'] or 0

    context = {'total_income':total_income , 'total_expense': total_expense}
    return render(request,'index.html', context)


def addview(request, formtype):
    if request.method == "POST":
        form = formtype(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sucessfully Added")
        else:
            messages.error(request, "Something went wrong!!")
        

    else:
        form = formtype()
    context = {'form': form}
    return render(request , 'add.html', context)

def showdb(request , database, datacategory):
    today = timezone.now().date()
    seven_days_ago = today - timedelta(days=7)


    data = database.objects.filter(date__gte = seven_days_ago)
    category = datacategory.objects.all()

    context = {
        'data' : data ,
        'category' : category
    }

    return render(request , 'datas.html', context)
    

