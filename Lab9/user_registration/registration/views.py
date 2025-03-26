from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            contact_number = form.cleaned_data['contact_number']

            # Store data and redirect to success page
            return redirect('success', username=username, email=email, contact_number=contact_number)
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def success(request, username, email, contact_number):
    return render(request, 'registration/success.html', {
        'username': username,
        'email': email,
        'contact_number': contact_number
    })
