from django import forms

class AddWorkDetailForm(forms.Form):
    FIELD_CHOICES = [
        ('Electrical', 'Electrical'),
        ('Carpentry', 'Carpentry'),
        ('Painting', 'Painting'),
        ('HVAC', 'HVAC'),
        ('Civil', 'Civil'),
        ('POP', 'POP'),
    ]
    
    field = forms.ChoiceField(choices=FIELD_CHOICES)
    company_name = forms.CharField(max_length=100)
    contractor_name = forms.CharField(max_length=100)
    gstin = forms.CharField(max_length=15)
    location = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    projects_completed = forms.IntegerField()
    experience = forms.IntegerField()
