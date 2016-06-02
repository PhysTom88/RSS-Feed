from django import forms

from django.contrib.auth.models import User

class Email(forms.EmailField): 
    
    def clean(self, value):
        super(Email, self).clean(value)
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("This email is already registered.")
        except User.DoesNotExist:
            return value


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	email = Email()

	class Meta:
		model = User
		fields = ('email', 'password')
