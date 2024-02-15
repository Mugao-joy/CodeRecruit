from django import forms
from .models import jobs

class jobform(forms.ModelForm):
    class Meta:
        model = jobs
        fields = [
            'company',
            'job_title',
            'requirements',
            'salary'
        ]