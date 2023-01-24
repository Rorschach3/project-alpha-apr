from django import forms


class LogInForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(
        label="Password",
        max_length=150,
        widget=forms.PasswordInput
        )
