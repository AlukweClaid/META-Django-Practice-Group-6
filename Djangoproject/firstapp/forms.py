from django.forms import ModelForm
from .models import Shoes, Clothes

class ShoesForm(ModelForm):
    class Meta:
        model=Shoes
        fields='__all__'
        
class ClothesForm(ModelForm):
    class Meta:
        model=Clothes
        fields='__all__'