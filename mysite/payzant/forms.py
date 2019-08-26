from django import forms

from .models import DbSalesDetailCustomerType

class InputForm(forms.ModelForm):
	class Meta:
		model = DbSalesDetailCustomerType
		fields = [
		'storenumber',
		'itemnumber',
		'date'
		]

