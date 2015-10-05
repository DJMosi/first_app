from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        fields = ['full_name', 'email']
        model = Student
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age > 120:
            raise forms.ValidationError('You are too old for this class')

        elif age < 10:
            raise forms.ValidationError('You may be too young')

        return age

