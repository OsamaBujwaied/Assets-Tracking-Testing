  
from django.contrib import admin
from .models import Subscriber, Employee, RFID, Tag, Borrowing, ClientAuth
from .models import *

# Register your models here.

admin.site.register(Subscriber)
admin.site.register(Employee)
admin.site.register(RFID)
admin.site.register(Tag)
admin.site.register(Borrowing)
admin.site.register(ClientAuth)


'''
admin.site.register(subscribers)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_email', 'user')
admin.site.register(Employees, EmployeeAdmin)

class AssetsAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'asset_name', 'asset_status', 'rfid_location')
admin.site.register(Tag, AssetsAdmin)

class BorrowedAssetsAdmin(admin.ModelAdmin):
    list_display = ('start_time0', 'end_time0', 'asset_id', 'employee_id', 'employee_id_scanned', 'asset_id_scanned')
admin.site.register(BorrowedAssets, BorrowedAssetsAdmin)

class ReadersAdmin(admin.ModelAdmin):
    list_display = ('reader_id', 'reader_location')
admin.site.register(Redaers, ReadersAdmin)

class ClientAuthAdmin(admin.ModelAdmin):
    list_display = ('client_username', 'client_password')
admin.site.register(ClientAuth, ClientAuthAdmin)
'''
