from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            message_body = f"Received message from {name}, Email: {email}\n\n{message}"

            send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, 'Thank you for contacting us!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact_us/contact.html', {'form': form})
