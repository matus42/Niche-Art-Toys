from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact
from django.views.decorators.http import require_POST

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


@require_POST
def delete_contact(request, contact_id):
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to perform this action.")
        return redirect('contact')

    try:
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        messages.success(request, "Contact message deleted successfully.")
    except Contact.DoesNotExist:
        messages.error(request, "Contact message not found.")

    return redirect('contact')