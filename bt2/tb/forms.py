from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('name', 'password',)
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_confirm")

        if password != confirm_password:
            self.add_error('password_confirm', "Пароли не совпадают")

        return cleaned_data
