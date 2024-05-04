from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message','created_at')
    search_fields = ('name', 'subject')

admin.site.register(Contact, ContactAdmin)
