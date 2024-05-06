from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact
from django.views.decorators.http import require_POST


def contact(request):
    """
    View function for handling the contact page.
    """
    form = ContactForm(request.POST or None)
    contact_messages = (Contact.objects.order_by('-created_at')
                        if request.user.is_superuser else None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(
            request,
            'Thank you for contacting us! '
            'We will contact you by email as soon as possible.'
            )
        return redirect('contact')

    return render(request, 'contact_us/contact.html', {
        'form': form,
        'contact_messages': contact_messages
    })


@require_POST
def delete_contact(request, contact_id):
    """
    View function for deleting a contact message.
    This view requires the user to be a superuser.
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            "You are not authorized to perform this action.")
        return redirect('contact')

    try:
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        messages.success(request, "Contact message deleted successfully.")
    except Contact.DoesNotExist:
        messages.error(request, "Contact message not found.")

    return redirect('contact')
