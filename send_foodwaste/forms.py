from django import forms
from send_foodwaste.models import Send_FoodWaste_Model

class FoodwasteForm(forms.ModelForm):
    class Meta:
        model = Send_FoodWaste_Model
        fields = ['id', 'name', 'phone_number', 'address', 'food_type', 'expiry_date', 'weight']