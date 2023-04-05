from django import forms
from .models import Mashins, TO, Complaint


class CarForm(forms.ModelForm):
    class Meta:
        model = Mashins
        fields = '__all__'


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = TO
        fields = '__all__'
        widgets = {
            'vid_TO': forms.RadioSelect()
        }


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'
