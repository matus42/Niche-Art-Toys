from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def contact(request):
    form = ContactForm(request.POST or None)
    # Sort messages from newest to oldest by the 'created_at' field
    contact_messages = Contact.objects.order_by('-created_at') if request.user.is_superuser else None

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Thank you for contacting us!')
        return redirect('contact')

    return render(request, 'contact_us/contact.html', {
        'form': form,
        'contact_messages': contact_messages  # Updated variable name as per previous discussion
    })
