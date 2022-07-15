from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Locations
from django import forms

# Input for for calculator
class CalculatorForm(forms.Form):
    # Start location of contract
    origin = forms.ModelChoiceField(queryset=Locations.objects.filter(origin=True), widget=forms.Select(attrs={'class': 'bg-dark text-white p-3', 'style': 'box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2); padding: 12px 16px;'}))
    # Finish location of contract
    destination = forms.ModelChoiceField(queryset=Locations.objects.filter(destination=True), widget=forms.Select(attrs={'class': 'bg-dark text-white p-3'}))
    # Collateral value of courier package
    collateral = forms.IntegerField(max_value=2000000000, min_value=0, widget=forms.NumberInput(attrs={'class': 'bg-dark text-white p-3'}))
    # Volume of courier package
    volume = forms.FloatField(max_value=60000, min_value=0.01, widget=forms.NumberInput(attrs={'class': 'bg-dark text-white p-3'}))




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))