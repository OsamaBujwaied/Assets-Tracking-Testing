from django.forms import ModelForm
from .models import Borrowing, Tag


class BorrowingForm(ModelForm):
    class Meta:
        model = Borrowing
        fields = ['end_date', 'employee_id', 'tag_id']
        
class BorrowingFormEmployee(ModelForm):
    class Meta:
        model = Borrowing
        fields = [ 'end_date']
        
    
class AssetForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_id', 'asset_name', 'rfid_id', 'asset_status', 'asset_location']
