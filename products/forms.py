from django import forms
from .widgets import CustomClearableFileInput
from .models import Rating, Product, Category


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'comment']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'sku', 'name', 'description',
                  'is_clearance', 'stock_quantity', 'price',
                  'old_price', 'image')

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput
                             )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'
