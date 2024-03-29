from django import forms
import datetime
from .models import Budget, Collateral, AssignQuota, AssignTerritory

from accounts.models import Profile, User
from bootstrap_datepicker_plus import MonthPickerInput, DatePickerInput
# class AssignIHEForm(forms.ModelForm):
    
#     class Meta:
#         model = AssignIHE
#         fields = ['a_senior_high', 'a_higher_education']


# class AssignICLForm(forms.ModelForm):
    
#     class Meta:
#         model = AssignICL
#         fields = ['a_retail','a_corporate','a_owwa']



class BudgetForm(forms.ModelForm):
    

    amount = forms.CharField( label='Budget Amount', widget=forms.NumberInput(),)
    arrival  = forms.DateField(widget=DatePickerInput(), label='Arrival')
    class Meta:
        model   = Budget
        fields  = (
            'amount',
            'arrival',
        ) 
    
        
    

class CollateralForm(forms.ModelForm):
    
    class Meta:
        model  = Collateral
        fields = (
            'name',
            'unit',
            'quantity',
        )
    
    def clean_name(self, *args, **kwargs):
        collateral = self.cleaned_data.get('name')
        queryset = Collateral.objects.filter(name=collateral)
        if queryset.exists():
            raise forms.ValidationError('This Name Has Already Been used')
        return collateral
    
    
def present_or_future_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return value


class AssignQuotaForm(forms.ModelForm):
    

    def __init__(self, *args, **kwargs):
        assigned_users = kwargs.pop('assigned_to',[])
        super(AssignQuotaForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': "form-control"}
        
        if assigned_users:
            self.fields['assigned_to'].queryset = assigned_users
        self.fields['assigned_to'].required = False
        
        self.fields['a_senior_high'].widget.attrs['placeholder'] = 'Number of Students'
        self.fields['a_senior_high'].required = False
        
        self.fields['a_higher_education'].widget.attrs['placeholder'] = 'Number of Students'
        self.fields['a_higher_education'].required = False
        
        self.fields['a_retail'].widget.attrs['placeholder'] = 'Amount Revenue'
        self.fields['a_retail'].required = False

        self.fields['a_corporate'].widget.attrs['placeholder'] = 'Amount Revenue'
        self.fields['a_corporate'].required = False

        self.fields['a_owwa'].widget.attrs['placeholder'] = 'Amount Revenue'
        self.fields['a_owwa'].required = False

        
    class Meta:
        model = AssignQuota
        fields = (
            'assigned_to',
            'start_month',
            'end_month',
            'a_senior_high',
            'a_higher_education',
            'a_retail',
            'a_corporate',
            'a_owwa',
        )
        
        labels = {
            'assigned_to': 'Assign User ',
            'a_senior_high': 'Senior High',
            'a_higher_education': 'Higher Education',
            'a_retail': 'Retail',
            'a_corporate': 'Corporate',
            'a_owwa':'OWWA',
        }
        
        

        widgets ={
            'start_month': MonthPickerInput().start_of('Assign Quota'),
            'end_month': MonthPickerInput().end_of('Assign Quota'),
        }
        validators = {
            'start_month':[present_or_future_date],
            'end_month':[present_or_future_date],
        }
        
    def clean(self):
        cleaned_data = super(AssignQuotaForm, self).clean()
        start_month = cleaned_data.get("start_month")
        end_month = cleaned_data.get("end_month")

        if start_month and end_month:
            if start_month > end_month:
                raise forms.ValidationError('Please Enter A Valid Date')
        
            if start_month < datetime.date.today():
                raise forms.ValidationError("The date cannot be in the past!")
            
            if end_month < datetime.date.today():
                raise forms.ValidationError("The date cannot be in the past!")

class AssignTerritoryForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        assigned_users = kwargs.pop('assigned_to',[])
        super(AssignTerritoryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': "form-control"}
        
        if assigned_users:
            self.fields['assigned_to'].queryset = assigned_users
        self.fields['assigned_to'].required = False
 
    
    class Meta:
        model = AssignTerritory
        fields = (
            'territory_choices',
            'assigned_to',
        )
  