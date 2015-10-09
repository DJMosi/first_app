from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        fields = ['full_name', 'age', 'email', 'interests']
        model = Student
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age > 120:
            raise forms.ValidationError('You are too old for this class')

        elif age < 10:
            raise forms.ValidationError('You may be too young')

        return age


class FeedbackForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

    def clean_message(self):
		message = self.cleaned_data.get('message')
		if message == 'Dirty':
			message == 'Clean'
		print(message)
		return message
