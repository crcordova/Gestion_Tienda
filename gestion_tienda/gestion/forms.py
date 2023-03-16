from django import forms

from django.forms import fields, models, widgets
from django.utils.regex_helper import Choice

from .models import Compra, Producto, Proveedor

dt_choice = [('Anuales', 'Anual'), ('Mensuales', 'Mensual'),('Diarias','Diario')]
vista_choice = [('cantidad', 'Cantidad'), ('venta', 'Venta')]
vista_choice_buy = [('cantidad', 'Cantidad'), ('dinero', 'Dinero')]

class FormDates(forms.Form):

    date_1 = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(2010, 2025)))
    date_2 = forms.DateField(widget=forms.SelectDateWidget())
    dt_type = forms.ChoiceField(widget=forms.RadioSelect, choices=dt_choice)

class FormSalesByProduct(forms.Form):

    date_1 = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(2010, 2025)))
    date_2 = forms.DateField(widget=forms.SelectDateWidget())
    dt_type = forms.ChoiceField(widget=forms.RadioSelect, choices=dt_choice)
    view_type = forms.ChoiceField(widget=forms.RadioSelect, choices=vista_choice)
    product = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset=Producto.objects.all(),required=False)

class FormSalesType(forms.Form):
    date_1 = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(2010, 2025)))
    date_2 = forms.DateField(widget=forms.SelectDateWidget())
    view_type = forms.ChoiceField(widget=forms.RadioSelect, choices=vista_choice)

class FormDateView(forms.Form):

    date_1 = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(2010, 2025)))
    date_2 = forms.DateField(widget=forms.SelectDateWidget())
    dt_type = forms.ChoiceField(widget=forms.RadioSelect, choices=dt_choice)
    view_type = forms.ChoiceField(widget=forms.RadioSelect, choices=vista_choice_buy)

class FormProveedor(forms.Form):
    date_1 = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(2010, 2025)))
    date_2 = forms.DateField(widget=forms.SelectDateWidget())
    view_type = forms.ChoiceField(widget=forms.RadioSelect, choices=vista_choice_buy)
    proveedor = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset=Proveedor.objects.all(),required=False)

class FormStock(forms.Form):
    product = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset=Producto.objects.all(),required=False)