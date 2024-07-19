from django.shortcuts import render , get_object_or_404
from .forms import *
from django.db.models import Sum
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def indexview(request):
    total_income = Income.objects.filter(category__user = request.user).aggregate(total = Sum('amount'))['total'] or 0
    total_expense = Expense.objects.filter(category__user = request.user).aggregate(total = Sum('amount'))['total'] or 0


    context = {'total_income':total_income , 'total_expense': total_expense}
    return render(request,'index.html', context)

@login_required
def addview(request, formtype):
    if request.method == "POST":
        form = formtype(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.user = request.user
            inst.save()
            messages.success(request, "Sucessfully Added")
        else:
            messages.error(request, "Something went wrong!!")
        

    # form.fields['category'].queryset = .objects.filter(user=request.user)
    if formtype == ExpenseForm or formtype == IncomeForm:
        form = formtype(request=request)
    else:
        form = formtype()
    context = {'form': form}
    return render(request , 'add.html', context)



@login_required
def showdb(request, database, datacategory):
    query = database.objects.filter(category__user = request.user)

    category_queryset = datacategory.objects.filter(user = request.user)

    cat_filter = request.GET.getlist('category')
    date_filter = request.GET.get('date')
    start_date_filter = request.GET.get('start_date')
    end_date_filter = request.GET.get('end_date')
    min_amount_filter = request.GET.get('min_amount')
    max_amount_filter = request.GET.get('max_amount')
    keyword_filter = request.GET.get('keyword')
    

    if cat_filter:
        query = query.filter(category__name__in=cat_filter)
    if date_filter:
        query = query.filter(date=date_filter)
    if start_date_filter and end_date_filter:
        query = query.filter(date__range=[start_date_filter, end_date_filter])
    if min_amount_filter:
        query = query.filter(amount__gte=min_amount_filter)
    if max_amount_filter:
        query = query.filter(amount__lte=max_amount_filter)
    if keyword_filter:
        query = query.filter(description__icontains=keyword_filter)

    context = {
        'data': query.order_by('-date'),
        'category': category_queryset,
        'selectedcategory' : cat_filter
    }

    return render(request, 'datas.html', context)

@login_required
def showcat(request):
    ecategory = ExpenseCategory.objects.filter(user=request.user)
    icategory = IncomeCategory.objects.filter(user=request.user)

    context = {
        'ecategory' : ecategory , 
        'icategory' : icategory,
    }

    return render(request , 'showcat.html', context)

@login_required
def updateview(request, id, database, formtype):
    obj = get_object_or_404(database , id=id)
    if request.method == "POST":
        form = formtype(request.POST, instance = obj)
        if form.is_valid:
            form.save()
            messages.success(request, "Updated Sucessfully")
        else:
            messages.error(request, "Something went wrong")
    
    uform = formtype(instance = obj)
    context = {
        'form' : uform
    }
    return render(request, "update.html", context)
