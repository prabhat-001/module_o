from django import forms

from .models import Guest
from .models import GuestPassport

class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = ('name', 'phone','email',)

class PassportForm(forms.ModelForm):
	class Meta:
		model = GuestPassport
		fields=('key' ,'passportphoto')

		
		
