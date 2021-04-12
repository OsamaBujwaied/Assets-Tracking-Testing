from django.shortcuts   import render, redirect
from django.http        import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import BorrowingForm, AssetForm
from datetime import date
# Create your views here.

def login(request):
    context = {}
    return render(request, 'assetstracking/login.html', context)


# @login_required
def home(request): 
    today = date.today()
    lastDay = Borrowing.objects.values('end_date')
    print("nnnnnnnnnn",lastDay)
    subscriber = Subscriber.objects.all()
    
    total_subscribers = subscriber.count()

    borrowing = Borrowing.objects.all()

    context = {'subscriber': subscriber, 'total_subscribers':total_subscribers, 'borrowing':borrowing }
    return render(request, 'assetstracking/home.html', context)


# @login_required
def subscriber(request, subscriber_test): 

    subscriber = Subscriber.objects.get(id=subscriber_test)
	
    borrowings = subscriber.borrowing_set.all()
    borrowing_count = borrowings.count()

    employee = Employee.objects.all()
    employees = subscriber.employee_set.all()
    employee_count = employees.count()

    tags = subscriber.tag_set.all()
    tag_count = tags.count()
    
    rfids = subscriber.rfid_set.all()
    rfid_count = rfids.count()

    context =   {'subscriber': subscriber, 
                'borrowings': borrowings, 'borrowing_count': borrowing_count,
                'employee': employee, 'employees': employees, 'employee_count': employee_count,
                'tags': tags , 'tag_count': tag_count,
                'rfids': rfids , 'rfid_count': rfid_count
                }
    return render(request, 'assetstracking/subscriber.html', context)


def employee(request, employee_test): 

    employee = Employee.objects.get(id=employee_test)
	
    borrowings = employee.borrowing_set.all()
    borrowing_count = borrowings.count()

    context = {'employee': employee, 'borrowings': borrowings, 'borrowing_count':borrowing_count}
    return render(request, 'assetstracking/employee.html', context)




def rfid(request): 
    rfid = RFID.objects.all()
    return HttpResponse('RDID reader page')


def tags(request): 
    tags = Tag.objects.all()
    return render(request, 'assetstracking/tags.html', {'tags': tags})


def index(request): 
    return render(request, 'assetstracking/index.html')

def createBorrowing(request):

    form = BorrowingForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = BorrowingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/subscriber/1')

    context = {'form':form}
    return render(request, 'assetstracking/createBorrowing.html', context)
    
def updateBorrowing(request, borrowing_test):

    borrowing = Borrowing.objects.get(id=borrowing_test)
    form = BorrowingForm()

    if request.method == 'POST':
        form = BorrowingForm(request.POST, instance=borrowing)
        if form.is_valid():
            form.save()
            return redirect('/subscriber/1')

    context = {'form':form}
    return render(request, 'assetstracking/createBorrowing.html', context)
    
def deleteBorrowing(request, pk):
    borrowing = Borrowing.objects.get(id=pk)
    if request.method == "POST":
        borrowing.delete()
        return redirect('/subscriber/1')
    context = {'item': borrowing}
    return render(request, 'assetstracking/deleteBorrowing.html',context)
    
    
def createAsset(request):

    form = AssetForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/subscriber/1')

    context = {'form':form}
    return render(request, 'assetstracking/createAsset.html', context)