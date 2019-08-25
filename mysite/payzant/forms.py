from django import forms

from .models import DbSalesDetailCustomerType

class ItemForm(forms.ModelForm):
	class Meta:
		model = DbSalesDetailCustomerType
		fields = '__all__'

class InputForm(forms.ModelForm):
	class Meta:
		model = DbSalesDetailCustomerType
		fields = [
		'storenumber',
		'itemnumber',
		'date'
		]
