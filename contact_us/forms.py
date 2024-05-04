from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name *'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email *'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject *'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message *'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Field('name', css_class='stripe-style-input'),
            Field('email', css_class='stripe-style-input'),
            Field('subject', css_class='stripe-style-input'),
            Field('message', css_class='stripe-style-input', rows="3"),
            Submit('submit', 'Send', css_class='btn btn-primary')
        )
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1 profile-form-input'
            field.label = False
