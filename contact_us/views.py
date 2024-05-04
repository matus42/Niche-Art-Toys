from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the new contact to the database
            contact_instance = form.save()

            # Prepare and send an email notification (optional)
            message_body = f"Received message from {contact_instance.name}, Email: {contact_instance.email}\n\n{contact_instance.message}"
            print("Attempting to send email")
            send_mail(
                contact_instance.subject,
                message_body,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],  # Email recipient list
                fail_silently=False,
            )
            
            messages.success(request, 'Thank you for contacting us!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact_us/contact.html', {'form': form})
