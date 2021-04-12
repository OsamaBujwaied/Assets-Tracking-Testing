from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subscriber(models.Model):
    subscriber_id = models.IntegerField(null=True)
    subscriber_name = models.CharField(max_length=200, null=True)
    
    def __str__(self): return self.subscriber_name


class Employee(models.Model):
    employee_id = models.IntegerField(null=True)
    employee_name = models.CharField(max_length=200, null=True)
    employee_email = models.CharField(max_length=200, null=True)
    
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
     
    subscriber_id = models.ManyToManyField(Subscriber)

    def __str__(self): return self.employee_name


class RFID (models.Model):
    rfid_id = models.IntegerField(null=True)
    rfid_location = models.CharField(max_length=200, null=True)

    subscriber_id = models.ManyToManyField(Subscriber)

    def __str__(self): return str(self.rfid_id)



class Tag(models.Model):
    tag_id = models.IntegerField(null=True)
    asset_name = models.CharField(max_length=200, null=True)
    STATUS = (('Available','Available'),('Taken','Taken'),)
    asset_status = models.CharField(max_length=200, null=True, choices=STATUS)

    subscriber_id = models.ManyToManyField(Subscriber)
    rfid_id = models.ManyToManyField(RFID)
    asset_location = models.CharField(max_length=200, null=True)

    def __str__(self): return self.asset_name


class Borrowing(models.Model):
    borrowing_id = models.IntegerField(null=True)
    start_date = models.DateField(auto_now_add=True, null=True)
    end_date = models.DateField(null=True)

    subscriber_id = models.ManyToManyField(Subscriber)

    employee_id = models.ForeignKey(Employee, null=True, on_delete= models.SET_NULL)
    tag_id = models.ForeignKey(Tag, null=True, on_delete= models.SET_NULL)

    employee_id_scanned = models.IntegerField(null=True,default=0)
    asset_id_scanned = models.IntegerField(null=True,default=0)
    reader_code = models.CharField(max_length=200, null=True, default=0)

    def __str__(self): 
        return str(self.borrowing_id)
        
class ClientAuth(models.Model):
    client_username = models.CharField(max_length=20, null=True)
    client_password = models.CharField(max_length=20, null=True)

    def __str__(self): 
        return str(self.client_username)