# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    # Valida un solo campo

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_query = User.objects.filter(username=username).exists()

        if username_query:
            raise forms.ValidationError('Username is already in use.')

        # Debe regresarse el campo
        return username

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)

        profile.save()
