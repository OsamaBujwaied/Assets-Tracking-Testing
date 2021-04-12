  
from django.contrib import admin
from .models import Subscriber, Employee, RFID, Tag, Borrowing, ClientAuth

# Register your models here.
'''
admin.site.register(Subscriber)
admin.site.register(Employee)
admin.site.register(RFID)
admin.site.register(Tag)
admin.site.register(Borrowing)
admin.site.register(ClientAuth)


'''
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('subscriber_id', 'subscriber_name')
admin.site.register(Subscriber, SubscriberAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_email', 'user')
admin.site.register(Employee, EmployeeAdmin)

class AssetsAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'asset_name', 'asset_status', 'asset_location')
admin.site.register(Tag, AssetsAdmin)

class BorrowedAssetsAdmin(admin.ModelAdmin):
    list_display = ('borrowing_id', 'start_date', 'end_date', 'employee_id', 'tag_id', 'employee_id_scanned', 'asset_id_scanned', 'reader_code')
admin.site.register(Borrowing, BorrowedAssetsAdmin)

class ReadersAdmin(admin.ModelAdmin):
    list_display = ('rfid_id', 'rfid_location')
admin.site.register(RFID, ReadersAdmin)

class ClientAuthAdmin(admin.ModelAdmin):
    list_display = ('client_username', 'client_password')
admin.site.register(ClientAuth, ClientAuthAdmin)
