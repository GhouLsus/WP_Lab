from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=False)
    contact_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}), required=False)
