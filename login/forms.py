from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
    helper = FormHelper()
    helper.layout = Layout(
        Fieldset(
            'Log in to Easychair',
            'username',
            'password',
        ),
        FormActions(
            Submit('login', 'Login'),
        )
    )
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Either user name or password are incorrect. Please try again.')
        return super(LoginForm, self).clean()


class registerForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Username')
    password1 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Retype password', widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    email = forms.CharField(max_length=100, label='Email')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords does not match')
        return password2

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
        ]

    helper = FormHelper()
    helper.layout=Layout(
        Fieldset(
            'New account registration',
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
        ),
        FormActions(
            Submit('register','Register')
        ),
    )