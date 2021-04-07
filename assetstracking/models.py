from django.db import models


# Create your models here.

class Subscriber(models.Model):
    subscriber_id = models.IntegerField(null=True)
    subscriber_name = models.CharField(max_length=200, null=True)
    
    def __str__(self): return self.subscriber_name


class Employee(models.Model):
    employee_id = models.IntegerField(null=True)
    employee_name = models.CharField(max_length=200, null=True)
    employee_salary = models.FloatField(null=True)
    

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

    subscriber_id = models.ManyToManyField(Subscriber)

    def __str__(self): return self.asset_name


class Borrowing(models.Model):
    borrowing_id = models.IntegerField(null=True)
    start_date = models.DateField(auto_now_add=True, null=True)
    end_date = models.DateField(null=True)

    subscriber_id = models.ManyToManyField(Subscriber)

    employee_id = models.ForeignKey(Employee, null=True, on_delete= models.SET_NULL)
    tag_id = models.ForeignKey(Tag, null=True, on_delete= models.SET_NULL)

    def __str__(self): 
        return str(self.borrowing_id)
