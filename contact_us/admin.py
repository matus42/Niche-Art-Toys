from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')  # Customize to display these fields
    search_fields = ('name', 'subject')  # Allow searching by name and subject

admin.site.register(Contact, ContactAdmin)
