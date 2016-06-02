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
    password_init = forms.CharField(widget=forms.PasswordInput(),
                                    label="Password")
    password_check = forms.CharField(widget=forms.PasswordInput(),
                                     label="Please re-enter your password")
    email = Email()

    def clean_password_init(self):
        if self.data['password_init'] != self.data['password_check']:
            raise forms.ValidationError("Passwords do not match")
        return self.data['password_init']

    class Meta:
        model = User
        fields = ('email', 'password_init', 'password_check', 'first_name')
