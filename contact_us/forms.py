from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Contact  

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name *'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email *'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject *'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message *', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Field('name', css_class='stripe-style-input'),
            Field('email', css_class='stripe-style-input'),
            Field('subject', css_class='stripe-style-input'),
            Field('message', css_class='stripe-style-input'),
            Submit('submit', 'Send', css_class='btn btn-primary')
        )
        # Update class for each field to ensure consistent styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1 profile-form-input'
            field.label = False
