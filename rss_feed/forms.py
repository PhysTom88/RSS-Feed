from django import forms
from django.contrib.auth.models import User

from .models import RssFeed


class Email(forms.EmailField):

    def clean(self, value):
        super(Email, self).clean(value)
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("This email is already registered.")
        except User.DoesNotExist:
            return value


class UserForm(forms.ModelForm):

    MIN_LENGTH = 8

    password_init = forms.CharField(widget=forms.PasswordInput(),
                                    label="Password")
    password_check = forms.CharField(widget=forms.PasswordInput(),
                                     label="Please re-enter your password")
    email = Email()

    def clean_password_init(self):
        if self.data['password_init'] != self.data['password_check']:
            raise forms.ValidationError("Passwords do not match")

        if len(self.data['password_init']) < self.MIN_LENGTH:
            raise forms.ValidationError(
                "Password must be at least %d letters long" % self.MIN_LENGTH)

        return self.data['password_init']

    class Meta:
        model = User
        fields = ('email', 'password_init', 'password_check', 'first_name')


class RssSubscribeForm(forms.ModelForm):

    subscribe = forms.MultipleChoiceField(
        choices=([(name[0], name[0])
                 for name in RssFeed.objects.values_list('feed_name')]),
        widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = RssFeed
        fields = ('subscribe',)
