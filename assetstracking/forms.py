from django.forms import ModelForm
from .models import Borrowing, Tag


class BorrowingForm(ModelForm):
    class Meta:
        model = Borrowing
        fields = ['borrowing_id', 'end_date', 'employee_id', 'tag_id']
        
class AssetForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_id', 'asset_name', 'rfid_id']
