from django.shortcuts   import render, redirect
from django.http        import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.
from .models import *
from .forms import BorrowingForm, BorrowingFormEmployee, AssetForm


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
    form = BorrowingForm(instance=borrowing)

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
    
def extendBorrowing(request, pk):

    borrowing = Borrowing.objects.get(id=pk)
    form = BorrowingFormEmployee(instance=borrowing)

    if request.method == 'POST':
        form = BorrowingForm(request.POST, instance=borrowing)
        if form.is_valid():
            form.save()
            return redirect('/subscriber/1')

    context = {'form':form}
    return render(request, 'assetstracking/createBorrowing.html', context)


    
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

def updateAsset(request, pk):
    asset = Tag.objects.get(id=pk)
    form = AssetForm(instance=asset)

    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('/subscriber/1')

    context = {'form':form}
    return render(request, 'assetstracking/createAsset.html', context)

def deleteAsset(request, pk):
    asset = Tag.objects.get(id=pk)
    if request.method == "POST":
        asset.delete()
        return redirect('/subscriber/1')
    context = {'item': asset}
    return render(request, 'assetstracking/deleteAsset.html',context)
    

@csrf_exempt
def packet(request):
    assets_list = Tag.objects.all()
    assets_list_count = assets_list.count()
    assets_borrowed = Borrowing.objects.all()
    readers = RFID.objects.all()
    employees_list = Employee.objects.all()
    employees_list_count = employees_list.count()
    a = assets_borrowed.count()
    r = readers.count()
    count = 0
    count0 = 0
    if request.method == "POST":
        client_username = request.POST.__getitem__('username')
        client_password = request.POST.__getitem__('password')
        auth_list = ClientAuth.objects.all()
        for e in auth_list:
            real_client_username = model_to_dict(e)["client_username"]
            real_client_password = model_to_dict(e)["client_password"]

            if client_username == real_client_username and client_password == real_client_password:
                tag_id = request.POST.__getitem__('TagID')
                reader_id = request.POST.__getitem__('ReaderID')



                for i in readers:
                    reader_id0 = str(model_to_dict(i)["rfid_id"])
                    location = model_to_dict(i)["rfid_location"]
                    if reader_id == str(reader_id0):
                        if reader_id[3:] == "00":
                            for j in assets_borrowed:
                                count0 += 1
                                asset_id1 = j.tag_id.tag_id
                                asset_scan_checker = model_to_dict(j)["asset_id_scanned"]
                                if tag_id == str(asset_id1) and asset_scan_checker == 1:
                                    print("This asset is permitted to be taken.")
                                    for a in assets_list:
                                        id4 = model_to_dict(a)["id"]
                                        asset_id3 = model_to_dict(a)["tag_id"]
                                        asset_location = model_to_dict(a)["asset_location"]
                                        if str(asset_id3) == str(asset_id1):
                                            update_location = assets_list.get(id=id4)
                                            update_location.asset_location = location
                                            update_location.save()
                                            break
                                        else:
                                            continue
                                    break
                                elif count0 == (a):
                                    for k in assets_list:
                                        count += 1
                                        asset_id2 = model_to_dict(k)["tag_id"]
                                        id2 = model_to_dict(k)["id"]
                                        if str(asset_id2) == tag_id:
                                            print("This asset is moved from its place without permission!!!")
                                            update_location = assets_list.get(id=id2)
                                            update_location.asset_location = location
                                            update_location.save()
                                            return HttpResponse("Moved" + tag_id + location, content_type='text/plain')
                                            break
                                        elif count == (assets_list_count):
                                            print("This id belong to no assets registered.")
                                            break
                                        else:
                                            continue
                                else:
                                    continue
                        elif reader_id[3:] == "01":
                            for k in employees_list:
                                employee_id12 = model_to_dict(k)["employee_id"]
                                count += 1
                                if tag_id == str(employee_id12):
                                    for j in assets_borrowed:
                                        count0 += 1
                                        id0 = model_to_dict(j)["id"]
                                        employee_id1 = j.employee_id.employee_id
                                        employee_scan_checker = model_to_dict(j)["employee_id_scanned"]
                                        if tag_id == str(employee_id1):
                                            print("There is request for this employee.")
                                            update_employee_checker = assets_borrowed.get(id=id0)
                                            update_employee_checker.employee_id_scanned = 1
                                            update_employee_checker.save()
                                            update_employee_checker.reader_code = reader_id0[0:3]
                                            update_employee_checker.save()
                                            return HttpResponse("scan asset", content_type='text/plain')
                                            break
                                        elif count0 == (a):
                                            print("There is no request for this employee id")
                                            return HttpResponse("no request for employee", content_type='text/plain')
                                            break
                                        else:
                                            continue
                                    break
                                elif count == employees_list_count:
                                    print("This is not an employee ID!!")
                                    return HttpResponse("not employee id", content_type='text/plain')
                                    break
                                else:
                                    continue


                        elif reader_id[3:] == "02":
                            for k in assets_list:
                                asset_id3 = model_to_dict(k)["tag_id"]
                                asset_status = model_to_dict(k)["asset_status"]
                                id5 = model_to_dict(k)["id"]
                                count += 1
                                if tag_id == str(asset_id3):
                                    for j in assets_borrowed:
                                        count0 += 1
                                        id1 = model_to_dict(j)["id"]
                                        asset_id1 = j.tag_id.tag_id
                                        reader_id_code = model_to_dict(j)["reader_code"]
                                        employee1_scan_checker = model_to_dict(j)["employee_id_scanned"]
                                        asset1_scan_checker = model_to_dict(j)["asset_id_scanned"]
                                        if tag_id == str(asset_id1) and employee1_scan_checker == 1 and reader_id[0:3] == reader_id_code:
                                            print("There is request for this asset.")
                                            update_asset_checker = assets_borrowed.get(id=id1)
                                            update_asset_checker.asset_id_scanned = 1
                                            update_asset_checker.save()

                                            update_asset_status = assets_list.get(id=id5)
                                            update_asset_status.asset_status = "Taken"
                                            update_asset_status.save()
                                            return HttpResponse("asset scanned", content_type='text/plain')
                                            break
                                        elif tag_id == str(asset_id1) and employee1_scan_checker == 1 and asset1_scan_checker == 1:
                                            print("Asset Alread Scanned.")
                                            return HttpResponse("already scanned", content_type='text/plain')
                                        elif tag_id == str(asset_id1) and employee1_scan_checker == 0:
                                            print("Scan your employee ID first.")
                                            return HttpResponse("scan employee id first", content_type='text/plain')
                                            break
                                        elif count0 == (a):
                                            print("There is no request for this asset id")
                                            return HttpResponse("no request for asset", content_type='text/plain')
                                            break
                                        else:
                                            continue
                                    break
                                elif count == assets_list_count:
                                    print("This not an asset ID!!")
                                    return HttpResponse("not asset id", content_type='text/plain')
                                    break
                                else:
                                    continue
                break
            else:
                print("You are not authorized.!!")
                return HttpResponse("not authorized", content_type='text/plain')
                break
    return HttpResponse(" ",  content_type='text/plain')
